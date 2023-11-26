# Crear imagen con: sudo docker build -t c3 .
# Crear contenedor con: sudo docker run -it c3 bash

FROM ubuntu:18.10
ENV DEBIAN_FRONTEND=noninteractive

RUN sed -i 's/archive.ubuntu.com/old-releases.ubuntu.com/g' /etc/apt/sources.list

RUN echo "deb http://old-releases.ubuntu.com/ubuntu cosmic main multiverse restricted universe" > /etc/apt/sources.list && \
    echo "deb http://old-releases.ubuntu.com/ubuntu cosmic-backports main multiverse restricted universe" >> /etc/apt/sources.list && \
    echo "deb http://old-releases.ubuntu.com/ubuntu cosmic-proposed main multiverse restricted universe" >> /etc/apt/sources.list && \
    echo "deb http://old-releases.ubuntu.com/ubuntu cosmic-security main multiverse restricted universe" >> /etc/apt/sources.list && \
    echo "deb http://old-releases.ubuntu.com/ubuntu cosmic-updates main multiverse restricted universe" >> /etc/apt/sources.list

RUN apt-get update && apt-get install -y net-tools libedit2 openssh-client openssh-server 

CMD ["bash"]

