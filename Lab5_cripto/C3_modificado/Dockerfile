# Dockerfile.c3_modificado (Corregido v3)
FROM ubuntu:20.10

# Arreglar repositorios
RUN sed -i -e 's/archive.ubuntu.com/old-releases.ubuntu.com/g' \
           -e 's/security.ubuntu.com/old-releases.ubuntu.com/g' /etc/apt/sources.list

# Instalar herramientas de compilación y librerías necesarias
RUN apt-get update && apt-get install -y \
    build-essential \
    wget \
    tcpdump \
    libssl-dev \
    zlib1g-dev \
    libedit-dev

# Descargar, modificar, compilar e instalar (TODO EN UNO)
RUN wget https://cdn.openbsd.org/pub/OpenBSD/OpenSSH/portable/openssh-8.3p1.tar.gz && \
    tar -xzf openssh-8.3p1.tar.gz && \
    cd openssh-8.3p1 && \
    # <<< ESTA ES LA LÍNEA CORREGIDA >>>
    sed -i 's/"OpenSSH_8.3"/"OpenSSH_?"/' version.h && \
    # Compilar e instalar el cliente modificado
    ./configure && \
    make && \
    make install

CMD ["bash"]