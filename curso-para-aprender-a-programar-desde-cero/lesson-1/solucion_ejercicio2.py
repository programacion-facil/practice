# Solución Ejercicio 2: Comprueba si un número es par o impar

# Pedimos al usuario que ingrese un número entero
num = int(input("Ingresa un número: "))

# Verificamos si el número es par o impar usando módulo %
if num % 2 == 0:
    print(f"El número {num} es par")
else:
    print(f"El número {num} es impar")
