class usuario:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        
    def hacer_deposito(self, amount):
        self.balance += amount
        return self
    def hacer_retiro(self, amount):
        self.balance -= amount
        return self
    def mostrar_balance_usuario(self):
        print(f"Nombre de usuario: {self.name}, Balance: {self.balance}")
        return self
    def transferir_dinero(self, destiny, amount):
        self.balance -= amount
        destiny.hacer_deposito(amount)
        return self

usuario1 = usuario("Juan", 0)
usuario2 = usuario("Francisco", 0)
usuario3 = usuario("Alexis", 0)

usuario1.hacer_deposito(50).hacer_deposito(50).hacer_deposito(50).hacer_retiro(50).mostrar_balance_usuario()

usuario2.hacer_deposito(70).hacer_deposito(70).hacer_retiro(40).hacer_retiro(40).mostrar_balance_usuario()

usuario3.hacer_deposito(200).hacer_retiro(50).hacer_retiro(50).hacer_retiro(50).mostrar_balance_usuario()

usuario1.transferir_dinero(usuario3, 100).mostrar_balance_usuario()

usuario3.mostrar_balance_usuario()