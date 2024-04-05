FROM ubuntu

WORKDIR /code

COPY requirements.txt ./requirements.txt

RUN apt-get update && apt-get install -y python3-pip gunicorn \
  && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && pip install --no-cache-dir -r ./requirements.txt

COPY . .

EXPOSE 8080

CMD ["gunicorn", "-b", "0.0.0.0:8080", "myapp:server"]
