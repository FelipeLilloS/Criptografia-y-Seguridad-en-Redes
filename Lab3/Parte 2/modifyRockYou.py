nombre_archivo_entrada = "./rockyou.txt"
nombre_archivo_salida = "rockyousinStringNumerosyEspacios.txt"

lineas_procesadas = []

with open(nombre_archivo_entrada, "r", encoding="latin1") as archivo_entrada:
    for linea in archivo_entrada:
        linea_sin_espacios = linea.lstrip()
        
        if linea_sin_espacios and not linea_sin_espacios[0].isdigit():
            lineas_procesadas.append(linea_sin_espacios)

with open(nombre_archivo_salida, "w") as archivo_salida:
    archivo_salida.writelines(lineas_procesadas)

print("Proceso completado. Las líneas han sido guardadas en", nombre_archivo_salida)