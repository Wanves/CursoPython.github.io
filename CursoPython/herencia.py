class Persona:
    def __init__(self, apellidoPaterno, apellidoMaterno, nombres):
        self.__apellidoPaterno = apellidoPaterno
        self.__apellidoMaterno = apellidoMaterno
        self.__nombres = nombres
        
    def getApellidoPaterno(self):
        return self.__apellidoPaterno
    def getApellidoMaterno(self):
        return self.__apellidoMaterno
    def getNombres(self):
        return self.__nombres

    def mostrarNombreCompleto(self):
        return f'Apellido paterno:{self.__apellidoPaterno} \nApellido materno:{self.__apellidoMaterno} \nNombres:{self.__nombres}'
    
    def datos(self):
        print(self.mostrarNombreCompleto())
        
p = Persona('Anderson','Gian','Neo')
print(p.mostrarNombreCompleto())


print(' ')
print('------------------------------')
print(' ')
# -------------------------------------------------------------------------------------
class Estudiante(Persona):
    
    def __init__(self,apellidoPaterno, apellidoMaterno, nombres,carrera):
        super().__init__(apellidoPaterno, apellidoMaterno, nombres)
        self.__carrera = carrera
    def getCarrera(self):
        return self.__carrera
    
    def datos(self):
        super().datos()
        print(f'Carrera:{self.__carrera}')
    
e = Estudiante('Wanvestrant','Gauna','Juan','Programador')
# print(e.mostrarNombreCompleto())
# print(f'Carrera:({e.getCarrera()})')
e.datos()