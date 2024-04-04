FROM ubuntu

WORKDIR /code

COPY requirements.txt ./requirements.txt

RUN apt-get update && apt-get install -y python3-pip gunicorn

RUN pip install --upgrade pip

RUN pip install -r ./requirements.txt

COPY . .

EXPOSE 8080

CMD ["gunicorn", "-b", "0.0.0.0:8080", "myapp:server"]
