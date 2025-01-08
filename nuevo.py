contador = 0

while contador < 5:
    print(f"El contador es {contador}")
    contador += 2

edad = 17

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")


# Ejemplo básico en Python

for i in range(5):
    i += 1
    print(f"Iteración {i}")

# Inicializamos la variable
numero = float(input("Introduce un número (0 para terminar): "))

# Bucle while que se ejecuta hasta que la condición sea True
acum= 0
suma=0
while True:
    suma= suma + numero
    acum= acum + 1
    promedio = suma / acum
    if numero == 0:
        print("Fin de la iteración.")
        break  # Sale del bucle si la variable es 0
    else:
        print(f"El número ingresado es {numero}")
        # Pedimos un nuevo número para la siguiente iteración
        numero = float(input("Introduce un número (0 para terminar): "))
        
        
        
        
print(f"La suma de los numeros ingresados es {suma}")
print("El promedio de los numeros ingresados es " , promedio)
print("Bucle terminado.")


print(2 + 3 )