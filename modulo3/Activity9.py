def ejemplo_funcion():
    mensaje = "Hola, soy una variable local"
    print("Dentro de la función:", mensaje)

# Llamamos la función
ejemplo_funcion()

# Intentamos acceder fuera de la función
print("Fuera de la función:", mensaje)  # Esto dará un error
