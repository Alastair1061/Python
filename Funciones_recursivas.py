def Fiboniacci(n):
  if n<0: print("Error")
  elif n==0 or n==1: return n
  else: return Fiboniacci(n-1) + Fiboniacci(n-2)

def Sumatoria(n):
  if n<0: print("Error")
  elif n==0: return 0
  else: return n + Sumatoria(n-1)

def SerieArmonica(n):
  if n<=0: print("Error")
  elif n==1: return 1
  else: return 1/n + SerieArmonica(n-1)
    
#Producto de dos numeros
def Producto(a, b):
  resultado=0
  if b<0:
    b*=-1
    a*=-1
  for x in range (b):
    resultado+=a    
  return resultado

def ProductoAB(a, b):
  if b<0:
    b*=-1
    a*=-1
  elif b==0 or a==0:
    return 0
  else:
    return a + ProductoAB(a, b-1)
  
#Potencia de un numero
def Potencia(a, b):
  if b<0: print("Error")
  elif b==0: return 1
  elif a==0 or a==1: return a
  else:
    resultado=1
    for x in range (b):
      resultado*=a
    return resultado

def PotenciaAB(a, b):
  if b<0: print('Error')
  elif b==0: return 1
  elif a==0 or a==1: return a
  else: return a * PotenciaAB(a, b-1)
  
#Convertir un numero decimal a binario
def Decimal_a_binario(n):
  i=0
  resultado=0
  while n!=0:
    resultado += (10**i) * (n%2)
    n//=2
    i+=1
  return resultado

def DecimalBinario(n, i=0):
  if n<0: print('Error')
  elif n==0: return 0
  else: return (10**i) * (n%2) + DecimalBinario(n//2, i+1)
                      
def CuantosDigitos(n):
  if n<0: n*=-1
  elif n//10 != 0: return 1 + CuantosDigitos(n//10)
  else: return 1

def InvertirNumero(n):
  digitos = CuantosDigitos(n)
  if n//10 != 0: return (n%10) * (10**digitos) + InvertirNumero(n//10)
  else: return 0

def MaximoComunDivisor(a, b):
  if b%a == 0: return a
  else: return MaximoComunDivisor(b%a, a)

def MinimoComunMultiplo(a, b):
  return abs(a*b)/MaximoComunDivisor(a,b)
  
#Dada una secuencia de caracteres, obtener dicha secuencia invertida.


#Implementar una función para calcular el logaritmo entero de número n en una base b.
  

#Desarrollar un algoritmo que permita realizar la suma de los dígitos de un número entero, no se puede convertir el número a cadena.