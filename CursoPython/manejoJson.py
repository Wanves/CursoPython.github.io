import json

# jsonStr = '{"nombre":"Juan","edad":28,"pais":"Argentina"}'
# print(jsonStr)
# print(type(jsonStr))



# pythonDict = json.loads(jsonStr)
# print(pythonDict)
# print(type(pythonDict))
# print(pythonDict['edad'])
# print(pythonDict['pais'])

# data = {
#     'persona ': 'Juan',
#     'nombre ': 'xxxx',
#     'edad ': 'xxxx',
# }

# jsonData = json.dumps(data)
# print(jsonData)
# print(type(jsonData))

# equivalencias = ['Python - Json',
# 'dict - Object',
# 'list - Array',
# 'tuple - Array',
# 'str - String',
# 'int - Number',
# 'float - Number',
# 'True - true',
# 'False - false',
# 'None - null']


# print(equivalencias)

# data = {
#     'persona ': 'Class',
#     'nombre ': 'Juan',
#     'edad ': '40',
#     'cursos' : ['Python', 'Json', 'Javascript', 'Node.js']
# }
# jsonData = json.dumps(data,indent=4,separators=(',',':'),sort_keys=True)
# print(jsonData)


# jsonData = json.JSONEncoder().encode({'lenguajes':['Python','javascript']})
# print(jsonData)
# print(type(jsonData))

# jsonDict = json.JSONDecoder().decode(jsonData)
# print(jsonDict)
# print(type(jsonDict))

class Curso:
    def __init__(self,codigo,nombre,creditos):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__creditos = creditos
    def getCodigo(self):
        return self.__codigo
    def getNombre(self):
        return self.__nombre
    def getCreditos(self):
        return self.__creditos

curso = Curso('9841', 'Lenguaje',4)
print(curso)

jsonObjetData = json.dumps(curso.__dict__)
print(jsonObjetData)
print(type(jsonObjetData))

pythonDict = json.loads(jsonObjetData)
print(pythonDict)
print(type(pythonDict))






