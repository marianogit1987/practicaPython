
# Tabla de multiplicacion del 1 al 10

for tabla_numero in range(1, 11):
    print(f"Tabla del {tabla_numero}")
    for numero in range(1, 11):
        print(f"{numero} x {tabla_numero} = {numero * tabla_numero}")
    print()