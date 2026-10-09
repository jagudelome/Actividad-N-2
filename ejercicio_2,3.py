from enum import Enum
class Comb (Enum):
    GASOLINA = 1; BIOETANOL = 2; DIESEL = 3; BIODIESEL = 4; GAS_NATURAL = 5
class Tipo (Enum):
    CIUDAD = 1; SUBCOMPACTO = 2; COMPACTO = 3; FAMILIAR = 4; EJECUTIVO = 5; SUV = 6
class Color (Enum):
    BLANCO = 1; NEGRO = 2; ROJO = 3; NARANJA = 4; AMARILLO = 5; VERDE = 6; AZUL = 7; VIOLETA = 8
class Automovil:
    def __init__(self, marca, mod, motor, comb, tipo, num_puertas, cant_asientos, vel_max, color, vel_act=0):
        self._marca = marca
        self._mod = mod
        self._motor = motor
        self._comb = comb
        self._tipo = tipo
        self._num_puertas = num_puertas
        self._cant_asientos = cant_asientos
        self._vel_max = vel_max
        self._color = color
        self._vel_act = vel_act
    def get_vel_act(self):
        return self._vel_act
    def set_vel_act(self, vel):
        self._vel_act = vel
        print(f"-> Velocidad actual seteada a: {self._vel_act} km/h")
    def acelerar(self, incremento):
        if self._vel_act + incremento > self._vel_max:
            print("No es posible acelerar mas de la velocidad maxima")
        else:
            self._vel_act += incremento
        print(f"Velocidad actual tras acelerar: {self._vel_act} km/h")
    def desacelerar(self, decremento):
        if self._vel_act - decremento < 0:
            print("No es posible desacelerar menos")
        else:
            self._vel_act -= decremento
        print(f"Velocidad actual tras desacelerar: {self._vel_act} km/h")
    def frenar(self):
        self._vel_act = 0
        print(f"frenar : Velocidad actual: {self._vel_act} km/h")
    def tiempo_llegada(self, distancia):
        if self._vel_act == 0:
            return "Error: El auto esta quieto (velocidad 0)"
        return distancia / self._vel_act
    def mostrar_datos(self):
        print("\n--- DATOS DEL AUTOMÓVIL ---")
        print(f"Marca: {self._marca} | Mod: {self._mod} | Motor: {self._motor}L")
        print(f"Puertas: {self._num_puertas} | Asientos: {self._cant_asientos}")
        print(f"Vel Máx: {self._vel_max} km/h | Vel Act: {self._vel_act} km/h")
        print(f"Combustible: {self._comb.name} | Tipo: {self._tipo.name} | Color: {self._color.name}")
def main():
    auto = Automovil(marca="Toyota", mod=2026, motor=2.0, comb=Comb.GASOLINA, tipo=Tipo.COMPACTO, num_puertas=4, cant_asientos=5, vel_max=150, color=Color.BLANCO)
    
    auto.mostrar_datos()
    auto.set_vel_act(100)  
    auto.acelerar(20)      
    auto.desacelerar(50)   
    auto.frenar()          

if __name__ == "__main__":
    main()