"""Mesa de partes digital - Prototipo para reportes ciudadanos ante un sismo.
Grupo 4 - Fundamentos de Programación (CIIN1205P) - UPN."""
import datos
from registro import registrar_expediente
from busqueda import buscar_binaria
from ordenamiento import ordenar_por_codigo, ordenar_por_prioridad
from archivos import guardar_archivo, cargar_archivo
from clasificacion import TIPOS

RUTA = "expedientes.txt"
NIVELES = ["Critico", "Alto", "Medio", "Bajo"]


def mostrar_expediente(i):
    print("  Codigo     : " + datos.codigos[i])
    print("  Ciudadano  : " + datos.nombres[i] + "  (DNI " + datos.dnis[i] + ")")
    print("  Telefono   : " + datos.telefonos[i])
    print("  Ubicacion  : " + datos.direcciones[i] + ", " + datos.distritos[i])
    print("  Tipo       : " + TIPOS[datos.tipos[i] - 1])
    print("  Afectados  : " + str(datos.personas[i]) +
          "  | Vulnerables: " + datos.vulnerables[i])
    print("  Descripcion: " + datos.descripciones[i])
    print("  Prioridad  : " + datos.prioridades[i].upper() +
          " (" + str(datos.puntajes[i]) + " pts)")


def listar():
    print("\n  {:<14}{:<26}{:<20}{:>4}  {}".format(
        "CODIGO", "CIUDADANO", "DISTRITO", "PTS", "PRIORIDAD"))
    print("  " + "-" * 74)
    for i in range(datos.cantidad()):
        print("  {:<14}{:<26}{:<20}{:>4}  {}".format(
            datos.codigos[i], datos.nombres[i][:25], datos.distritos[i],
            datos.puntajes[i], datos.prioridades[i].upper()))


def consultar():
    codigo = input("Codigo a consultar (ej. SIS-2026-0001): ")
    ordenar_por_codigo()                     # la binaria necesita orden
    pos = buscar_binaria(codigo)
    if pos == -1:
        print("  No existe un expediente con ese codigo.")
    else:
        mostrar_expediente(pos)


def reporte():
    conteo = [0, 0, 0, 0]                    # arreglo paralelo a NIVELES
    for prioridad in datos.prioridades:
        for k in range(len(NIVELES)):
            if prioridad == NIVELES[k]:
                conteo[k] += 1
    print("\n  Casos por nivel de prioridad")
    for k in range(len(NIVELES)):
        print("  {:<8} {:>3}  {}".format(NIVELES[k], conteo[k], "#" * conteo[k]))
    print("  Total    {:>3}".format(datos.cantidad()))


def mostrar_menu():
    print("\n===== MESA DE PARTES DIGITAL - EMERGENCIA SISMICA =====")
    print("1. Registrar reporte")
    print("2. Consultar expediente por codigo")
    print("3. Listar ordenado por prioridad")
    print("4. Listar ordenado por codigo")
    print("5. Reporte de casos por prioridad")
    print("6. Guardar y salir")


def main():
    total = cargar_archivo(RUTA)
    print("Se cargaron " + str(total) + " expedientes desde " + RUTA)
    opcion = ""
    while opcion != "6":
        mostrar_menu()
        opcion = input("Opcion: ").strip()
        if opcion == "1":
            registrar_expediente()
            guardar_archivo(RUTA)            # respaldo inmediato
        elif opcion == "2":
            consultar()
        elif opcion == "3":
            ordenar_por_prioridad()
            listar()
        elif opcion == "4":
            ordenar_por_codigo()
            listar()
        elif opcion == "5":
            reporte()
        elif opcion == "6":
            guardar_archivo(RUTA)
            print("Datos guardados. Hasta luego.")
        else:
            print("  Opcion no valida.")


if __name__ == "__main__":
    main()
