# Ejercicio 7 del modulo 2 - Escribir una Sentencia condicional

"""¡Bienvenido! En este diálogo, exploraremos cómo escribir una declaración condicional en Python para determinar el precio de las entradas de cine según la edad del cliente. Aquí están las reglas de precios:
Niños (menores de 12 años): $8
Adultos (12-64 años): $12
Mayores (65 años o más): $10
Aquí está lo que cubriremos:
Comprender el propósito de las declaraciones condicionales.
Identificar los componentes clave de una declaración condicional.
Escribir una declaración condicional para el problema de precios de entradas.
Discutir las aplicaciones de las declaraciones condicionales en el mundo real."""

edad = 80
if edad < 12:
  print("Valor entrada es de 8k")
elif edad >= 12 and edad <=64:
  print("Valor entrada es de 12k")
elif edad >= 65:
  print("Valor entrada es de 10k")