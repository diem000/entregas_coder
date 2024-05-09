
#enumeramos los clientes  
def select_client(Client_list):    
    print("**Clientes disponibles**")
    for i, client_position in enumerate(Client_list , start=1):
        print(f"{i}- {client_position}")
    #seleccionamos un cliente
    cliente_num_select = int(input("Seleccione un cliente para iniciar la compra: ")) 
    client_select = Client_list[cliente_num_select -1]
    print(f"Ha seleccionado a {client_select} \r")
    print("Hola",client_select, "Bienvenido!")
    
    return client_select