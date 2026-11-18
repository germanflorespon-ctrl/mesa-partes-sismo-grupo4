"""Módulo registro: genera el código y registra expedientes validados."""
from datetime import date

import datos
from validaciones import (validar_nombre, validar_dni, validar_telefono,
                          validar_distrito, validar_descripcion,
                          validar_entero_positivo)
from clasificacion import TIPOS, calcular_puntaje, clasificar_prioridad


def generar_codigo(contador):
    """Formato SIS-AAAA-NNNN, p. ej. SIS-2026-0001."""
    return "SIS-" + str(date.today().year) + "-" + str(contador).zfill(4)


def siguiente_numero():
    """Toma el mayor correlativo existente y le suma 1."""
    mayor = 0
    for codigo in datos.codigos:
        numero = int(codigo.split("-")[2])
        if numero > mayor:
            mayor = numero
    return mayor + 1


def pedir_dato(mensaje, validador, error):
    """Repite la lectura hasta que el dato cumpla la regla."""
    valor = input(mensaje).strip()
    while not validador(valor):
        print("  [!] " + error)
        valor = input(mensaje).strip()
    return valor


def registrar_expediente():
    print("\n--- NUEVO REPORTE DE EMERGENCIA ---")
    nombre = pedir_dato("Nombres y apellidos: ", validar_nombre,
                        "Solo letras y espacios, minimo 5 caracteres.")
    dni = pedir_dato("DNI: ", validar_dni, "El DNI debe tener 8 digitos.")
    telefono = pedir_dato("Telefono: ", validar_telefono,
                          "9 digitos y debe iniciar con 9.")
    distrito = pedir_dato("Distrito: ", validar_distrito,
                          "Distrito no registrado en la lista.")
    direccion = input("Direccion: ").strip()

    for i in range(len(TIPOS)):
        print("  " + str(i + 1) + ". " + TIPOS[i])
    tipo = int(pedir_dato("Tipo de reporte (1-4): ",
                          lambda t: t in ["1", "2", "3", "4"],
                          "Elija una opcion entre 1 y 4."))
    cant = int(pedir_dato("Personas afectadas: ", validar_entero_positivo,
                          "Debe ser un entero mayor o igual a 1."))
    vuln = pedir_dato("Hay personas vulnerables? (S/N): ",
                      lambda r: r.upper() in ["S", "N"], "Responda S o N.")
    vuln = "Si" if vuln.upper() == "S" else "No"
    descripcion = pedir_dato("Descripcion breve: ", validar_descripcion,
                             "Minimo 10 caracteres, sin el simbolo |.")

    puntaje = calcular_puntaje(tipo, cant, vuln)
    prioridad = clasificar_prioridad(puntaje)
    codigo = generar_codigo(siguiente_numero())

    datos.agregar([codigo, nombre.title(), dni, telefono, distrito.title(),
                   direccion, tipo, cant, vuln, descripcion, puntaje, prioridad])

    print("\n  Expediente registrado: " + codigo)
    print("  Puntaje: " + str(puntaje) + "  ->  Prioridad: " + prioridad.upper())
    return codigo
