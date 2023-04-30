
# def verificar_rango():
#     num = int(input("Ingresa un número: "))
#     if num >= 10 and num <= 100:
#         print(f"El número {num} se encuentra dentro del rango de 10 a 100")
#     elif num < 10 or num > 100:
#         print(f"El número {num} se encuentra fuera del rango de 10 a 100")
#         return True
# print(verificar_rango())

# ----------------------------------------------------

# import math

# radio = float(input("Ingresa el radio del cilindro: "))
# altura = float(input("Ingresa la altura del cilindro: "))
# pi = math.pi

# volumen = pi*(radio**2)*altura

# print(f"El volumen del cilindro es: {volumen:.2f} cm³")

# cond = volumen >= 300
# print(f"Se puede llenar el cilindro: {cond} ")

# ------------------------------------------------

# num1 = int(input("Ingrese el primer número: "))
# num2 = int(input("Ingresa segundo número: "))

# ult2 = num1 % 100

# cond1 = ult2 % num2 == 0
# cond2 = pow(2,num2) < ult2 
# respuesta = cond1 and cond2

# print(f'Cumple las dos condiciones?: {respuesta}')

# --------------------------------------------------

# x = int(input("Ingrese el valor de x: "))

# y = 4 * pow(2,x) + (3/2) * x - 5

# print(y)

# ----------------------------------------------------

# import math 

# a = float(input("Ingresa el valor del cateto a: "))
# b = float(input("Ingresa el valor del cateto b: "))

# c = ((a**2)+(b**2))**(1/2)

# print(f' {c:.3f} ')

# ------------------------------------------------------

# web = input("Ingrese URL Empresarial:")
# nom1 = input("Ingrese el primer nombre:")
# nom2 = input("Ingrese el segundo nombre:")
# apel1 = input("Ingrese el primer apellido:")
# year = input("Ingrese año de nacimento:")

# letra1 = nom1[0]
# letra2 = nom2[0]
# letra3 = apel1[:]
# ultNum = year[2:]
# nomEmpre = web[4:-4]

# correo = letra1+letra2+letra3+ultNum+'@'+nomEmpre+'.com'
# print(f'Su correo empresarial es: {correo}')

# ---------------------------------------------------

# tweet = "El día de ayer hubo ayudantías con #Joel de FP y #Kevin de CUV ya se divirtieron los pollos, ahora le toca a los gallos con #Axell "

# pos1 = tweet.index("#")
# subTweet = tweet[pos1+1:]
# posEsp1 = subTweet.index(" ")
# ayud1 = subTweet[:posEsp1]
# print(ayud1)

# pos2 = tweet.index("#",pos1+1)
# posEsp2 = tweet.index(" ",pos2)
# ayud2 = tweet[pos2+1:posEsp2]
# print(ayud2)

# tweetInv = tweet[::-1]
# posUlt = tweetInv.index("#")
# subTweetUlt = tweetInv[:posUlt]
# subTweetUltInv = subTweetUlt[::-1]
# posEspUlt = subTweetUltInv.index(" ")
# ayuUlt = subTweetUltInv[:posEspUlt]
# print(ayuUlt)

# ---------------------------------------------------


# frase = "Hacemos de algo #😃 simple algo extraordianario"
# busqueda1 = frase.index("#")
# frase1 = frase[busqueda1 + 1 :]
# fraseEspacio = frase1.index(" ")
# busquedaFinal = frase1[:fraseEspacio]
# print(busquedaFinal)

# frase2 = "Nunca pares de 😃 aprender "
# busqueda = frase2.index("😃")
# frase3 = frase2[busqueda + 2 :]
# fraseEspacio = frase3.index(" ")
# busquedaFinal = frase3[:fraseEspacio]
# print(busquedaFinal)

# def busqueda():
#     for i in frase2:
#         if i == "a":
#             print(frase2.index("a"))
#             print(f"Letra encontrada: {i}")
            
# busqueda()


# busqueda = lambda a,b : a in b

# print(busqueda("pares","Nunca pares de aprender"))

# if "Casa" != "Casa": print("Distinto") 
# else: print("Igual")

# list = ["a", 100,"Genial",[1,2,3,4,5]]
# print(list[3][2])

# -----------------------------------------

# list = [101,203,105,100,53]
# print(" ")
# print(list)
# list_ordenada = sorted(list, key = lambda n : n % 5)
# print(" ")
# print(list_ordenada)


# list_ordenada = sorted(list, key = lambda n : n % 5, reverse=True)
# print(" ")
# print(list_ordenada)

# ------------------------------------------------

# frase = "Python es tremendo"
# print(frase)
# print(" ")

