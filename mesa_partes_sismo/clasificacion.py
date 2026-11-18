"""Módulo clasificacion: puntaje ponderado y nivel de prioridad."""

TIPOS = ["Persona atrapada o herida",
         "Riesgo de colapso, incendio o fuga de gas",
         "Sin agua, luz o alimentos",
         "Dano leve en vivienda"]
PUNTOS_TIPO = [5, 4, 2, 1]          # arreglo paralelo a TIPOS


def calcular_puntaje(tipo, personas, vulnerables):
    """Suma ponderada de los tres factores de riesgo (rango 2 a 10)."""
    puntaje = PUNTOS_TIPO[tipo - 1]

    if personas <= 2:
        puntaje += 1
    elif personas <= 5:
        puntaje += 2
    else:
        puntaje += 3

    if vulnerables == "Si":
        puntaje += 2
    return puntaje


def clasificar_prioridad(puntaje):
    """Convierte el puntaje en un nivel según intervalos."""
    if puntaje >= 8:
        return "Critico"
    elif puntaje >= 6:
        return "Alto"
    elif puntaje >= 4:
        return "Medio"
    else:
        return "Bajo"
