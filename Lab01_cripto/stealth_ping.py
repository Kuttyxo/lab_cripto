import sys
from scapy.all import *

def send_stealth_ping(texto, destino="127.0.0.1"):
    for char in texto:
        pkt = IP(dst=destino)/ICMP(type=8, code=0)/Raw(load=char.encode())
        send(pkt, verbose=False)
        print(f"Enviando: {char}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: sudo python3 stealth_ping.py \"mensaje\" [destino]")
        sys.exit(1)
    
    texto = sys.argv[1]         # Primer argumento = mensaje
    destino = sys.argv[2] if len(sys.argv) > 2 else "8.8.8.8"  # Segundo argumento opcional
    send_stealth_ping(texto, destino)

