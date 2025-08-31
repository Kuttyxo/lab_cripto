import sys
import string

def caesar(texto: str, shift: int) -> str:
    def desplazar(ch, base):
        alpha = string.ascii_lowercase if base == 'a' else string.ascii_uppercase
        idx = alpha.index(ch)
        return alpha[(idx + shift) % 26]
    res = []
    for ch in texto:
        if ch.islower():
            res.append(desplazar(ch, 'a'))
        elif ch.isupper():
            res.append(desplazar(ch, 'A'))
        else:
            res.append(ch)
    return ''.join(res)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python caesar.py \"Mensaje con espacios\" shift")
        sys.exit(1)
    texto = sys.argv[1]
    try:
        shift = int(sys.argv[2])
    except ValueError:
        print("El shift debe ser un entero (puede ser negativo).")
        sys.exit(1)
    print(caesar(texto, shift))
