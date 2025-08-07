# Desafío de código funcional: Aprovechando los bucles for.
""" Tarea:
En este ejercicio, utilizarás un bucle for para mostrar valores que son divisibles entre 3 y 4.

Empezarás por 0 y seguirás hasta el final. Comenzará en 0 y pasará por valor_máximo + 1.
1. Crear un bucle for: Utilice la función range() para generar la secuencia de números.
Recuerde que range(max_value + 1) incluirá max_value en el bucle."""

max_value = 50
for value in range (max_value+1):
    if value % 3 == 0 and value % 4 == 0:
        print(value)