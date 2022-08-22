# QUESTÃO
# Crie uma classe de sua preferência com, no mínimo, uma variável, um método e um incremento.
# Depois, desenvolva três ou mais objetos para testar o código.

# RESPOSTA
# Função: Desenvolvendo uma Classe
# Autor(a): Joyce Silva de Almeida
# Curso: SOFTEX - Back-End - UPE/Garanhuns-PE
# Data: 22-08-2022

# Criando a Classe

class Brinquedo:
    def __init__(self, modelo, anoFabricacao, valor):
        self.modelo = modelo
        self.anoFabricacao = anoFabricacao
        self.valor = valor
    def getModelo(self):
        return "Modelo: {}, Fabricado: {} e Valor: R$ {},00.".format(
            self.modelo, self.anoFabricacao, self.valor)
    def getFabricacao(self):
        return 2022 - self.anoFabricacao
    def getValor(self):
        return self.valor

# Testantado a classe

b1 = Brinquedo("Boneca", 1948, 120)
print(str(b1.getModelo()))
b2 = Brinquedo("Carro", 1990, 49)
print(b2.getFabricacao())
b3 = Brinquedo("Peteca", 2014, 25)
print(b3.getValor())
