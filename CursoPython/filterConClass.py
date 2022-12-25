class Usuario:
    def __init__(self,nombre, registro):
        self.__nombre = nombre
        self.__registro = registro
    def getNombre(self):
        return self.__nombre
    def getRegistro(self):
        return self.__registro
    def __str__(self):
        return f'Nombre: {self.getNombre()} === Registro: {self.getRegistro()}'
    
usuario = [
    Usuario('Juan',777111),
    Usuario('Zoe',555000),
    Usuario('Juliana',333222),
    Usuario('Neo',444555),
    Usuario('Gokú',222888)
]

verUsuarios = list(filter(lambda user:user.getRegistro() > 0,usuario))
for user in verUsuarios:
    print(user)
print(' ')    
print('============')
print(' ')   
class Usuario:
    def __init__(self,nombre, registro):
        self.__nombre = nombre
        self.__registro = registro
    def getNombre(self):
        return self.__nombre
    def getRegistro(self):
        return self.__registro
    def __str__(self):
        return f'Nombre: {self.getNombre()} === Registro: {self.getRegistro()}'
    
usuario = [
    Usuario('Juan',777111),
    Usuario('Zoe',555000),
    Usuario('Juliana',333222),
    Usuario('Neo',444555),
    Usuario('Gokú',222888)
]

verUsuarios = list(filter(lambda user:user.getNombre() > 'N',usuario))
for user in verUsuarios:
    print(user)    