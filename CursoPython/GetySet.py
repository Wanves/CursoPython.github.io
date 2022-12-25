# class Cuenta:
#     def __init__(self,pro,sal,mon):
#         self.__propietario = pro
#         self.__saldo = sal
#         self.__moneda = mon
#     def getPropietario(self):
#         return self.__propietario
#     def getSaldo(self):
#         return self.__saldo
#     def getMoneda(self):
#         return self.__moneda
    
#     def setMoneda(self,nuevaMoneda):
#         self.__moneda = nuevaMoneda
        
        
        
        
# cuenta = Cuenta('Juan','$5.000.000','dolares')
# print(cuenta.getPropietario(), cuenta.getSaldo(), cuenta.getMoneda())
# print(cuenta.getMoneda())
# cuenta.setMoneda('Euros')
# print(cuenta.getMoneda())
# cuenta.setMoneda('Monedas Oro')
# print(cuenta.getMoneda())


# class Cuenta:
#     def __init__(self, prop, sal, mon  ):
#         self.__propietario = prop
#         self.__saldo = sal
#         self.__moneda = mon
#  # -----------------------------------------------       
#     def Propietario(self):
#         print(c.__propietario)
#     def Saldo(self):
#         print(c.__saldo)
#     def Moneda(self):
#         print(c.__moneda)    
# # -----------------------------------------------    
#     def setPropietario(self,nuevoPropietario):
#         self.__propietario = nuevoPropietario
#         print(nuevoPropietario)
#     def setSaldo(self,nuevoSaldo):
#         self.__saldo = nuevoSaldo
#         print(nuevoSaldo)
#     def setMoneda(self,nuevoMoneda):
#         self.__moneda = nuevoMoneda
#         print(nuevoMoneda)
        
        
        
# c = Cuenta('Juan','$20.000.000','dolares')
# c.Propietario()
# c.Saldo()
# c.Moneda()
# print('-----------------------')
# c.setPropietario('Tom')
# c.setSaldo('$1000.000.000')
# c.setMoneda('Euros')

# ------------------------------------------ 

class Cuenta:
  def __init__(self, pro, sal, mon):
    self.__propietario = pro
    self.__saldo = sal
    self.__moneda = mon
  
  def getPropietario(self):
    return self.__propietario
  def getSaldo(self):
    return self.__saldo
  def getMoneda(self):
    return self.__moneda 
  
  def setPropietario(self, nuevoPropietario):
    self.__propietario = nuevoPropietario
  def setSaldo(self, nuevoSaldo):
    self.__saldo = nuevoSaldo
  
  def setMoneda(self, nuevaMoneda):
    self.__moneda = nuevaMoneda
    
c = Cuenta('Juan','$20.000.000','dólares')

print(' ')
print(c.getPropietario())
print(c.getSaldo())
print(c.getMoneda())
print(' ')
print('---------------------')
print(' ')
c.setPropietario('Juan Wanvestrant')
c.setSaldo('$50.000.000')
c.setMoneda('Euros')
print(c.getPropietario())
print(c.getSaldo())
print(c.getMoneda())
    



    



