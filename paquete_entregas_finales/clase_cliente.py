
class Client():
    def __init__(self,name,email,address):
        self.name = name 
        self.email = email
        self.address = address
        self.cart = []

    def add_to_cart(self,product):
        self.cart.append(product)
        print(f"{self.name} ha agregado {product} al carrito")

    def delet_from_car(self, product):
        if product in self.cart:
            self.cart.remove(product)
            print(f"**{self.name}, has eliminado {product} del carrito**")
        else:
            print(f"**el producto {product} no existe en el carrito!**")
    
    def show_cart(self):
        if self.cart:
            print(f"CARRITO DE: {self.name}")
            print("---Productos en el carrito---")
            for product in self.cart:
                print(product)
        else:
            print(f"** No hay productos en el carrito de {self.name} **")

    def __str__(self):
        return f"{self.name}"