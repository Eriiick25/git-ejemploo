print("¡Hola, mundo!")
#modificación 1
def factorial(n):
    """Calcula el factorial de un número entero positivo."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Solicitar al usuario que ingrese un número
numero = int(input("Ingresa un número entero: "))

# Calcular y mostrar el factorial del número ingresado
print("El factorial de", numero, "es:", factorial(numero))

