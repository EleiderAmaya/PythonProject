# While los bucles son inestimables para tareas con un número desconocido de repeticiones.
# Vamos a simular una tirada de dados hasta obtener un 6:

import random
roll = 0
while roll != 6:
    roll = random.randint(1, 6)
    print("You rolled a", roll)