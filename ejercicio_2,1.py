class Persona:
    def __init__(self, nombre, apellido, documento, año_nacimiento, pais, genero):
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento
        self.año_nacimiento = año_nacimiento
        self.pais = pais
        self.genero = genero

    def mostrar(self):
        print("Nombre:", self.nombre)
        print("Apellido:", self.apellido)
        print("Documento de identidad:", self.documento)
        print("Año de nacimiento:", self.año_nacimiento)
        print("Pais:", self.pais)
        print("Genero:", self.genero)

persona1 = Persona("Jeronimo", "Marin", "1017234567", 2009, "Mexico", "H")
persona2 = Persona("Laura", "Velasquez", "28876543", 2008, "Colombia", "M")

persona1.mostrar()
persona2.mostrar()