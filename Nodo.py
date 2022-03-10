class Pedido():
    def __init__(self, nombre_cliente, cantidad_pizzas, ingrediente, tiempo):
        self.nombre_cliente = nombre_cliente
        self.cantidad_pizzas = cantidad_pizzas
        self.colingredienteumn = ingrediente
        self.ingrediente = ingrediente
        self.tiempo = tiempo
    
    def getNombreCliente(self):
        return self.nombre_cliente
    
    def setNombreCliente(self, nombre_cliente):
        self.nombre_cliente = nombre_cliente

    def getCantidad(self):
        return self.cantidad_pizzas
    
    def setCantidad(self, cantidad_pizzas):
        self.cantidad_pizzas = cantidad_pizzas
    
    def getIngrediente(self):
        return self.ingrediente
    
    def setIngrediente(self, ingrediente):
        self.ingrediente = ingrediente

    def getTiempo(self):
        return self.tiempo
    
    def setTiempo(self, tiempo):
        self.tiempo = tiempo