# vocales_min = list(filter(lambda c: c in "aeiou" , frase ))
# print(vocales_min)

# -------------------------------------------------------


# frase = "Hacemos De Algo Simple Algo Extraordinario"
# print(frase)
# print(" ")

# vocales_may = list(filter(lambda c: c in "AEIOU" , frase ))

# print(vocales_may)

# -------------------------------------------------------
# from string import ascii_lowercase

# frase = "Hacemos De Algo Simple Algo Extraordinario"
# print(frase)
# print(" ")
# letras = set(ascii_lowercase)- set("aeiou")
# consonantes_min = list(filter(lambda c: c in letras , frase ))

# print(consonantes_min)

# -------------------------------------------------------

# frase = "Lo primero es aprender , después empieza el futuro 2023"
# print(frase)
# numeros = list(map(lambda d: int(d), list(filter(lambda c: c in '0123456789', frase))))
# print(numeros)

# -------------------------------------------------------      

# numeros = [150,250,183,50,10,330,25,67]

# menores_100 = list(filter(lambda n : n < 100, numeros))

# print(menores_100)

# resultado = list(map(lambda n:n +10,menores_100))

# print(resultado)



# ------------------------------------------------------- 


# num = [-150,50,80,-1000,-20,2,3]
# result = list(filter(lambda n:n > 100 ,map(lambda n:-n, num)))

# print(result)

# -------------------------------------------------------

# nombres = ['Juan','Zoe','Silvana','Sam']
# numero = [777,666,555,444]

# resultado = dict(zip(nombres,numero))
# print(resultado)




# nombres = ['Juan','Zoe','Silvana','Sam']
# numero = [777,666,555,444]

# resultado = list(zip(nombres,numero))
# resultado = sorted(resultado, reverse=True)
# print(resultado)

# ---------------------------------------------

# a = 5
# b = 40
# suma = lambda a , b : a + b
# resta = lambda a , b : a - b
# multiplica = lambda a , b : a * b
# divide = lambda a , b : a / b
# print(suma(a,b))
# print(resta(a,b))
# print(multiplica(a,b))
# print(divide(a,b))

# --------------------------------------------
# import random
# numeros = [10,500,800,5,13,87,456]
# print(numeros)
# numeros.sort(key=lambda n: 100/n)

# print(numeros)

# --------------------------------------------

# lista = ['Python','JavaScript','C++','Go','Php','Java']
# print(" ")
# print(lista)
# print(" ")

# ordered_list = sorted(lista, key=lambda c: c[1])
# print(" ")
# print(ordered_list)
# print(" ")

# ----------------------------------------------

# datos = [(777, 'Dev'), (666,'Gamer'), (555,'students'), (444,'teacher')]

# datos_ordenados = sorted(datos, key=lambda c: c[1])

# print(" ")
# print(datos_ordenados)
# print(" ")

# --------------------------------------------------


# datos = [(777, 'Dev'), (666,'Gamer'), (555,'students'), (444,'teacher')]

# datos_ordenados = sorted(datos, key=lambda c: c[1][-1])

# print(" ")
# print(datos_ordenados)
# print(" ")

# ----------------------------------------------------------

# nombres = ['Juan','Zoe','Pedro','Luisa','Gustavo','Noelia','Delsy']

# nombres1 = list(map(lambda n: f'{n} Lo primero es aprender, después comienza el futuro.', nombres ))
# nombres[0]='Neo'
# nombres[3]='Juan'
# print(nombres)
# nombres1 = list(map(lambda n: f'{n} Lo primero es aprender, después comienza el futuro.', nombres ))
# print('')
# print(f'{nombres1[0]}\n{nombres1[1]}\n{nombres1[2]}\n{nombres1[3]}\n{nombres1[4]}\n{nombres1[5]}\n{nombres1[6]}')
# print('')

# ------------------------------------------------------

# nombres = ['Juan','Zoe','Pedro','Luisa','Gustavo','Noelia','Delsy']

# nombres2 = list(map(lambda n: len(n), nombres))
# nombres3 = list(map(len,nombres))
# print('')
# print(nombres2)
# print('')
# print('')
# print(nombres3)
# print('')

# longitud = []
# for i in nombres:
#     mostrar_longitud = len(i)
#     longitud.append(mostrar_longitud)
# print(longitud)

# ----------------------------------------------------------

# list1 = [1 ,2 ,3 ,4 ,5 ,6 , 7 , 8, 9]
# list2 = [10,11,12,13,14,15, 16, 17, 18]

# lista3 = list(map(lambda a , b : a + b, list1,list2))
# print(" ")
# print(lista3)
# print(" ")

# ----------------------------------------------------

