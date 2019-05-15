FROM python:3.7-slim

WORKDIR /app

RUN echo "deb http://ftp.fr.debian.org/debian/ stretch main">/etc/apt/sources.list \
    && apt-get update \
    && apt-get install -y --no-install-recommends gcc libc6-dev libpython3.5-dev \
    && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8090
CMD ["gunicorn", "--forwarded-allow-ips=*", "--bind=0.0.0.0:8090", "--worker-class=gevent", "app:app"]
