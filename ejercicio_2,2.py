from enum import Enum
class TipoPlaneta(Enum):
    GASEOSO = 1
    TERRESTRE = 2
    ENANO = 3

class Planeta:
    def __init__(self, nombre=None, satelites=0, masa=0.0, volumen=0.0, diametro=0, distancia_sol=0, tipo=None, observable=False):
        self.nombre = nombre
        self.satelites = satelites
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.distancia_sol = distancia_sol  # En millones de kilómetros
        self.tipo = tipo
        self.observable = observable

    def valores(self):
        print(f"Planeta: {self.nombre}")
        print(f"Cantidad de satelites: {self.satelites}")
        print(f"Masa: {self.masa} kg")
        print(f"Volumen: {self.volumen} km³")
        print(f"Diametro: {self.diametro} km")
        print(f"Distancia media al Sol: {self.distancia_sol} millones de km")
        tipo_str = self.tipo.name if self.tipo else "No definido"
        print(f"Tipo de planeta: {tipo_str}")
        observable_str = "Si" if self.observable else "No"
        print(f"Observable a simple vista: {observable_str}")

    def calcular_densidad(self):
        if self.volumen == 0:
            return 0.0
        return self.masa / self.volumen

    def es_planeta_exterior(self):
        distancia_km = self.distancia_sol * 1_000_000
        limite_exterior_km = 3.4 * 149597870
        return distancia_km > limite_exterior_km


def main():
    planeta_1 = Planeta(
        nombre="Tierra",
        satelites=1,
        masa=5.972e24,         
        volumen=1.08321e12,     
        diametro=12742,
        distancia_sol=149,     
        tipo=TipoPlaneta.TERRESTRE,
        observable=True
    )


    planeta_2 = Planeta(
        nombre="Júpiter",
        satelites=95,
        masa=1.898e27,
        volumen=1.43128e15,
        diametro=139820,
        distancia_sol=778,      
        tipo=TipoPlaneta.GASEOSO,
        observable=True
    )

    lista_planetas = [planeta_1, planeta_2]

    for p in lista_planetas:
        p.valores()
        densidad = p.calcular_densidad()
        print(f"Densidad calculada: {densidad:,.2f} kg/km³")
        
        es_exterior = "Sí" if p.es_planeta_exterior() else "No"
        print(f"¿Es planeta exterior?: {es_exterior}")
        print("\n")
if __name__ == "__main__":
    main()