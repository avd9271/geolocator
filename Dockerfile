# NOTES:
# -- -y command is 'answer yes to all prompts'
# -- 'yum clean all' clears all chached information
# -- 'sed' command is for replace

# -- centos7 comes with python 2, which is nice for us since rest of project is in python
FROM centos:centos7

# ---- INSTALL ----
# -- install postgresql with postgis instance

# update yum
RUN yum -y update; yum clean all
# repos
RUN yum -y install sudo epel-release; yum clean all
RUN yum -y install https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm; yum clean all

# install postgresql 9.6
RUN yum -y install postgresql96-server postgresql-contrib postgis; yum clean all
# install postgis2 for 9.6
RUN yum -y install postgis2_96; yum clean all

# install libs for python module psycopg2
RUN yum -y install postgresql-libs; yum clean all
RUN yum -y install python-devel postgresql-devel
RUN yum -y install gcc; yum clean all

# install pip for python
RUN yum -y install python-pip; yum clean all

# ---- /INSTALL ----



# ---- DEBUG ----
# used in debug. 'locate' command for finding files. used when debugging through container shell
RUN yum -y install mlocate; yum clean all
RUN updatedb
# ---- /DEBUG ----



# ---- PROJECT ----

# database init
RUN sudo -u postgres /usr/pgsql-9.6/bin/initdb -D /var/lib/pgsql/9.6/data

# copy over resources
COPY /resources /resources
COPY /scripts /scripts
COPY ./config.py /config.py
COPY ./main.py /main.py
COPY ./requirements.txt /requirements.txt

# pip installl requirements
RUN pip install -r requirements.txt

# expose port 80 so you can hit server
EXPOSE 80

# copy over start script
COPY ./docker_start.sh /docker_start.sh
CMD ./docker_start.sh

# ---- /PROJECT ----