from Nodo import Pedido
from helpers import Menu
from lista_pedidos import Lista_Pedidos
def main():
    opcion = Menu()
    pedido = Lista_Pedidos()
    while opcion != 6 :
        if opcion == 1:
            nombre = input("Ingrese su nombre:")
            cantidad = input("Ingrese la cantidad de pizzas que desea:")
            ingrediente = input("Ingrese una opción: \n1. Pepperoni\n2. Salchica\n3. Carne\n4. Queso\n5. Piña\n").lower()
            if ingrediente == "pepperoni":
                tiempo = 3
            elif ingrediente == "salchicha":
                tiempo = 4
            elif ingrediente == "carne":
                tiempo = 10
            elif ingrediente == "queso":
                tiempo = 5
            elif ingrediente == "piña":
                tiempo = 2
            else:
                print("Está malo")
            aux = Pedido(nombre, cantidad, ingrediente, tiempo)
            pedido.insertar(aux)
        if opcion == 2:
            print("Entregar pedido")
            pedido.extraer()
            
        if opcion == 3:
            print("Ver pedidos")
            pedido.recorrer()
        if opcion == 4:
            print("En")
        if opcion ==5:
            print("José Ibarra - 202001800")
        opcion = Menu();

if __name__ == "__main__":
    main()
