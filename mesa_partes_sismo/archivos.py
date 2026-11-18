"""Módulo archivos: persistencia en archivo de texto (un expediente por línea)."""
import os

import datos

SEPARADOR = "|"


def guardar_archivo(ruta):
    """Escribe todos los expedientes; los campos se unen con '|'."""
    with open(ruta, "w", encoding="utf-8") as archivo:
        for i in range(datos.cantidad()):
            campos = [str(arreglo[i]) for arreglo in datos.TODOS]
            archivo.write(SEPARADOR.join(campos) + "\n")


def cargar_archivo(ruta):
    """Lee el archivo y llena los arreglos. Devuelve cuántos cargó."""
    datos.limpiar()
    if not os.path.exists(ruta):
        return 0
    with open(ruta, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            partes = linea.strip().split(SEPARADOR)
            if len(partes) != 12:          # línea dañada: se omite
                continue
            partes[6] = int(partes[6])     # tipo
            partes[7] = int(partes[7])     # personas
            partes[10] = int(partes[10])   # puntaje
            datos.agregar(partes)
    return datos.cantidad()
