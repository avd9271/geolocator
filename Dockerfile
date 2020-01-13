FROM python:3

COPY /resources /resources
COPY /scripts /scripts
COPY ./config.py /config.py
COPY ./main.py /main.py
COPY ./requirements.txt /requirements.txt

RUN pip install -r requirements.txt

EXPOSE 80

CMD python main.py