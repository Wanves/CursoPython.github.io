# edad = int(input('Ingresa tu edad-> '))
# if edad >= 18:
#     print('Eres mayor de edad')
# elif edad <= 0 :
#     print('edad incorrecta')
#     while  edad <= 0 :
#         edad = int(input('Ingresa tu edad-> '))
#         if edad >= 18:
#             print('Eres mayor de edad')
#         else:
#             print('Eres menor')
# else:
#     print('Eres menor')
    
edad = int(input('Ingresa tu edad-> '))
if edad <= 0 :
    print('edad incorrecta')
    while  edad <= 0 :
        edad = int(input('Ingresa tu edad-> '))
        if edad >= 18:
            print('Eres mayor de edad')
        else:
            print('Eres menor')
else:
    print('Eres menor de edad')