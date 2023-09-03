# sudo python3 readv2.py capl1.pcapng

import sys
import os
from scapy.all import rdpcap
from termcolor import colored

# Función para aplicar el cifrado César
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            shifted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            if is_upper:
                shifted_char = shifted_char.upper()
            result += shifted_char
        else:
            result += char
    return result

# Verificar si se proporciona un nombre de archivo como argumento
if len(sys.argv) != 2:
    print("Uso: python3 programa.py archivo.pcapng")
    sys.exit(1)

archivo_pcapng = sys.argv[1]

# Verificar si el archivo existe
if not os.path.isfile(archivo_pcapng):
    print(f"El archivo {archivo_pcapng} no existe.")
    sys.exit(1)

# Leer el archivo .pcapng
paquetes = rdpcap(archivo_pcapng)

# Inicializar una variable para almacenar los caracteres
caracteres = ""

# Recorrer todos los paquetes ICMP Request y obtener el primer caracter del campo "DATA"
for paquete in paquetes:
    if paquete.haslayer("ICMP") and paquete["ICMP"].type == 8:
        data = paquete["Raw"].load.decode('utf-8', errors='ignore')
        if data:
            primer_caracter = data[0]
            caracteres += primer_caracter

# Imprimir la cadena original
print("Cadena original:", caracteres)

# Aplicar el cifrado César y buscar la frase específica
for i in range(26):
    cifrado = caesar_cipher(caracteres, i)
    if "criptografia y seguridad en redes" in cifrado:
        print(colored(f"{i}: {cifrado}", "green"))
    else:
        print(f"{i}: {cifrado}")
