FROM python:3.9-slim
LABEL maintainer="tech@careers360.com"

ENV PYTHONUNBUFFERED 1

USER root

RUN  apt-get update -y && \
     apt-get install -y gcc-x86-64-linux-gnu g++ libc6-dev unixodbc-dev linux-headers-generic make openssh-client  && \
     apt-get install -y wget && \
     apt-get install -y curl && \
     apt-get install -y vim && \
     apt-get install -y awscli && \
     apt-get install -y default-libmysqlclient-dev && \
     apt-get install -y procps


# Configure project
WORKDIR /home/ubuntu/main/cnext-search
COPY requirements.txt /home/ubuntu/main/cnext-search/requirements.txt
COPY pyproject.toml /home/ubuntu/main/cnext-search/pyproject.toml

RUN pip3 install -r requirements.txt

#test

COPY . /home/ubuntu/main/cnext-search
EXPOSE 8080
ENTRYPOINT bash ./run.bash
