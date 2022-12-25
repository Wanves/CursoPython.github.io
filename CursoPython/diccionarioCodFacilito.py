dic = {'a':55, 'b':100}
dic2 = {'c':2, 'd':3}


dic['x']= dic2
print(dic)
dic['x']
print(dic['x'])
dic['b'] = 5555
print(dic)
dic['z'] = 'Genial'
print(dic)
dicValor = dic.get('p',False)
print(dicValor)
dicValor = dic.get('a',False)
print(dicValor)
del dic['b']
print(dic)

llaves = dic.keys()
print(llaves)
print(list(llaves))

valores = dic.values()
print(valores)
print(list(valores))
print(tuple(valores))

dic3 = {'j':'Colores','o':'lugares','num':777}
dic['p'] = dic3
print(dic)
dic.update(dic)
print(dic)