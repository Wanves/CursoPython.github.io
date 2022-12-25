# class Region:
#     def __init__(self, pais, provincia, localidad):
#         self.__pais = pais
#         self.__provincia = provincia
#         self.__localidad = localidad
        
#     def getPais(self):
#         return self.__pais
#     def getProvincia(self):
#         return self.__provincia
#     def getLocalidad(self):
#         return self.__localidad
    
#     def __str__(self):
#         return f'País: {self.__pais}, \nProvincia: {self.__provincia}, \nLocalidad: {self.__localidad}'
    
# region = Region('Argentina','Buenos Aires','Hurlingham')
# print(region)


# # -------------------------------------------------------------

# class Persona:
#     def __init__(self, nombre, edad,region):
#         self.__nombre = nombre
#         self.__edad = edad
#         self.__region = region
        
#     def getNombre(self):
#         return self.__nombre
#     def getEdad(self):
#         return self.__edad
#     def getRegion(self):
#         return self.__region
    
#     def __str__(self):
#         return f'Nombre: {self.__nombre} \nEdad: {self.__edad}  \nRegión: {self.__region}'
    
# # -------------------------------------------------------------
    
#     def __repr__(self):
#         return f'Nombre:** {self.__nombre} \nEdad: {self.__edad}  \nRegión: {self.__region}'
        
# print(' ')    
# persona = Persona('Juan', '40', region)
# print(persona)

class Vehiculo:
    def __init__(self, modelo, año):
        self.__modelo = modelo
        self.__año = año
    # -----------------------------------------------------
    def getModelo(self):
        return self.__modelo

    def getAño(self):
        return self.__año
    #-----------------------------------------------------
    def mDatos(self):
        return f'Modelo: {self.__modelo} \nAño: {self.__año}'
    #-----------------------------------------------------
    def datos(self):
            print(self.mDatos())
v = Vehiculo('Fort Gt', 1966)
v.datos()
#---------------------------------------------------------
class Auto(Vehiculo):
    def __init__(self, modelo, año, serie):
        super().__init__(modelo,año)
        self.__serie = serie
    def getSerie(self):
        return self.__serie
    def mostrarDatos(self):
        return f'Modelo: {self.__modelo} \nAño: {self.__año} \nSerie: {self.__serie}'
    def datos1(self):
        super().datos()
        print(self.__serie)
print(' ')
print('---------------------')
print(' ')
a = Auto('Mustang',1966,'1966,1967,1968,1970')
a.datos1()
