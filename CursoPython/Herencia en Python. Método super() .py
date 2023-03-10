# class Persona:
#     def __init__(self, apePat, apeMat, nom):
#         self.apellidoPaterno = apePat
#         self.apellidoMaterno = apeMat
#         self.nombres = nom
        
#     def mostrarNombreCompleto(self):
#         return f'{self.apellidoPaterno}{self.apellidoMaterno}{self.nombres}'
    
# p = Persona('Gauna ',' Wanvestrant ',' Juan')

# print(p.mostrarNombreCompleto('Matrix','anderson', 'Neo'))

# class Estudiantes(Persona):
#     pass

# es = Estudiantes('Kakaroto','lyon','Goku')
# print(es.apellidoPaterno())
# print(es.apellidomaterno())

import numpy as np

class Sector:
  def __init__(self, costo, lugares):
    self.__costo = costo
    self.__registros = np.zeros(lugares, Registro)
    self.__ocupados = 0
        
    print(np.transpose(self.__registros))
    print(np.transpose(lugares))
  def __repr__(self):
    cadenaString = f"lugares:{self.__ocupados}, {self.__registros}"
    return cadenaString

  def ingresarRegistro(self, patente, horaEntrada):
    self.__registros[self.__ocupados] = Registro(patente, horaEntrada)
    self.__ocupados += 1
  

    
#-------------------------------------------------------------    
  def datoSectorEstudiantes(p,patente,horaEntrada):
    if patente>= len(p):
        raise Exception('No tengo lugar para esa posición')
    p[patente]= horaEntrada 
    
         
  s = np.zeros(50,int)
  datoSectorEstudiantes(s,0,111222)
  datoSectorEstudiantes(s,12,333444)
  datoSectorEstudiantes(s,25,555666)
  print(s)  
  
  if 111222 in s:
    print('Esta dentro')
  else:
    print('No esta dentro')
# #-------------------------------------------------------------  
  def datosSectorProfesores(p,patente,horaEntrada):
    if patente>= len(p):
        raise Exception('No tengo lugar para esa posición')
    p[patente]= horaEntrada
  
    
  s = np.zeros(50,int)
  datosSectorProfesores(s,30,777888)
  datosSectorProfesores(s,19,999101)
  print(s)
  if 333999 in s:
    print('Esta dentro')
  else:
    print('No esta dentro')
# #-------------------------------------------------------------  
  def datoSectorGeneral(p,patente,horaEntrada):
    if patente>= len(p):
        raise Exception('No tengo lugar para esa posición')
    p[patente]= horaEntrada 
 
  s = np.zeros(100,int)
  datoSectorGeneral(s,0,111222)
  datoSectorGeneral(s,18,333444)
  datoSectorGeneral(s,45,555666)
  print(s)

#-------------------------------------------------------------      
    
  def sacarRegistro(self, patente, horaSalida):
    i = 0
    for r in self.__registros:
      if r != 0 and r.getPatente()== patente:
        self.__registros[i] = 0
        self.__ocupados -= 1
        Registro(self.__registros, i)
        return r.cuantoEstuvo(horaSalida) * self.__costo
      i+=1  
         

class Registro:
  
  def __init__(self, patente, horaEntrada):
    self.__patente = patente
    self.__horaEntrada = horaEntrada
  
  def __repr__(self) -> str:
    cadenaString = f"({self.__patente} - {self.__horaEntrada})"
    return cadenaString
  
  def cuantoEstuvo(self, horaSalida):
    return horaSalida - self.__horaEntrada
  
  def getPatente(self):
    return self.__patente
# -----------------------------------------------------
#En esta parte dejo una linea sin comentar y una comentada para que al imprimir se muestre el dato dentro del sector
# y se pueda apreciar el entendimeinto del proceso.  
estudiantes = Sector(5, 50)
estudiantes.ingresarRegistro("aaa111",8)
# estudiantes.sacarRegistro("aaa111",9)
estudiantes.ingresarRegistro("aaa222", 9)              
# estudiantes.sacarRegistro("aaa222",10)
estudiantes.ingresarRegistro("bbb222", 10)
# estudiantes.sacarRegistro("bbb222",11)
print(estudiantes)

# -----------------------------------------------------
#En esta parte dejo una linea sin comentar y una comentada para que al imprimir se muestre el dato dentro del sector
# y se pueda apreciar el entendimeinto del proceso.  
profesores = Sector(10,50)
profesores.ingresarRegistro("NEO777", 14)
# profesores.sacarRegistro("NEO777", 15)
profesores.ingresarRegistro("TRI666", 10)
# profesores.sacarRegistro("TRI666", 11)
print(profesores)


