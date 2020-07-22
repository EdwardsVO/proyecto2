class Client:
    def __init__(self, dni, name, age, money_spent, disease):
        self.dni = dni
        self.name = name
        self.age = age
        self.money_spent = money_spent #NOTE El cliente almacena cada compra aqui
        self.disease = disease
        