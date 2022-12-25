def leerArchivo():    
    file = open('data1.txt' , 'r')
    print()
    lineas = file.readlines()
    print(lineas)


def abrirArchivo():
    with open('data2.txt' , 'r') as file:
        lineas = file.readlines()
        print(lineas)
        for i in lineas:
            print(i.replace('\n', ' '))  

def openArchivo():
    with open('data2.txt' , 'r') as file:
        contenido = file.read()
        lineas = contenido.split('\n ')
        print(lineas)
        

def opArchivo():
    with open('data2.txt' , 'r') as file:
        contenido = file.read()
        lineas = contenido.split('\n ')
        pos = file.tell()
        print(pos)
        print(f'El archivo tiene {pos} caracteres de longitud')
  
def opeArchivo():
    with open('data2.txt' , 'r') as file:
        file.seek(10)  
        pos = file.tell()
        print(pos)
        contenido = file.read()
        lineas = contenido.split('\n ')
        print(lineas)
  
        
# leerArchivo()
# abrirArchivo()
# openArchivo()
# opArchivo()
# opeArchivo()










