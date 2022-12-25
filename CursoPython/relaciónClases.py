# class Pais:
#   def __init__(self, nombre, presidente):
#     self.__nombre = nombre
#     self.__presidente = presidente

#   def getNombre(self):
#     return self.__nombre

#   def getPresidente(self):
#     return self.__presidente

#   def __str__(self):
#     return f'{self.__nombre} {self.__presidente}'


# class Ciudad:
#   def __init__(self,nombre, habitantes, pais):
#     self.__nombre = nombre
#     self.__habitantes = habitantes
#     self.__pais = pais

#   def __str__(self):
#     return f'Ciudad: {self.__nombre} \nHabitantes: {self.__habitantes} \nPaís: {self.__pais}  '




# p = Pais('Perú', 'Vizcarra') 
# print(' ')
# print(p)
# print(' ')
# c = Ciudad('Hurlingham',5000000, p)
# print(c)





# # --------------------------------------------------------------
class Pais:
  def __init__(self, nombre, presidente):
    self.__nombre = nombre
    self.__presidente = presidente

  def getNombre(self):
    return self.__nombre

  def getPresidente(self):
    return self.__presidente

  def __str__(self):
    return f'{self.__nombre} {self.__presidente}'
  def dato1(self):
    print(self.__str__())

class Ciudad:
  def __init__(self,nombre, habitantes, pais):
    self.__nombre = nombre
    self.__habitantes = habitantes
    self.__pais = pais

  def __str__(self):
    return f'Ciudad: {self.__nombre} \nHabitantes: {self.__habitantes} \nPaís: {self.__pais}  '
  
  
  def dato(self):
    print(self.__str__())



p = Pais('Perú', 'Vizcarra') 
print(' ')
p.dato1()
# print(p)
print(' ')
c = Ciudad('Hurlingham',5000000, p)
c.dato()
# print(c)


