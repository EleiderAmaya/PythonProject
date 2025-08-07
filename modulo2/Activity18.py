## crear un programa que simule un temporizador de cuenta regresiva.
# El temporizador comenzará en 10 y contará hacia atrás hasta 0, imprimiendo cada número.
# Además, cuando el temporizador llegue a 5, deberá mostrar un mensaje especial: '¡Punto medio alcanzado!'.
# y cuando el temporizador llegue a 0, deberá mostrar un mensaje especial: '¡Punto final alcanzado!'.

i=10

while i >= 0:
    if i == 5:
        print(i, "¡Punto medio alcanzado!")
    elif i == 0:
        print(i, "¡Punto final alcanzado!")
    else:
        print(i)
    i -= 1