# -----------------------------------------------------
#En esta parte dejo una linea sin comentar y una comentada para que al imprimir se muestre el dato dentro del sector
# y se pueda apreciar el entendimeinto del proceso. 
general = Sector(20, 100)                       
# general.ingresarRegistro("gok777", 16)
# general.sacarRegistro("gok777", 17)
general.ingresarRegistro("jir666", 18)
general.sacarRegistro("jir666", 19)
# general.ingresarRegistro("fre777", 21)
# general.sacarRegistro("fre777", 21)
print(general)


# -----------------------------------------------------


class Estacionamiento:

  def __init__(self):
    self.__es = Sector(5, 50)
    self.__pr = Sector(10, 50)
    self.__gr = Sector(20, 100)
    self.__reca = 0
    
    
  
  def ingresarAuto(self, sector, patente, horaEntrada):
    if (sector == "estudiantes"):
      self.__es.ingresarRegistro(patente, horaEntrada)
    elif (sector == 'profesores'):
      self.__pr.ingresarRegistro(patente, horaEntrada)
    elif (sector == 'general'):
      self.__gr.ingresarRegistro(patente, horaEntrada)
    else:
      raise Exception("No conozco ese sector")
    
  
    

  def sacarAuto(self, sector, patente, horaSalida):
    if (sector == 'estudiantes'):
      self.__reca += self.__es.sacarRegistro(patente, horaSalida)
    elif (sector == 'profesores'):
      self.__reca += self.__pr.sacarRegistro(patente, horaSalida)
    elif (sector == 'general'):
      self.__reca += self.__gr.sacarRegistro(patente, horaSalida)
    else:
      raise Exception("No conozco ese sector")
    
    if (5,50 == 'profesores'):
      print('Esta dentro')
    else:
      print('No esta dentro ya se retiró')
      
    # if (20,100 == "jir666", 18):
    #   print('Esta dentro')
    # else:
    #   print('No esta dentro ya se retiró')  
   
    
  def calcularTiempo(self):
    if not self.estaDentro:
      return self.__horaSalida - self.__horaEntrada
    raise Exception('No ha egresado')  
  
  def estaDentro(self):  
    return self.__horaSalida is None
    
  
  def __repr__(self):
    result = f'{self.__patente}: {self.__horaEntrada} - {self.__horaSalida} ' 
    if self.estaDentro ():
      return result
      return result + f' - {self.__horaSalida} ' 
    

  def cuantoRecaudaste(self):
    return self.__reca

  def __repr__(self):
    return f"sector estudiantes: {self.__es}\nsector profes: {self.__pr}\nsector general: {self.__gr}n"
  
  def get__reca(self):
    return self.__reca
  


esta = Estacionamiento()
# -----------------------------------------------------
esta.ingresarAuto("estudiantes","aaa111", 8)
esta.ingresarAuto("estudiantes", "aaa222", 9)
esta.ingresarAuto("estudiantes", "bbb222", 10)
                                                  # Ingresa auto / Egresa auto sector estudiantes
esta.sacarAuto("estudiantes","bbb222", 11)
esta.sacarAuto("estudiantes","aaa222", 10)
est1=esta.sacarAuto("estudiantes","aaa111", 9)
# -----------------------------------------------------
esta.ingresarAuto("profesores", "NEO777", 14)
esta.ingresarAuto("profesores", "TRI666", 10)
                                                  # Ingresa auto / Egresa auto sector profesores
esta.sacarAuto("profesores", "NEO777", 15)
esta.sacarAuto("profesores", "TRI666", 11)
# -----------------------------------------------------
esta.ingresarAuto("general", "gok777", 16)
esta.ingresarAuto("general", "jir666", 18)
esta.ingresarAuto("general", "fre777", 20)
                                                  # Ingresa auto / Egresa auto sector general
esta.sacarAuto("general", "gok777", 17)
#esta.sacarAuto("general", "jir666", 19)
esta.sacarAuto("general", "fre777", 21)


# -----------------------------------------------------

# esta.ingresarAuto("padres", "vvv666", 10)
# esta.ingresarAuto("descarga", "jjj555", 10)
# esta.ingresarAuto("familaires", "iii888", 10)
# esta.ingresarAuto("camiones", "sam999", 10) #no conoce este sector Exception


# -----------------------------------------------------

print(esta)
esta.get__reca()
print(f'El monto recaudado es-> {esta.get__reca()}')