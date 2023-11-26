# Crear imagen con: sudo docker build -t c4 .
# Crear contenedor con: sudo docker run -it c4 bash
# sudo docker exec -it 252 bash


FROM ubuntu:20.10
ENV DEBIAN_FRONTEND=noninteractive

RUN sed -i 's/archive.ubuntu.com/old-releases.ubuntu.com/g' /etc/apt/sources.list

RUN echo "deb http://old-releases.ubuntu.com/ubuntu/ groovy main restricted universe multiverse" > /etc/apt/sources.list && \
    echo "deb http://old-releases.ubuntu.com/ubuntu/ groovy-updates main restricted universe multiverse" >> /etc/apt/sources.list && \
    echo "deb http://old-releases.ubuntu.com/ubuntu/ groovy-security main restricted universe multiverse" >> /etc/apt/sources.list && \
    echo "deb http://old-releases.ubuntu.com/ubuntu/ groovy-backports main restricted universe multiverse" >> /etc/apt/sources.list

RUN apt-get update && apt-get install -y net-tools libedit2 openssh-client openssh-server 

EXPOSE 22

CMD ["bash"]