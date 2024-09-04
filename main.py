'''Algoritmo para calificaciones numericas y literarias.'''

# Recibe la calificación.
calificacion = float(input("Dame una calificación: "))

# Inicio de la condición:
if calificacion > 17.0:
    print("\nLa calificación es AD.")
elif(calificacion > 14.0):
    print("\nLa calificación es A.")
elif(calificacion >= 11):
    print("\nLa calificación es B.")
else:
    print("\nLa calificación es C.")

#Fin de la condición anidada.

