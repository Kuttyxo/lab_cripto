#!/usr/bin/env python3
"""
Laboratorio 4 - Cifrado Simétrico
Algoritmos: DES, AES-256, 3DES en modo CBC
"""

import base64
import sys

try:
    from Crypto.Cipher import DES, AES, DES3
    from Crypto.Random import get_random_bytes
    from Crypto.Util.Padding import pad, unpad
except ImportError:
    print("Error: PyCryptodome no está instalado.")
    print("Ejecuta: pip install pycryptodome")
    sys.exit(1)

# =============================================================================
# FUNCIÓN PARA VALIDAR Y AJUSTAR CLAVES
# =============================================================================

def ajustar_clave(clave_bytes, tamaño_requerido, algoritmo):
    """Ajusta la clave al tamaño requerido"""
    print(f"\n--- Ajuste de clave para {algoritmo} ---")
    print(f"Clave original: {len(clave_bytes)} bytes")
    
    if len(clave_bytes) < tamaño_requerido:
        # Completar con bytes aleatorios
        bytes_faltantes = tamaño_requerido - len(clave_bytes)
        clave_completada = clave_bytes + get_random_bytes(bytes_faltantes)
        print(f"Clave completada con {bytes_faltantes} bytes aleatorios")
        print(f"Clave final: {len(clave_completada)} bytes")
        print(f"Clave final (hex): {clave_completada.hex()}")
        return clave_completada
    
    elif len(clave_bytes) > tamaño_requerido:
        # Truncar la clave
        clave_truncada = clave_bytes[:tamaño_requerido]
        print(f"Clave truncada a {tamaño_requerido} bytes")
        print(f"Clave final: {len(clave_truncada)} bytes")
        print(f"Clave final (hex): {clave_truncada.hex()}")
        return clave_truncada
    
    else:
        print("Clave ya tiene el tamaño correcto")
        print(f"Clave final: {len(clave_bytes)} bytes")
        print(f"Clave final (hex): {clave_bytes.hex()}")
        return clave_bytes

# =============================================================================
# FUNCIONES DE CIFRADO Y DESCIFRADO
# =============================================================================

def cifrar_des(texto, clave, iv):
    """Cifrado DES en modo CBC"""
    try:
        cipher = DES.new(clave, DES.MODE_CBC, iv)
        texto_padded = pad(texto, DES.block_size)
        texto_cifrado = cipher.encrypt(texto_padded)
        return texto_cifrado
    except Exception as e:
        print(f"Error en cifrado DES: {e}")
        return None

def descifrar_des(texto_cifrado, clave, iv):
    """Descifrado DES en modo CBC"""
    try:
        cipher = DES.new(clave, DES.MODE_CBC, iv)
        texto_descifrado_padded = cipher.decrypt(texto_cifrado)
        texto_descifrado = unpad(texto_descifrado_padded, DES.block_size)
        return texto_descifrado
    except Exception as e:
        print(f"Error en descifrado DES: {e}")
        return None

def cifrar_aes256(texto, clave, iv):
    """Cifrado AES-256 en modo CBC"""
    try:
        cipher = AES.new(clave, AES.MODE_CBC, iv)
        texto_padded = pad(texto, AES.block_size)
        texto_cifrado = cipher.encrypt(texto_padded)
        return texto_cifrado
    except Exception as e:
        print(f"Error en cifrado AES-256: {e}")
        return None

def descifrar_aes256(texto_cifrado, clave, iv):
    """Descifrado AES-256 en modo CBC"""
    try:
        cipher = AES.new(clave, AES.MODE_CBC, iv)
        texto_descifrado_padded = cipher.decrypt(texto_cifrado)
        texto_descifrado = unpad(texto_descifrado_padded, AES.block_size)
        return texto_descifrado
    except Exception as e:
        print(f"Error en descifrado AES-256: {e}")
        return None

def cifrar_3des(texto, clave, iv):
    """Cifrado 3DES en modo CBC"""
    try:
        cipher = DES3.new(clave, DES3.MODE_CBC, iv)
        texto_padded = pad(texto, DES3.block_size)
        texto_cifrado = cipher.encrypt(texto_padded)
        return texto_cifrado
    except Exception as e:
        print(f"Error en cifrado 3DES: {e}")
        return None

def descifrar_3des(texto_cifrado, clave, iv):
    """Descifrado 3DES en modo CBC"""
    try:
        cipher = DES3.new(clave, DES3.MODE_CBC, iv)
        texto_descifrado_padded = cipher.decrypt(texto_cifrado)
        texto_descifrado = unpad(texto_descifrado_padded, DES3.block_size)
        return texto_descifrado
    except Exception as e:
        print(f"Error en descifrado 3DES: {e}")
        return None

# =============================================================================
# SOLICITUD DE DATOS Y PROGRAMA PRINCIPAL
# =============================================================================

