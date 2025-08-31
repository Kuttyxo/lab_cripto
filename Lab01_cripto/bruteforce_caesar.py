def caesar_bruteforce(ciphertext: str):
    resultados = []
    for shift in range(26):
        descifrado = []
        for ch in ciphertext:
            if ch.isalpha():
                base = ord('A') if ch.isupper() else ord('a')
                descifrado.append(chr((ord(ch) - base - shift) % 26 + base))
            else:
                descifrado.append(ch)
        resultados.append((shift, "".join(descifrado)))
    return resultados

if __name__ == "__main__":
    mensaje_capturado = "larycxpajorj h bnpdarmjm nw anmnb"
    resultados = caesar_bruteforce(mensaje_capturado)
    for shift, texto in resultados:
        print(f"Shift {shift:2d}: {texto}")
