class Curso:
    def __init__(self, nombre, nota, profesion,cursada):
        self.__nombre = nombre
        self.__nota = nota
        self.__profesion = profesion
        self.__cursada = cursada
    def getNombre(self):
        return self.__nombre
    def getNota(self):
        return self.__nota
    def getProfesion(self):
        return self.__profesion
    def getCursada(self):
        return self.__cursada
    
       
    def mostrarDatos(self): 
        print(f'{self.__nombre } {self.__nota } {self.__profesion } {self.__cursada }')
        verificando = self.__verificarDocente()
        if verificando  == True:
            print('Existe un docente asignado')
        else:
            print('No existe un docente asignado')
        
        
    def __verificarDocente(self):
        print('Verificando si existe docente asignado ')
        if self.__cursada == 'presencial':
            return True
        else:
            return False
    def mostrarVerificar(self):
        return self.__verificarDocente

       
        
curso = Curso('Cienca',10,'Investigador', 'presencial')
print([curso.getNombre(), curso.getNota(), curso.getProfesion(), curso.getCursada()])
curso.mostrarDatos()
curso.mostrarVerificar()