def solicitar_datos():
    """Solicita todos los datos al usuario"""
    print("\n" + "="*60)
    print("INGRESO DE DATOS")
    print("="*60)
    
    # Texto a cifrar
    texto_plano = input("Ingrese el texto a cifrar: ").encode('utf-8')
    
    print("\n--- CLAVES ---")
    print("Puede ingresar texto o valores en hexadecimal")
    print("Ejemplo: 'mi clave' o '6d6920636c617665'")
    
    clave_des_input = input("Ingrese clave para DES: ")
    clave_aes_input = input("Ingrese clave para AES-256: ") 
    clave_3des_input = input("Ingrese clave para 3DES: ")
    
    print("\n--- VECTORES DE INICIALIZACIÓN ---")
    iv_des_input = input("Ingrese IV para DES: ")
    iv_aes_input = input("Ingrese IV para AES-256: ")
    iv_3des_input = input("Ingrese IV para 3DES: ")
    
    return {
        'texto': texto_plano,
        'claves': {
            'des': clave_des_input,
            'aes': clave_aes_input,
            '3des': clave_3des_input
        },
        'ivs': {
            'des': iv_des_input,
            'aes': iv_aes_input,
            '3des': iv_3des_input
        }
    }

def convertir_a_bytes(dato):
    """Convierte entrada a bytes, intentando hexadecimal primero"""
    try:
        # Si son solo caracteres hexadecimales, convertir desde hex
        if all(c in '0123456789abcdefABCDEF' for c in dato.strip()):
            return bytes.fromhex(dato)
        else:
            return dato.encode('utf-8')
    except:
        return dato.encode('utf-8')

def main():
    print("=" * 60)
    print("LABORATORIO 4 - CIFRADO SIMÉTRICO")
    print("DES, AES-256 y 3DES en modo CBC")
    print("=" * 60)
    
    # Solicitar datos
    datos = solicitar_datos()
    
    # Convertir todo a bytes
    clave_des_bytes = convertir_a_bytes(datos['claves']['des'])
    clave_aes_bytes = convertir_a_bytes(datos['claves']['aes']) 
    clave_3des_bytes = convertir_a_bytes(datos['claves']['3des'])
    
    iv_des_bytes = convertir_a_bytes(datos['ivs']['des'])
    iv_aes_bytes = convertir_a_bytes(datos['ivs']['aes'])
    iv_3des_bytes = convertir_a_bytes(datos['ivs']['3des'])
    
    # Ajustar claves
    print("\n" + "="*60)
    print("AJUSTE DE CLAVES")
    print("="*60)
    
    clave_des_ajustada = ajustar_clave(clave_des_bytes, 8, "DES")
    clave_aes_ajustada = ajustar_clave(clave_aes_bytes, 32, "AES-256")
    clave_3des_ajustada = ajustar_clave(clave_3des_bytes, 16, "3DES")
    
    # Ajustar IVs
    iv_des_ajustado = ajustar_clave(iv_des_bytes, 8, "IV DES")
    iv_aes_ajustado = ajustar_clave(iv_aes_bytes, 16, "IV AES")
    iv_3des_ajustado = ajustar_clave(iv_3des_bytes, 8, "IV 3DES")
    
    # =========================================================================
    # CIFRADO
    # =========================================================================
    
    print("\n" + "="*60)
    print("RESULTADOS DE CIFRADO")
    print("="*60)
    
    # DES
    print("\n--- DES ---")
    cifrado_des = cifrar_des(datos['texto'], clave_des_ajustada, iv_des_ajustado)
    if cifrado_des:
        print(f"Texto cifrado (hex): {cifrado_des.hex()}")
        print(f"Texto cifrado (base64): {base64.b64encode(cifrado_des).decode()}")
    
    # AES-256
    print("\n--- AES-256 ---")
    cifrado_aes = cifrar_aes256(datos['texto'], clave_aes_ajustada, iv_aes_ajustado)
    if cifrado_aes:
        print(f"Texto cifrado (hex): {cifrado_aes.hex()}")
        print(f"Texto cifrado (base64): {base64.b64encode(cifrado_aes).decode()}")
    
    # 3DES
    print("\n--- 3DES ---")
    cifrado_3des = cifrar_3des(datos['texto'], clave_3des_ajustada, iv_3des_ajustado)
    if cifrado_3des:
        print(f"Texto cifrado (hex): {cifrado_3des.hex()}")
        print(f"Texto cifrado (base64): {base64.b64encode(cifrado_3des).decode()}")
    
    # =========================================================================
    # DESCIFRADO
    # =========================================================================
    
    print("\n" + "="*60)
    print("RESULTADOS DE DESCIFRADO")
    print("="*60)
    
    if cifrado_des:
        print("\n--- DES ---")
        descifrado_des = descifrar_des(cifrado_des, clave_des_ajustada, iv_des_ajustado)
        if descifrado_des:
            print(f"Texto descifrado: {descifrado_des.decode('utf-8')}")
    
    if cifrado_aes:
        print("\n--- AES-256 ---")
        descifrado_aes = descifrar_aes256(cifrado_aes, clave_aes_ajustada, iv_aes_ajustado)
        if descifrado_aes:
            print(f"Texto descifrado: {descifrado_aes.decode('utf-8')}")
    
    if cifrado_3des:
        print("\n--- 3DES ---")
        descifrado_3des = descifrar_3des(cifrado_3des, clave_3des_ajustada, iv_3des_ajustado)
        if descifrado_3des:
            print(f"Texto descifrado: {descifrado_3des.decode('utf-8')}")

if __name__ == "__main__":
    main()