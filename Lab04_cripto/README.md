# Laboratorio 4 - Cifrado Simétrico

Implementación de algoritmos de cifrado simétrico en Python usando PyCryptodome.

## 🚀 Características

- Cifrado y descifrado con DES, AES-256 y 3DES
- Modo de operación CBC
- Ajuste automático de claves
- Soporte para entrada en texto y hexadecimal
- Validación de parámetros

## 📋 Requisitos

```bash
pip install pycryptodome
```

## 📝 Uso

Ejecuta el programa con:

```bash
python laboratorio4.py
```

El programa solicitará:
- Texto a cifrar
- Claves para cada algoritmo (DES, AES-256, 3DES)
- Vectores de inicialización (IV) para cada algoritmo

## 🔧 Funcionalidades

**Ajuste automático de claves:**
- Claves demasiado cortas: Se completan con bytes aleatorios
- Claves demasiado largas: Se truncán al tamaño requerido
- Claves correctas: Se usan sin modificaciones

**Algoritmos implementados:**
- DES: 8 bytes clave, 8 bytes IV
- AES-256: 32 bytes clave, 16 bytes IV
- 3DES: 16 bytes clave, 8 bytes IV

**Formatos de salida:**
- Hexadecimal
- Base64

## 📝 Ejemplo de uso

```
Texto: Hola Mundo UDP 2025
Clave DES: miclave
Clave AES-256: clave_aes_256_muy_larga_123456
Clave 3DES: clave3des123456
IV DES: vectoriv
IV AES: iv_aes_16_bytes!
IV 3DES: iv3des!!
```

## 🏗️ Estructura del código

- `ajustar_clave()`: Ajusta claves al tamaño requerido
- `cifrar_*()`: Funciones de cifrado para cada algoritmo
- `descifrar_*()`: Funciones de descifrado para cada algoritmo
- `solicitar_datos()`: Interfaz de entrada de usuario
- `convertir_a_bytes()`: Conversión flexible de entradas

---

