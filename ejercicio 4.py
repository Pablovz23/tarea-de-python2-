from abc import ABC, abstractmethod

# Clase abstracta (el contrato)
class FiguraGeometrica(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

# Clase concreta 1
class Circulo(FiguraGeometrica):
    def init(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.1416 * (self.radio ** 2)

# Clase concreta 2
class Rectangulo(FiguraGeometrica):
    def init(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

# Prueba corta
c = Circulo(5)
r = Rectangulo(4, 6)
print("Area Circulo:", c.calcular_area())
print("Area Rectangulo:", r.calcular_area())