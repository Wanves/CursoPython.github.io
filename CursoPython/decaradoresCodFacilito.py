# def decorador(func):
#     def nuevaFuncion():
#         print('Vamos a ejecutar la función')
#         func()
#         print('Se ejecutó la función')
#     return nuevaFuncion

# @decorador
# def saluda():
#     print('Genial')
    
# @decorador   
# def suma():
#     print(10+20)
# saluda()
# suma()

# def decorador(func):
#     def mensaje():
#         print('*Recuerda registrar bien tus datos*')
#         func()
#         print('*-------------------------------------*')
#     return mensaje
        

# @decorador
# def datos():
#     nombre = input('Ingrese su nombre ')
#     edad = int(input('Ingrese su edad '))
#     dato = f'Nombre: {nombre} Edad: {edad}'
#     print(dato)
# datos()

# def decorador(func):
#     def mensaje(*args, **kwargs):
#         print(' ')
#         print('Sus datos se encuentran protegidos-************')
#         print(' ')
#         func(*args, **kwargs)
#     return mensaje

# @decorador
# def registro():
#     nombre = input('Ingrese su nombre ')
#     edad = int(input('Ingrese su edad '))
#     telefono = int(input('Ingrese su teléfono '))
#     print(' ')
#     print(f'Nombre: {nombre} Edad: {edad} Tel: {telefono}')
#     print(' ')

# @decorador
# def suma(n,n1):
#     print(n+n1)


# suma(25,50)
# registro()

    
def decorador(func):  
    def mensaje(*args, **kwargs):
        print(' ')
        print('Sus datos se encuentran protegidos')
        print(' ')
        func(*args, **kwargs)
    return mensaje
    


@decorador
def datos():
    nombre = input('Ingrese su nombre ')
    edad = input('Ingrese su edad ')
    print(' ')
    print(f'Nombre: {nombre} Edad: {edad}')
    print(' ')
    
@decorador  
def datos2(telefono,direccion):
    print(f'Tel: {telefono} Dirección: {direccion}')
    print(' ')
 
@decorador
def suma(n,n1):
    print(n+n1)
    print(' ')
    
datos()
datos2(1169324968, 'Centenera984')
suma(25,50)