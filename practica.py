"""
 En un cine, se dispone de 70 butacas distribuidas en 7 filas con 10 columnas cada una. El
 objetivo es desarrollar un sistema de turnero que permita visualizar un mapa interactivo de
 las butacas, mostrando cuáles están vacías y cuáles han sido reservadas .
 Al momento de reservar un asiento , el sistema debe registrar el nombre y el teléfono del
 cliente, y marcar el asiento como ocupado o reservado en el mapa. Además, se debe
 proporcionar la funcionalidad de consultar la información del cliente que ha reservado un
 lugar específico, permitiéndole ver sus datos de contacto .
 
"""

class Cine:
    def __init__(self):
        self.butacas = [['Vacío' for _ in range(10)] for _ in range(7)]
        self.reservaciones = {}

    def mostrar_butacas(self):
        for fila in self.butacas:
            print(" ".join(fila))
        print("\n")

    def reservar_butaca(self, fila, columna, nombre, telefono):
        if  self.butacas[fila][columna] == 'Vacío':
            self.butacas[fila][columna] = 'Usado'
            self.reservaciones[(fila, columna)] = {'nombre': nombre, 'telefono': telefono}
            print(f"Asiento en fila {fila}, columna {columna} reservado exitosamente.")
        else:
            print("El asiento ya está reservado.")

    def consultar_reservacion(self, fila, columna):
        if (fila, columna) in self.reservaciones:
            info = self.reservaciones[(fila, columna)]
            print(f"Reservado por: {info['nombre']}, Teléfono: {info['telefono']}")
        else:
            print("El asiento no está reservado.")

# Ejemplo de uso
cine = Cine()
cine.mostrar_butacas()
cine.reservar_butaca(1, 1, "Mariano", "1234567")
cine.reservar_butaca(1, 0, "Marisa", "1234568")
cine.mostrar_butacas()
cine.consultar_reservacion(1, 1)
cine.consultar_reservacion(1, 2)



