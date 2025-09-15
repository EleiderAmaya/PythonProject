import math


def calculate_diameter_circle(radius: float) -> float:
    if radius < 0:
        return -1
    return radius * 2

print(calculate_diameter_circle(1000000))
