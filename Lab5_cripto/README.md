# Laboratorio 5: SSH Fingerprinting y Criptografía

Este repositorio contiene los Dockerfiles y la guía de ejecución para el Laboratorio 5. El objetivo es analizar, replicar y modificar el tráfico del protocolo SSH para entender el concepto de huella digital (HASSH).

## Prerrequisitos

* **Docker** instalado y corriendo.
* **Wireshark** (o `tshark`) para analizar los archivos `.pcap` generados.

## Estructura del Repositorio

* `/C1`, `/C2`, `/C3`, `/C4-S1`: Dockerfiles para los clientes base (Ubuntu 16.10, 18.10, 20.10, 22.10).
* `/C3_modificado`: Dockerfile para el cliente modificado de la Parte 2, que compila OpenSSH desde el código fuente.
* `*.pcap`: (Opcional) Las capturas de tráfico generadas.
* `README.md`: Esta guía.

## Guía de Ejecución

### Fase 0: Construcción de Imágenes

Primero, creamos la red de Docker y construimos todas las imágenes necesarias.

```bash
# 1. Crear la red virtual
docker network create lab_ssh_net

# 2. Construir las 4 imágenes base
docker build -t c1 C1/
docker build -t c2 C2/
docker build -t c3 C3/
docker build -t c4s1 C4-S1/

# 3. Construir la imagen modificada para la Parte 2
docker build -t c3_modificado C3_modificado/

# 4. Iniciar el servidor (S1) en modo 'detached'
docker run -d --name s1 --net lab_ssh_net c4s1
```

### Fase 1 Parte 1 - Captura de Clientes Base (C1, C2, C3, C4)
Para C1->S1
Terminal 1 (captura)
```bash
docker run -it --rm --name c1 --net lab_ssh_net c1 tcpdump -i eth0 -w /tmp/c1_traffic.pcap port 22
```

Terminal 2 (cliente)
```bash
docker exec -it c1 ssh prueba@s1
# Escribir 'yes', luego la contraseña 'prueba', y luego 'exit'
```

Copiar captura en terminal 2 (cliente)
```bash
docker cp c1:/tmp/c1_traffic.pcap ./c1_traffic.pcap
```

### Fase 2: Parte 2 - Replicación de Tráfico ("OpenSSH_?")
```bash
# 1. Asegurarse que S1 esté corriendo y obtener su IP
docker start s1
docker inspect s1 | grep "IPAddress"
# (Anotar la IP, ej: "172.19.0.3")

# 2. Terminal 1 (Captura):
docker run -it --rm --name c3_mod --net lab_ssh_net c3_modificado tcpdump -i eth0 -w /tmp/c3_mod_traffic.pcap port 22

# 3. Terminal 2 (Cliente Modificado):
# (Usar el path /usr/local/bin/ssh y la IP obtenida)
docker exec -it c3_mod /usr/local/bin/ssh prueba@172.19.0.3

# 4. Copiar Captura:
docker cp c3_mod:/tmp/c3_mod_traffic.pcap ./c3_mod_traffic.pcap
```

### Fase 3: Parte 3 - Modificación del Servidor (< 300 bytes)
```bash
# 1. Entrar a S1 y modificar su configuración
docker exec -it s1 bash

# (Dentro de s1) Ejecutar estos 4 comandos:
echo "KexAlgorithms diffie-hellman-group14-sha1" >> /etc/ssh/sshd_config
echo "HostKeyAlgorithms ssh-rsa" >> /etc/ssh/sshd_config
echo "Ciphers aes128-ctr" >> /etc/ssh/sshd_config
echo "MACs hmac-sha1" >> /etc/ssh/sshd_config

# (Dentro de s1) Reiniciar el servicio y salir
service ssh restart
exit

# 2. Asegurarse que S1 esté corriendo (el restart puede detenerlo)
docker start s1

# 3. Realizar la captura (en dos terminales)
# Terminal 1 (Captura):
# (Usamos /s1_mod... porque /tmp dio problemas de permisos)
docker exec -it s1 tcpdump -i lo -w /s1_mod_traffic.pcap port 22

# Terminal 2 (Cliente):
docker exec -it s1 ssh prueba@localhost
# (La conexión fallará con "Unable to negotiate...", es normal)

# 4. Detener y Copiar
# (Presionar Ctrl+C en Terminal 1)
docker cp s1:/s1_mod_traffic.pcap ./s1_mod_traffic.pcap
```

### Limpieza
```bash
# Detener y eliminar el servidor
docker stop s1
docker rm s1

# Eliminar la red
docker network rm lab_ssh_net

# (Los contenedores C1, C2, C3, C3_mod se borran solos por el flag --rm)
```