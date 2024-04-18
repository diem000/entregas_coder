#esta va a ser la funcion para registrar un usuario
def registrar_usuario(db):
    nombre_usuario = input("Ingrese nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    db [nombre_usuario] = contraseña
    print("Usuario cargado correctamnte!")
    
#aca vamos a guardar los usuarios registrados para despues usarlo como valor.
usuario = {}



#aca vamos a hacer la funcion para mostrar los usuarios

def mostrar_usuarios(db):
    print("estos son los usuarios registrados: ")
    for usuario, contraseña in db.items():
        print(f"usuario:  {usuario}, contraseña:  {contraseña}")

#aca vamos a hacer el login

def login(db):
    nombre_usuario = input("Ingrese nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    if nombre_usuario in db and db[nombre_usuario] == contraseña:
        print("Ingreso exitoso!")
    else:
        print("Usuario o contrasela no coinciden, vuelva a intentar!")
        
#menu

while True: 
    print("\n")
    print("1 - Registrar usuario ")
    print("2 - Mostrar usuarios ")
    print("3 - Login ")
    print("4 - Salir")

    seleccionar_opcion = input("seleccione una opcion: ")

    if seleccionar_opcion == "1":
        print(registrar_usuario(usuario))
    elif seleccionar_opcion =="2":
        print(mostrar_usuarios(usuario))
    elif seleccionar_opcion == "3":
        print(login(usuario))
    elif seleccionar_opcion == "4":
        print(" Chauuuu! ")
        break
    else:
        print("No existe esa opcion!, Intenta de nuevo")
    
