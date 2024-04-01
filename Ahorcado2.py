import palabras
import ahorcado_diagramas
import random
import os

palabras_ = palabras.diccionario_palabras
diagramas = ahorcado_diagramas.diagramas_ahorcado

def obtenerCategoria():

  #Se muestran las categorias
  print("\nElige una de las siguientes categorias: ")
  for i, x in enumerate(palabras_, start=1):
    print(f"{i}) {x}")
  print(f"{i+1}) Aleatorio")

  #Bucle para asegurar que se ingresa una opcion valida
  while True: 
    eleccion = int(input("\n")) 
    if 0 < eleccion <= len(palabras_) + 1: 
      break

  #Si elige aleatorio, se elige una categoria aleatoria
  if eleccion == len(palabras_) + 1:  
    eleccion = random.randint(1, len(palabras_))

  llaves = list(palabras_.keys())
  return llaves[eleccion-1]

def letra_acentuada(letra):
    acentos={"a":"á", "e":"é", "i":"í", "o":"ó", "u":"ú", "A":"Á", "E":"É", "I":"Í", "O":"Ó", "U":"Ú"}
    if letra.lower() in "aeiou":
        return acentos[letra]
    else:
        return letra

def ejecucion():
    categoria = obtenerCategoria()
    palabra_secreta = random.choice(palabras_[categoria])
    letras_adivinadas = []
    intentos = []
    error = 0
    os.system("clear")
    while True:

        #Formar la cadena de _ y letras adivinadas
        cadena = ""
        for letra in palabra_secreta:
            if letra in letras_adivinadas or letra == " ": 
                cadena += letra + " "
            else: 
                cadena += "_ "

        #Pintar tablero
        print(diagramas[error],"\n",cadena,"\n")

        #Verificar ganador o perdedor
        if "_" not in cadena:
            print("Felcicidades ganaste")
            break
        if error == len(diagramas)-1:
            print("Perdiste, la palabra secreta es:", palabra_secreta)
            break

        #Solicitar letra y verificar si está o no en la ps
        letra = input("Ingresa una letra: ")
        letras = [letra.lower(), letra.upper(), letra_acentuada(letra.lower()), letra_acentuada(letra.upper())]
        for letra in letras:
            if letra in letras_adivinadas: 
                break
            elif letra in palabra_secreta:
                letras_adivinadas.append(letra)
                break
        else:
            if letra not in intentos:
                error += 1
            intentos.append(letra)
        os.system("clear")
            
ejecucion()