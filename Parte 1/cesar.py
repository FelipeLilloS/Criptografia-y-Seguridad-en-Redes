# sudo python3 cesar.py "criptografia y seguridad en redes" 9

import sys

def cifrar_cesar(texto, corrimiento):
    texto_cifrado = ""
    
    for char in texto:
        if char.isalpha():
            mayuscula = char.isupper()
            char = char.lower()
            char_cod = ord(char)
            char_cod_cifrado = ((char_cod - ord('a') + corrimiento) % 26) + ord('a')
            
            if mayuscula:
                char_cod_cifrado -= 32
            
            char_cifrado = chr(char_cod_cifrado)
            texto_cifrado += char_cifrado
        else:
            texto_cifrado += char
    
    return texto_cifrado

if len(sys.argv) != 3:
    print("Uso: python cifrado_cesar.py <texto> <corrimiento>")
    sys.exit(1)

texto_a_cifrar = sys.argv[1]
corrimiento = int(sys.argv[2])

texto_cifrado = cifrar_cesar(texto_a_cifrar, corrimiento)
print(texto_cifrado)
