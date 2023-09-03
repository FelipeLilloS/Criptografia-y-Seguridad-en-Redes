# sudo python3 pingv4.py "larycxpajorj h bnpdarmjm nw anmnb"

import sys
import time
from scapy.all import IP, ICMP, send

def generate_icmp_packets(phrase):
    # Inicializamos los valores iniciales para Identifier (BE) y Sequence Number (BE)
    identifier_be = 1
    sequence_be = 1

    # Inicializamos los valores iniciales para Identifier (LE) y Sequence Number (LE)
    identifier_le = 256
    sequence_le = 256

    # Inicializamos el contador para Identifier (IPv4)
    identifier_ipv4 = 1

    # Inicializamos el contador para Identifier (BE) para rastrear el patrón de 3 paquetes
    identifier_be_counter = 0

    # Variable con la información para el campo "DATA"
    data_icmp = " !\"#$%&'()*+,-./01234567 "

    # Obtenemos una lista de caracteres de la frase
    characters = list(phrase)

    for char in characters:
        # Obtener el timestamp actual
        timestamp = int(time.time())

        # Construir el paquete ICMP y agregar carácter + timestamp + data_icmp al campo "DATA"
        icmp_packet = IP(dst="8.8.8.8", id=identifier_ipv4) / ICMP() / (char + str(timestamp) + data_icmp)

        # Agregar los valores de Identifier (BE) al paquete
        icmp_packet[ICMP].id = identifier_be

        # Agregar los valores de Sequence Number (BE) y (LE) al paquete
        icmp_packet[ICMP].seq = sequence_be
        icmp_packet[ICMP].id_le = identifier_le
        icmp_packet[ICMP].seq_le = sequence_le

        # Enviamos el paquete ICMP
        send(icmp_packet)

        # Incrementamos los contadores de Identifiers
        identifier_ipv4 += 1

        # Actualizar los valores de Sequence Number (BE) y (LE)
        sequence_be += 1
        sequence_le += 256

        # Si Sequence Number (BE) llega a 4, lo reseteamos
        if sequence_be == 4:
            sequence_be = 1

        # Si Sequence Number (LE) llega a 1024, lo reseteamos
        if sequence_le == 1024:
            sequence_le = 256

        # Incrementamos el contador de Identifier (BE)
        identifier_be_counter += 1

        # Cambiar Identifier (BE) después de enviar 3 paquetes
        if identifier_be_counter == 3:
            identifier_be += 1
            identifier_be_counter = 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python icmp_sender.py 'frase'")
    else:
        phrase = sys.argv[1]
        generate_icmp_packets(phrase)
