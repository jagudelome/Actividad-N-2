import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio
    def cal_area(self):
        return math.pi * (self.radio ** 2)
    def cal_perimetro(self):
        return 2 * math.pi * self.radio
    
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def c_area(self):
        return self.base * self.altura
    def cal_perimetro(self):
        return (2 * self.base) + (2 * self.altura)

class Cuadrado:
    def __init__(self, lado):
        self.lado = lado
    def area(self):
        return self.lado ** 2
    def cal_perimetro(self):
        return 4 * self.lado

class TrianguloRectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def c_area(self):
        return (self.base * self.altura) / 2
    def cal_hipotenusa(self):
        return math.sqrt((self.base ** 2) + (self.altura ** 2))
    def cal_perimetro(self):
        return self.base + self.altura + self.cal_hipotenusa()
    def tipo(self):
        hipotenusa = self.cal_hipotenusa()
        if self.base == self.altura and self.base == hipotenusa:
            return "Equilatero"
        elif self.base != self.altura and self.base != hipotenusa and self.altura != hipotenusa:
            return "Escaleno"
        else:
            return "Isosceles"

def main():
    circulo = Circulo(5)
    rectangulo = Rectangulo(4, 6)
    cuadrado = Cuadrado(3)
    triangulo = TrianguloRectangulo(3, 4)

    print("Circulo")
    print("Area:", circulo.cal_area())
    print("Perimetro:", circulo.cal_perimetro())

    print("Rectangulo")
    print("Area:", rectangulo.c_area())
    print("Perimetro:", rectangulo.cal_perimetro())

    print("Cuadrado")
    print("Area:", cuadrado.area())
    print("Perimetro:", cuadrado.cal_perimetro())

    print("Triangulo Rectangulo")
    print("Area:", triangulo.c_area())
    print("Perimetro:", triangulo.cal_perimetro())
    print("Hipotenusa:", triangulo.cal_hipotenusa())
    print("Tipo:", triangulo.tipo())

if __name__ == "__main__":
    main()