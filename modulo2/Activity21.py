#Escenario: Tienes una lista de calificaciones de estudiantes en un examen, y te gustaría curvar las calificaciones
# añadiendo 10 puntos a cada calificación. Esto lo almacenará en una nueva lista:

exam_scores = [55, 70, 78, 52, 68]
curve_amount = 10
# Use a list comprehension to create a new list of curved grades
curved_grades = [score + curve_amount for score in exam_scores]
print("Original scores:", exam_scores)
print("Curved scores:", curved_grades)