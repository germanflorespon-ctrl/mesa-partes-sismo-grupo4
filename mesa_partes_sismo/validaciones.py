"""Módulo validaciones: reglas de validación de cada campo del expediente."""

DISTRITOS = ["Comas", "Los Olivos", "Independencia", "Carabayllo",
             "Puente Piedra", "San Martin de Porres", "San Luis", "Lima"]


def validar_nombre(texto):
    """Solo letras y espacios, mínimo 5 caracteres."""
    texto = texto.strip()
    if len(texto) < 5:
        return False
    for caracter in texto:
        if not (caracter.isalpha() or caracter == " "):
            return False
    return True


def validar_dni(texto):
    """Exactamente 8 dígitos numéricos."""
    texto = texto.strip()
    return len(texto) == 8 and texto.isdigit()


def validar_telefono(texto):
    """Exactamente 9 dígitos y debe iniciar con 9."""
    texto = texto.strip()
    return len(texto) == 9 and texto.isdigit() and texto[0] == "9"


def validar_distrito(texto):
    """El distrito debe estar en la lista configurada (sin importar mayúsculas)."""
    texto = texto.strip().lower()
    for distrito in DISTRITOS:
        if distrito.lower() == texto:
            return True
    return False


def validar_descripcion(texto):
    """Mínimo 10 caracteres y sin el separador | usado en el archivo."""
    texto = texto.strip()
    return len(texto) >= 10 and "|" not in texto


def validar_entero_positivo(texto):
    """Número entero mayor o igual a 1."""
    texto = texto.strip()
    return texto.isdigit() and int(texto) >= 1
