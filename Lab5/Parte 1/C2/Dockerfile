# Crear imagen con: sudo docker build -t c2 .
# Crear contenedor con: sudo docker run -it c2 bash

FROM ubuntu:16.10
ENV DEBIAN_FRONTEND=noninteractive

RUN sed -i 's/archive.ubuntu.com/old-releases.ubuntu.com/g' /etc/apt/sources.list

RUN echo "deb http://old-releases.ubuntu.com/ubuntu yakkety main multiverse restricted universe" > /etc/apt/sources.list && \
    echo "deb http://old-releases.ubuntu.com/ubuntu yakkety-backports main multiverse restricted universe" >> /etc/apt/sources.list && \
    echo "deb http://old-releases.ubuntu.com/ubuntu yakkety-proposed main multiverse restricted universe" >> /etc/apt/sources.list && \
    echo "deb http://old-releases.ubuntu.com/ubuntu yakkety-security main multiverse restricted universe" >> /etc/apt/sources.list && \
    echo "deb http://old-releases.ubuntu.com/ubuntu yakkety-updates main multiverse restricted universe" >> /etc/apt/sources.list

RUN apt-get update && apt-get install -y net-tools libedit2 openssh-client openssh-server 

CMD ["bash"]

