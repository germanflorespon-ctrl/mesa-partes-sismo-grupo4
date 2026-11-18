"""Módulo ordenamiento: selección O(n²) moviendo todos los arreglos paralelos."""
import datos


def intercambiar(i, j):
    """Intercambia la posición i y j en TODOS los arreglos paralelos."""
    for arreglo in datos.TODOS:
        arreglo[i], arreglo[j] = arreglo[j], arreglo[i]


def ordenar_por_codigo():
    """Ascendente por código (necesario para la búsqueda binaria)."""
    n = datos.cantidad()
    for i in range(n - 1):
        menor = i
        for j in range(i + 1, n):
            if datos.codigos[j] < datos.codigos[menor]:
                menor = j
        if menor != i:
            intercambiar(i, menor)


def ordenar_por_prioridad():
    """Descendente por puntaje; si empatan, el de menor código va primero."""
    n = datos.cantidad()
    for i in range(n - 1):
        mayor = i
        for j in range(i + 1, n):
            p_j, p_m = datos.puntajes[j], datos.puntajes[mayor]
            if p_j > p_m or (p_j == p_m and datos.codigos[j] < datos.codigos[mayor]):
                mayor = j
        if mayor != i:
            intercambiar(i, mayor)
