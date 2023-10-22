def procesar_archivo_entrada(archivo_entrada):
    resultados = []

    with open(archivo_entrada, 'r') as archivo:
        for linea in archivo:
            linea = linea.strip()
            
            if linea:
                resultado = linea[0].upper() + linea[1:] + '0' # Cambio de primer caracter a mayusculas y se agrega 0 al final.
                resultados.append(resultado)

    return resultados

def guardar_resultados(resultados, archivo_salida):
    with open(archivo_salida, 'w') as archivo:
        for resultado in resultados:
            archivo.write(resultado + '\n')


archivo_entrada = "rockyousinStringNumerosyEspacios.txt"
archivo_salida = "rockyou_mod.dic"

resultados = procesar_archivo_entrada(archivo_entrada)
guardar_resultados(resultados, archivo_salida)

print(f"Procesamiento completado. Los resultados se han guardado en '{archivo_salida}'.")