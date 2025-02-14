# Dockerfile
FROM python:3.13-alpine


LABEL maintainer="dofospider@gmail.com"
LABEL version="1.0"
LABEL description="This is a Docker image for Aliyun DDNS updater."

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "aliyunDDNS.py"]