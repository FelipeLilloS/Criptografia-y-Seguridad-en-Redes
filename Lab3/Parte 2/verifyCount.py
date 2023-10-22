archivo1 = "rockyou.txt"
archivo2 = "rockyou_mod.dic"

def contar_filas(archivo):
    with open(archivo, "rb") as file:
        return sum(1 for line in file)

filas_archivo1 = contar_filas(archivo1)
print(f"Archivo '{archivo1}' cuenta con {filas_archivo1} filas.")

filas_archivo2 = contar_filas(archivo2)
print(f"Archivo '{archivo2}' cuenta con {filas_archivo2} filas.")