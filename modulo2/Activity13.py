# Bucles anidados - Generar una tabla de multiplicar clásica.

for i in range(1, 11):
    for j in range(1, 11):
        print(j, "*", i, "=", j * i, end="\t") # Print the equation
    print() # Move to the next line after each row