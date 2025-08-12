def areaRectangulo(base, altura):
    """ areaRectangulo toma 2 valores numericos base * altura retornando el resultado en la variable area de valor numerico"""
    area = base * altura
    return area

area = areaRectangulo(58, 79)
print("El área del rectangulo es: ", area)

def volumen(area, altura):
    """ volumen toma el resultado area de la funciòn areaRectangulo y lo multiplica por la altura"""
    volumen = area * altura
    return volumen
volumen = volumen(area, 2)
print("El volumen del rectangulo es: ", volumen)