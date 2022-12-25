class Alumno:
    def __init__(self, nombre, registro):
        self.__nombre = nombre
        self.__registro = registro

    def getNombre(self):
        return self.__nombre
    def getRegistro(self):
        return self.__registro


    def __str__(self):
        print(' ')
        return f'Nombre: {self.getNombre()} - Número de Registro: {self.getRegistro()}'
        print(' ')

alumnos = [
    Alumno('Juan',777111),
Alumno('Zoe',777555),
Alumno('Maria',333555),
Alumno('Neo',222444),
Alumno('July',444111),
Alumno('Flor',111000),
Alumno('Mar',222888),
Alumno('Tina',111999),
Alumno('Gus',666999)
]

datosAlumnos = list(filter(lambda alum:alum.getNombre() > 'L',alumnos))
for alum in datosAlumnos:
    print(alum)