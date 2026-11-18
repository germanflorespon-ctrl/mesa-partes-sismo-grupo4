# Mesa de partes digital – Emergencia sísmica (Grupo 4)

Prototipo en Python para registrar, validar, clasificar, buscar, ordenar y almacenar
reportes ciudadanos ante un terremoto. Curso Fundamentos de Programación (CIIN1205P) – UPN.

## Ejecución
```
python main.py
```
Requiere Python 3.8 o superior, sin librerías externas.

## Módulos
| Archivo | Responsabilidad |
|---|---|
| validaciones.py | Reglas de validación por campo |
| clasificacion.py | Puntaje ponderado y nivel de prioridad |
| datos.py | Arreglos paralelos de expedientes |
| registro.py | Generación de código y registro |
| busqueda.py | Búsqueda secuencial y binaria |
| ordenamiento.py | Ordenamiento por selección |
| archivos.py | Guardar / cargar `expedientes.txt` |
| main.py | Menú y flujo principal |
