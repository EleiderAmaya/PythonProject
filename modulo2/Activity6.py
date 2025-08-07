# Ejercicio 6 del modulo 2 - Toma de decisiones
import random
# Set the secret_number variable here (between 1 and 10) - Establezca aquí la variable secret_number (entre 1 y 10).
secret_number = 8
# Initialize the guess variable here with a value of 0 - Inicialice la variable guess aquí con un valor de 0
guess = 0
while secret_number: # Add the while loop condition here - Agregue la condición del bucle while aquí

  guess = random.randint(1, 10)
  if guess!=secret_number:
    print("Guessing:",guess)
  else:
    print("I guessed the right number! It was",secret_number)
    break
