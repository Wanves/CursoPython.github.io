edad = [12,2,35,23,41,25,78,9,10,15,16,13,55,45,36]
print(' ')
edadMAyores = list(filter(lambda edades: edades >=18, edad ))
for edades in edadMAyores:
    print(edades,end=' ')
print('==> Mayores')
    

print('================== ') 
edadMenores = list(filter(lambda edades: edades <=18, edad ))
for edades in edadMenores:
    print(edades,end=' ')
print('==> Menores')    
print(' ')


print('================== ') 
print(' ')
nombres = ['Juan', 'Zoe', 'Juliana', 'Flor', 'Julieta', 'Ramiro', 'Gustavo','Artemisa']

nombresMayores = list(filter(lambda nom:nom > 'J', nombres))
for nom in nombresMayores:
    print(nom,end=' ')
print('==> Mayores')

print('================== ') 
print(' ')

nombresMenores = list(filter(lambda nom:nom < 'J', nombres))
for nom in nombresMenores:
    print(nom,end=' ')
print('==> Menores')    
print(' ')







