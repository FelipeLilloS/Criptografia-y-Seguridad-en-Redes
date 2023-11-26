# Crear imagen con: sudo docker build -t c1 .
# Crear contenedor con: sudo docker run -it c1 bash
# Para levantar contenedor creado: sudo docker start -i <container_id>

FROM ubuntu:14.10
ENV DEBIAN_FRONTEND=noninteractive

RUN sed -i 's/archive.ubuntu.com/old-releases.ubuntu.com/g' /etc/apt/sources.list

RUN echo "deb http://old-releases.ubuntu.com/ubuntu/ utopic main restricted universe multiverse" > /etc/apt/sources.list && \
    echo "deb http://old-releases.ubuntu.com/ubuntu/ utopic-updates main restricted universe multiverse" >> /etc/apt/sources.list && \
    echo "deb http://old-releases.ubuntu.com/ubuntu/ utopic-security main restricted universe multiverse" >> /etc/apt/sources.list

RUN apt-get update && apt-get install -y net-tools libedit2 openssh-client openssh-server

CMD ["bash"]

