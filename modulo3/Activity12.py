import random

def get_lucky_number():
    lucky_num = random.randint(1, 100)
    return lucky_num

lucky_number = get_lucky_number()

print("Your lucky number is:", lucky_number)