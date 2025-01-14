"""
 Una oficina de atención al cliente tiene una cola de personas esperando para ser
 atendidas. Implementa un programa que:
 
 ● Agregueclientes a la cola cuando lleguen.
 ● Atiendaalosclientes en el orden en que llegaron.
 ● Permiteconsultar cuántos clientes quedan en la cola.
 
"""

from collections import deque

class atencionCliente:
    def __init__(self):
        self.cola = deque()
        
    def agregar_cliente(self, nombre):
        self.cola.append(nombre)
        print(f"{nombre} ha sido agregadoa a la cola.")
        
    def atender_cliente(self):
        if self.cola:
            cliente_atendido = self.cola.popleft()
            print(f"{cliente_atendido} esta siendo atendido.")
            
        else:
            print("No hay cliente en la cola.")
            
    def cliente_en_cola(self):
        print(f"Clientes en cola: {len(self.cola)}")
        
# Ejemplo de uso
oficina = atencionCliente()
oficina.agregar_cliente("Mariano")
oficina.agregar_cliente("Marisa")
oficina.cliente_en_cola()
oficina.atender_cliente()
oficina.cliente_en_cola()
oficina.atender_cliente()
oficina.atender_cliente()