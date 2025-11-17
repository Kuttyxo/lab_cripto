# Dockerfile.c2
FROM ubuntu:18.10

# Actualizar repositorios a old-releases
RUN sed -i -e 's/archive.ubuntu.com/old-releases.ubuntu.com/g' \
           -e 's/security.ubuntu.com/old-releases.ubuntu.com/g' /etc/apt/sources.list

# Instalar cliente SSH y tcpdump
RUN apt-get update && \
    apt-get install -y openssh-client tcpdump

CMD ["bash"]