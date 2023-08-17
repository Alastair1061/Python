import palabras
import ahorcado_diagramas
import random
random.seed(None)

ahorcado_diagramas = ahorcado_diagramas.ahorcado_diagramas #Este es una lista con los diagramas del ahorcado
palabras = palabras.palabras  #Este es un diccionario cuyas llaves son las categorias y los valores son las palabras que puedes elegir

def obtenerCategoria():

  #Se muestran las categorias
  print("\nElige una de las siguientes categorias: ")
  for i, x in enumerate(palabras, start=1):
    print(i, ")", x)
  print(i+1,") Aleatorio")

  #Bucle para asegurar que se ingresa una opcion valida
  while True: 
    eleccion = int(input("\n")) 
    if 0 < eleccion <= len(palabras) + 1: 
      break

  #Si elige aleatorio, se elige una categoria aleatoria
  if eleccion == len(palabras) + 1:  
    eleccion = random.randint(1, len(palabras))

  llaves = list(palabras.keys())
  return llaves[eleccion-1]

def Ejecucion():
  print("Bienvenido al juego del ahorcado")
  
  categoria = obtenerCategoria()
  palabra = random.choice(palabras[categoria])
  respuesta = ["_"] * len(palabra)
  errores = 0
  intentos = []
  letras = "abcdefghijklmnñopqrstuvwxyz"
  
  print("\nQue comience el juego")
  
  while True:

    #Pinta el tablero y la respuesta
    print(ahorcado_diagramas[errores])
    for letra in respuesta:
      print("   ", letra, end="")
    print("\n")
  
    #Bucle que se repite si se ingresa una letra repetida o si se ingresa algo que no sea una letra
    while True:
      letra = input("Ingresa una letra: ")
      if letra not in intentos and letra in letras:
        intentos.append(letra)
        break
      elif letra == palabra: #solo en el caso de que se ingrese la palabra correcta completa se ejecuta esto
        respuesta = palabra
        break
  
    #aqui se comprueba si acerto y se guarda la letra en la respuesta o se agrega un error
    if letra in palabra:
      for i, x in enumerate(palabra):
        if letra == x:
          respuesta[i] = letra
    elif letra != palabra:
      errores += 1
  
    #aqui se comprueba si ya se completo la palabra, si ingreso la palabra correcta o si ya perdio
    if "_" not in respuesta or letra == palabra: 
      print(ahorcado_diagramas[errores])
      for letra in palabra:
        print("   ", letra, end="")
      print("\n\nFelicidades, ganaste")
      break
    elif errores == len(ahorcado_diagramas) - 1:
      print(ahorcado_diagramas[errores] + "\n\nYa perdiste \nLa palabra correcta era: " + str(palabra))
      break

while True:
  Ejecucion()
  eleccion=input("\n\nQuieres jugar otra vez?(s/n)")
  if eleccion=='n':
    break