# Dockerfile.c4s1
FROM ubuntu:22.10

# <<< AÑADIR ESTA LÍNEA PARA CORREGIR EL ERROR >>>
RUN sed -i -e 's/archive.ubuntu.com/old-releases.ubuntu.com/g' \
           -e 's/security.ubuntu.com/old-releases.ubuntu.com/g' /etc/apt/sources.list

# Instalar cliente, servidor SSH y tcpdump
RUN apt-get update && \
    apt-get install -y openssh-client openssh-server tcpdump

# Crear usuario "prueba" con contraseña "prueba"
RUN useradd -m -s /bin/bash prueba && \
    echo "prueba:prueba" | chpasswd

# Configurar SSH para permitir login con contraseña
RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config
RUN sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/' /etc/ssh/sshd_config
RUN mkdir -p /run/sshd

# Exponer el puerto 22
EXPOSE 22

# Iniciar el servidor SSH
CMD ["/usr/sbin/sshd", "-D"]