class Prato:
    def __init__(self, sabor="", calorias=0, preparo="", ingrediente="", tempo_preparo=0):
        self.sabor = sabor
        self.calorias = calorias
        self.preparo = preparo
        self.ingrediente = ingrediente
        self.tempo_preparo = tempo_preparo

    def definir_sabor(self):
        self.sabor = str(input("Qual o sabor do prato? "))

    def definir_calorias(self):
        self.calorias = float(input("Quantas calorias tem o seu prato? "))
    
    def definir_preparo(self):
        self.preparo = str(input("Descreva o modo de preparo: "))

    def definir_ingrediente(self):
        self.ingrediente = str(input("Quais são os ingredientes usados? "))

    def definir_tempo_preparo(self):
        self.tempo_preparo = int(input("Qual o tempo de preparo? "))

    def info(self):
        print(self)

    def __str__(self):
        return (f"\n=== Informações do Prato ===\n"
                f"Sabor: {self.sabor}\n"
                f"Calorias: {self.calorias} kcal\n"
                f"Modo de preparo: {self.preparo}\n"
                f"Ingredientes: {self.ingrediente}\n"
                f"Tempo de preparo: {self.tempo_preparo} minutos\n"
                f"============================")

prato1 = Prato()

prato1.definir_sabor()
prato1.definir_calorias()
prato1.definir_preparo()
prato1.definir_ingrediente()
prato1.definir_tempo_preparo()

print("\nPrato criado pelo usuário:")
print(prato1)
