class Curso:
    def __init__(self, nombre, nota, profesion):
        self.__nombre = nombre
        self.__nota = nota
        self.__profesion = profesion
        self.__imparticion = 'Presencial'
# --------------------------------------------        
    def getNombre(self):
        return self.__nombre
    def getNota(self):
        return self.__nota
    def getProfesion(self):
        return self.__profesion
    def getImparticion(self):
        return self.__imparticion    
# --------------------------------------------
    def setNombre(self, nuevoNombre):
        self.__nombre = nuevoNombre
        print(c.getNombre())
    def setNota(self, nuevoNota):
        self.__nota = nuevoNota
        print(c.getNota())
    def setProfesion(self, nuevoProfesion):
        self.__profesion = nuevoProfesion
        print(c.getProfesion())
    def setImparticion(self, nuevoImparticion):
        self.__imparticion = nuevoImparticion
        print(c.getImparticion())
# --------------------------------------------  
    def mostrarDatos(self):
        datos = print(f'Curso: {c.__nombre} \nNota: {c.__nota} \nProfesion: {c.__profesion} \nImparticion: {c.__imparticion}')
        docenteAsignado = self.__verificarDocente()
        if docenteAsignado:
            print('Existe docente asignado')
        else:
            print('No es necesario asignar un docente')
# -------------------------------------------- 
    def __verificarDocente(self):
        print('Verificando si existe docente asignado...')
        if self.__imparticion == 'Presencial':
            return True
        else:
            return False           
        
# --------------------------------------------  

    def __str__(self):
        print(self.__nombre, self.__nota, self.__profesion)






# --------------------------------------------        
c = Curso('Ciencia', 10, 'Developer')
print(' ')
print(c.getNombre())
print(c.getNota())
print(c.getProfesion())
print(c.getImparticion())
print(' ')
print('------------------------')
print(' ')
c.setNombre('Python')
c.setNota('10')
c.setProfesion('Docente')
c.setImparticion('Virtual')
print(' ')
print('------------------------')
print(' ')
c.mostrarDatos()
print(' ')
print('------------------------')
c.__str__()
print('------------------------')
