FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN pwd
RUN ls

RUN apt-get update && \
    apt-get install -y postgresql-client

CMD ["python", "test.py"]
