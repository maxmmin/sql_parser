FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY sql_parser .

RUN apt-get update && \
    apt-get install -y postgresql-client

CMD [ "python", "./manage.py runserver" ]