# list1 = [1 ,2 ,3 ,4 ,5 ,6 , 7 , 8, 9]
# list2 = [10,11,12,13,14,15, 16, 17, 18]

# lista3 = list(map(lambda a , b : a * b, list1,list2))
# print(" ")
# print(lista3)
# print(" ")

# -------------------------------------------------

# nombres = ['Juan','Zoe','Pedro','Luisa','Gustavo','Noelia','Delsy']

# cantidad = list(map(lambda c:c.count('o'), nombres))
# print(' ')
# print(cantidad)
# print(' ')

# -----------------------------------------------------

# nombres = ['Juan','Zoe','Pedro','Luisa','Gustavo','Noelia','Julia','Delsy','Jenifer']

# cantidad = list(map(lambda c : c.upper().count('J') , nombres))
# print(' ')
# print(cantidad)
# print(' ')

# ------------------------------------------------------

# numeros = [10,-100,-50,5,-100,-5,200,-200]

# resultado = list(map(lambda n : abs(n) , numeros))
# print('')
# print(resultado)
# print('')
# suma = sum(resultado)
# print(suma)

# ----------------------------------------------------------

# class Cola:
#     def __init__(self):
#         self.datos = []
        
#     def cantidad(self):
#         return len(self.datos)
    
#     def insertar(self,dato):
#         self.datos.insert(0,dato)
        
#     def quitar(self):
#         for i in range(len(self.datos)-1,-1,-1):
#             if self.datos[i]==777:
#                 self.datos.pop(i)
#             else:
#                 print(f'No existen datos en el sistema.')
    
#     def full_quitar(self):
#         return self.datos.clear()     
        
#     def mostrar_dato(self):
#         print(f'Datos: {self.datos}')
        
#     def primer_dato(self):
#         if self.cantidad():
#             return self.datos[0]
#     def ultimo_dato(self):
#         if self.cantidad():
#             return self.datos[-1]
    
        
                
        
# c = Cola()
# c.insertar(777)
# c.insertar(666)
# c.insertar(555)
# c.insertar(444)
# c.insertar(333)
# c.insertar(222)
# print(c.primer_dato())
# print(c.ultimo_dato())
# c.mostrar_dato()
# print(c.cantidad())
# c.quitar()
# c.mostrar_dato()
# print(c.cantidad())
# c.full_quitar()
# c.mostrar_dato()
# c.quitar()

# ---------------------------------

# def unir(palabras, separador=''):
#     resultado = separador.join(palabras)
    
#     return resultado

# lista = ['Python','JavaScript','C++','Go','Php','Java']
# print(" ")
# print(unir(lista,' | '))
# print(" ")
# print(" ")
# print(unir(lista,' , '))
# print(" ")
# print(" ")
# print(unir(lista,' : '))
# print(" ")

# ------------------------------------------------

# calculadora
# def run():
#     try:
#         def calculadora():
#             num1 = float(input('Ingresa el primer número: '))
#             op = input('Ingresa un operador: ')
#             num2 = float(input('Ingresa el segundo número: '))



#             if op == '+':
#                 resultado = num1 + num2
#                 print(f'El resultado es: {resultado}')
#             elif op == '-':
#                 resultado = num1 - num2
#                 print(f'El resultado es: {resultado}')
#             elif op == '*':
#                 resultado = num1 * num2
#                 print(f'El resultado es: {resultado}')
#             elif op == '/':
#                 resultado = num1 / num2
#                 print(f'El resultado es: {resultado}')
#             elif op == '**':
#                 resultado = num1 ** num2
#                 print(f'El resultado es: {resultado}')
#             else:
#                 print('Estas ingresando un valor no requerido.')
    
#     except:
#         print('Estas ingresando un valor no requerido.')
        
#     calculadora()
        
# if __name__ == '__main__':
#     run()
    
# -----------------------------------------------

# adivina el número

# import random 
# def run():
#     try:
       
#             oportunidades = 0
#             while oportunidades < 3:
                
#                 num = random.randint(1,10)
#                 print("")
#                 valor_usuario = int(input("Ingresa el número a adivinar: "))
#                 print("")
#                 oportunidades += 1
#                 if valor_usuario == num:
#                     print(f"Genial Adivinaste!!!, el número lanzado por pc es: {num}, el número lanzado por ti es: {valor_usuario}")
#                     print("")
#                 else:
#                     print(f"No has adivinado. El valor lanzado por pc es: {num}, el número ingresado por ti es: {valor_usuario}")
#                     print("")
#                 print(f'Oportunidad: {oportunidades}')
#             else:
#                 print("Juego terminado")
            
#     except:
#         print('Estas ingresando un valor no requerido.')
        
    
        
# if __name__ == '__main__':
#     run()

# ---------------------------------------------------