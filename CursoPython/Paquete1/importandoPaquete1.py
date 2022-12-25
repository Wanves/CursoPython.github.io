# from funcionesNumericas import *
# from funcionesCadenas import *
# operaciones()
# print(len('Hacemos de algo simple algo extraordinario'))


class Persona:
  def __init__(self, nombre , edad ):
    self.nombre = nombre
    self.edad = edad
    
  
  def despertar(self):
    print('Ha despertado temprano y esta estudiando')

  def prepara(self):
    print('Prepara su café para seguir estudiando')

estudiante = Persona('Goku',40)
estudiante.nombre
estudiante.edad
print(estudiante.nombre)
print(estudiante.edad)