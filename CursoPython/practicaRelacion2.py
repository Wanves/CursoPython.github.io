class Usuario:
    def __init__(self, nombre, edad, legajo):
        self.__nombre = nombre
        self.__edad = edad
        self.__legajo = legajo
    #----------------------------------------
    def getNombre(self):
        return self.__nombre
    def getEdad(self):
        return self.__edad
    def getLegajo(self):
        return self.__legajo
    # ----------------------------------------
    def mostrarDatos(self):
        return f'Datos de usuario \nNombre: {self.__nombre}, \nEdad: {self.__edad}, \nLegajo: {self.__legajo}'
    def datos(self):
        print(self.mostrarDatos())
    # ----------------------------------------
print(' ')
u = Usuario('Neo', 40, 777111)
u.datos()
print(' ')
print('-------------------')

class Cable_canal(Usuario):
    def __init__(self, nombre, edad, legajo,ingreso):
        super().__init__(nombre, edad, legajo)
        self.__ingreso = ingreso

    # ----------------------------------------
    def getIngreso(self):
        return self.__ingreso
    # ----------------------------------------
    def mostrarDatoUsuarioCable(self):
        return f'Datos Usuario Cable Canal \nNombre: {self.__nombre} \nEdad: {self.__edad} \nLegajo: {self.__legajo} \nAño de ingreso: {self.__ingreso}'
    def datos1(self):
        super().datos()
        print(self.__ingreso())
    # ----------------------------------------
c = Cable_canal('Zohar',49,777000,2010)
c.datos()