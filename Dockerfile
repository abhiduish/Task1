FROM python 3.7.6-slim

ENV USER ABHIJEET

#creating directry for the application

RUN mkdir /code1

WORKDIR code1

RUN pip install --upgrade pip
RUN pip install django

COPY . /code1/

EXPOSE 8000

CMD ["python","magae.py","runserver","0.0.0.0.8000"]