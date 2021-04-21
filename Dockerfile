FROM ubuntu:20.04

ENV USER ABHIJEET

#creating directry for the application

RUN mkdir /code1

WORKDIR code1

RUN apt-get update -y
RUN apt-get install -y python3.4 python3-pip
RUN pip3 install Django==3.2

COPY . /code1/

EXPOSE 8000

CMD ["python","manage.py","runserver","0.0.0.0.8000"]
