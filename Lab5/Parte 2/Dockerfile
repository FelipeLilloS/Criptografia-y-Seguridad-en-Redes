# Crear imagen con: sudo docker build -t signo .
# Crear contenedor con: sudo docker run -it signo bash

FROM ubuntu:20.10
ENV DEBIAN_FRONTEND=noninteractive

RUN sed -i 's/archive.ubuntu.com/old-releases.ubuntu.com/g' /etc/apt/sources.list

RUN echo "deb http://old-releases.ubuntu.com/ubuntu/ groovy main restricted universe multiverse" > /etc/apt/sources.list && \
    echo "deb http://old-releases.ubuntu.com/ubuntu/ groovy-updates main restricted universe multiverse" >> /etc/apt/sources.list && \
    echo "deb http://old-releases.ubuntu.com/ubuntu/ groovy-security main restricted universe multiverse" >> /etc/apt/sources.list && \
    echo "deb http://old-releases.ubuntu.com/ubuntu/ groovy-backports main restricted universe multiverse" >> /etc/apt/sources.list

EXPOSE 22

RUN apt-get update && apt-get install -y openssh-server wireshark tshark
RUN apt-get update && apt-get install -y autoconf net-tools libedit2 openssl libfido2-1 libfido2-dev libfido2-doc fido2-tools libssl-dev zlib1g-dev
RUN apt-get update && apt-get install -y git gcc make nano vim

CMD ["bash"]

