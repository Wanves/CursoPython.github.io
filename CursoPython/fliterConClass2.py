class Cliente:
    def __init__(self,id,registro):
        self.__id = id
        self.__registro = registro
    def getId(self):
        return self.__id
    def getRegistro(self):
        return self.__registro
    
    def __str__(self):
        return f'ID: {self.getId()} Registro: {self.getRegistro()}'
    
cliente = [
    Cliente(1,777111),
    Cliente(2,777222),
    Cliente(3,777333),
    Cliente(4,777444),
    Cliente(5,777555),
    Cliente(6,777666),
    Cliente(7,777777),
    Cliente(8,777888),
    Cliente(9,777999),
    Cliente(10,777000),
]

datosClientes = list(filter(lambda client:client.getId() > 0 ,cliente))
for client in datosClientes:
    print(client)