"""Módulo busqueda: búsqueda secuencial O(n) y binaria O(log n)."""
import datos


def buscar_secuencial(codigo):
    """Recorre el arreglo de inicio a fin. Devuelve la posición o -1."""
    codigo = codigo.strip().upper()
    for i in range(len(datos.codigos)):
        if datos.codigos[i] == codigo:
            return i
    return -1


def buscar_binaria(codigo):
    """Requiere el arreglo ordenado por código. Devuelve la posición o -1."""
    codigo = codigo.strip().upper()
    inicio = 0
    fin = len(datos.codigos) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if datos.codigos[medio] == codigo:
            return medio
        elif datos.codigos[medio] < codigo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1
