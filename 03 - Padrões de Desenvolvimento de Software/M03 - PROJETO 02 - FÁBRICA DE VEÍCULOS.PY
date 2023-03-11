from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, modelo, marca, cor, numeroRodas):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.numeroRodas = numeroRodas
        
    @abstractmethod
    def clone(self):
        pass
    
    @abstractmethod
    def represent(self):
        pass

class Carro(Veiculo):
    def __init__(self, modelo, marca, cor, numeroRodas, numeroPortas):
        super().__init__(modelo, marca, cor, numeroRodas)
        self.numeroPortas = numeroPortas
        
    def clone(self):
        return Carro(self.modelo, self.marca, self.cor, self.numeroRodas, self.numeroPortas)
    
    def represent(self):
        return f"Carro {self.marca} {self.modelo} na cor {self.cor}, com {self.numeroRodas} rodas e {self.numeroPortas} portas"

class Moto(Veiculo):
    def __init__(self, modelo, marca, cor, numeroRodas, cilindradas):
        super().__init__(modelo, marca, cor, numeroRodas)
        self.cilindradas = cilindradas
        
    def clone(self):
        return Moto(self.modelo, self.marca, self.cor, self.numeroRodas, self.cilindradas)
    
    def represent(self):
        return f"Moto {self.marca} {self.modelo} na cor {self.cor}, com {self.numeroRodas} rodas e {self.cilindradas} cilindradas"

class Aplicacao:
    def main(self):
        veiculos = [Carro("Fiesta", "Ford", "azul", 4, 4),
                    Moto("CG", "Honda", "preta", 2, 150),
                    Carro("Gol", "Volkswagen", "vermelho", 4, 2),
                    Moto("XTZ", "Yamaha", "branca", 2, 250),
                    Carro("Civic", "Honda", "prata", 4, 4),
                    Moto("Bros", "Honda", "azul", 2, 160)]
        
        clones = []
        for v in veiculos:
            clones.append(v.clone())
            
        for c in clones:
            print(c.represent())

if __name__ == '__main__':
    app = Aplicacao()
    app.main()
