"""Módulo datos: arreglos paralelos. La posición i corresponde al mismo expediente."""

codigos = []
nombres = []
dnis = []
telefonos = []
distritos = []
direcciones = []
tipos = []
personas = []
vulnerables = []
descripciones = []
puntajes = []
prioridades = []

TODOS = [codigos, nombres, dnis, telefonos, distritos, direcciones,
         tipos, personas, vulnerables, descripciones, puntajes, prioridades]


def agregar(registro):
    """Inserta un expediente (lista de 12 campos) en todos los arreglos."""
    for k in range(len(TODOS)):
        TODOS[k].append(registro[k])


def cantidad():
    return len(codigos)


def limpiar():
    for arreglo in TODOS:
        arreglo.clear()
