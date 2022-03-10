from Nodo import Pedido
class Lista_Pedidos():

    def __init__(self):
        self.cola = []

    def cantidad(self):
        return len(self.cola)
    
    
    def insertar(self, pedido):
        self.cola.append(pedido)

    def recorrer(self):
        i = 0
        for elemento in self.cola:
            i+=1
            print("Posición en cola: ",i,", Nombre del cliente: ", elemento.nombre_cliente, ", Cantidad: ", elemento.cantidad_pizzas, ", Ingrediente: ", elemento.ingrediente, ", Tiempo: ", elemento.tiempo,"min" )
    
    def extraer(self):
        if self.cola:
            for elemento in self.cola:
                print("Nombre del cliente: ", elemento.nombre_cliente, ", Cantidad: ", elemento.cantidad_pizzas, ", Ingrediente: ", elemento.ingrediente, ", Tiempo: ", elemento.tiempo,"min" )
                break
            self.cola.pop(0)
            

    def sumaTiempo(self):
        if self.cola():
            print("a")
