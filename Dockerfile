# NOTES:
# -- -y command is 'answer yes to all prompts'
# -- 'yum clean all' clears all chached information
# -- 'sed' command is for replace

# -- centos7 comes with python 2, which is nice for us since rest of project is in python
FROM centos:centos7

# INSTALL
# -- install postgresql with postgis instance. 
# -- based on dockerfile from 
# -- https://github.com/CentOS/CentOS-Dockerfiles/tree/master/postgres/centos7

# update yum
RUN yum -y update; yum clean all
RUN yum -y install sudo epel-release; yum clean all
RUN yum -y install https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm; yum clean all
# RUN yum -y install https://download.postgresql.org/pub/repos/yum/11/redhat/rhel-7-x86_64/pgdg-centos11-11-2.noarch.rpm; yum clean all



# install postgresql 11
# 'postgresql-contrib' is optional argument that can be added after postgresql11-server
# 'postgis' for installing postgis. this is needed.
RUN yum -y install postgresql96-server postgresql-contrib postgis; yum clean all

# install libs for python
RUN yum -y install postgresql-libs; yum clean all
RUN yum -y install python-devel postgresql-devel
# move this to top later
RUN yum -y install gcc; yum clean all

# GARBAGE
# -- RUN yum -y install postgresql-devel; yum clean all
# -- install postgis2. the _11 refers to version 11 of postgresql
# -- RUN yum -y install postgis25_11


# START POSTGRESQL
# -- based on dockerfile from
# -- https://github.com/CentOS/CentOS-Dockerfiles/tree/master/postgres/centos7
# GARBAGE
# remove tty requirements
# this is a regex replace:
# '.*requirestty$' --> anything ending in requirestty
# '#Defaults requiretty' --> just the value replacing the strings ending in requirestty 
# RUN sed -i 's/.*requiretty$/#Defaults requiretty/' /etc/sudoers
# RUN locate initdb
# RUN sudo postgresql-setup initdb
# RUN systemctl start postgresql
# -- don't think this is necessary
# EXPOSE 5432

# -- docker setup for python code
# -- done by avd9271

RUN yum -y install python-pip; yum clean all

COPY /resources /resources
COPY /scripts /scripts
COPY ./config.py /config.py
COPY ./main.py /main.py
COPY ./requirements.txt /requirements.txt

RUN pip install -r requirements.txt


RUN sed -i 's/.*requiretty$/#Defaults requiretty/' /etc/sudoers

RUN yum -y install mlocate; yum clean all
RUN updatedb

# whole bunch of bullshit
RUN yum -y install systemd; yum clean all; \
(cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == systemd-tmpfiles-setup.service ] || rm -f $i; done); \
rm -f /lib/systemd/system/multi-user.target.wants/*;\
rm -f /etc/systemd/system/*.wants/*;\
rm -f /lib/systemd/system/local-fs.target.wants/*; \
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \
rm -f /lib/systemd/system/basic.target.wants/*;\
rm -f /lib/systemd/system/anaconda.target.wants/*;

RUN sudo -u postgres /usr/pgsql-9.6/bin/initdb -D /var/lib/pgsql/9.6/data


EXPOSE 80

RUN yum -y install postgis2_96; yum clean all

# RUN sudo -u postgres /usr/pgsql-9.6/bin/pg_ctl -D /var/lib/pgsql/9.6/data start; echo "CREATE EXTENSION postgis;" | /usr/bin/psql -U postgres -d postgres; /usr/bin/shp2pgsql -s 4326 /resources/cb_2018_us_state_500k/cb_2018_us_state_500k.shp | /usr/bin/psql -U postgres -d postgres


COPY ./docker_start.sh /docker_start.sh

CMD ./docker_start.sh
# CMD python main.py