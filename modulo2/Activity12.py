#while los bucles pueden realizar tareas más complejas, como filtrar números pares de una lista:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
index = 0

while index < len(numbers):
    if numbers[index] % 2 == 0:
        print(numbers[index])
    index += 1