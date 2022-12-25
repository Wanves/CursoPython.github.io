# edades = [12,11,24,23,32,78,96,8,6,14,7]

# def mayorEdad(edad):
#     return edad >= 18
       
# # print(filter(mayorEdad,edades))

# edadesMayoresEdad = list(filter(mayorEdad,edades))
# print(edadesMayoresEdad)

# legajos = [777111,777222,777333,666111,666222,666333]

# def legajos777(siete):
#     return siete <= 777000

# legajosMayoresSiete = list(filter(legajos777,legajos))
# # print(legajosMayoresSiete)

class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    
    def getNombre(self):
        return self.__nombre
    def getEdad(self):
        return self.__edad    

    def __str__(self):
        return f'Nombre: {self.__nombre} \nEdad: {self.__edad}'
        
personas = [Persona('Juan', 10),
            Persona('Pedro', 12),
            Persona('Maria', 23),
            Persona('Esteban', 14),
            Persona('Claudio', 25),
            Persona('Ramón', 36)]

def mostrarPersonas(personas1):
    return personas1


personasMayoresEdad = list(filter(mostrarPersonas,personas ))
for i in personas:
    print(i)
