FROM python:3.7-alpine
EXPOSE 8000

RUN mkdir /polibrastest
WORKDIR /polibrastest 

COPY Pipfile /polibrastest
COPY Pipfile.lock /polibrastest

RUN pip install pipenv --upgrade
RUN pipenv install --system

COPY . /polibrastest 
ENTRYPOINT ["python3"] 
CMD ["manage.py", "runserver", "0.0.0.0:8000"]
