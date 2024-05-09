
from paquete_entregas_finales.clase_cliente import Client
from paquete_entregas_finales.funcion_select_client import select_client


Client_list =[            
Client("David","david@coder.com","JJpaso 123"),
Client("juan","juan@coder.com","La rioja 124"),
Client("Maria","mar@coder.com", "Av siempreviva 742")
]

client_select = select_client(Client_list)

while True:
    print("----MENU----")
    print("**Elija una opcion**")
    print("1- Agregar producto al carrito")
    print("2- Eliminar un producto del carrito")
    print("3- Mostrar carrito")
    print("4- cambiar de cliente")
    print("5- Salir")        

    option = input("ingrese una opcion: ")

    if option == "1":
        product = input("ingrese el producto para agregar al carrito: ").strip().capitalize()
        if product == "":
            print("**Debe ingrasar un producto!**")
        else:
            client_select.add_to_cart(product)
    elif option == "2":
        product = input("ingrese el producto para eliminar del carrito: ").strip().capitalize()
        if product == "":
            print("**No ingreso ningun producto para eliminar**")
        else:    
            client_select.delet_from_car(product)
    elif option == "3":
        client_select.show_cart()
    elif option == "4":
       client_select = select_client(Client_list)
    elif option == "5":
        print("adiooos, gracias por comprar!")
        break
    else:
        print("**Esa opcion no es correcta**")    

            




# creamos la clase cliente, con 4 atributos uno de ellos es una lista vacia para guardar los productos y 3 funciones para agregar al carrito, borrar del carrito y mostrar el carrito.

#se agrego la funcion __str__ para devolver el nombre cada vez que se lo solicite con client_select.
#para crear los clientes creamos una lista client_list, en esta lista guardaremos los clientes, para mas adelante iterarla y seleccionar con que cliente queremos comprar.

#creamos una funcion para seleccionar un cliente de la lista:

#Un for para iterar la lista y le decimos q guarde cada cliente en una variable client_position. enumeramos la lista de clientes, le indicamos con "start=1" que comience enumerando desde el 1 en [0] , 2 [1]... y que imprima esa posicion con el nombre del cliente en esa posicion.

#con un int((input()) hacemos que el usuario seleccione el numero de un cliente y lo guardamos en client_num_select.
#creamos la variable client_select y le decimos que busque la posicion ingresada dentro de la lista de clientes (client_list) y le restamos 1 para que seleccione el cliente en la posicion [0].

#por ultimo creamos un menu con un while true para invocar las funciones y los atrbutos.
