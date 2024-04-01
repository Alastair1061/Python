import palabras 
import ahorcado_diagramas 
import random
import os

class ahorcado():
    
    def __init__(self):
        self.diccionario_palabras = palabras.diccionario_palabras
        self.diagramas_ahorcado = ahorcado_diagramas.diagramas_ahorcado
        self.letras_adivinadas = []
        self.intentos = []
        self.errores = 0
        self.palabra_secreta = self.obtenerPalabraSecreta()
        #self.palabra_secreta = "Canadá"
        self.palabra_usuario = self.formarPalabra()
        
    def obtenerPalabraSecreta(self):
        """
        Muestra las categorias y devuelve una palabra secreta según la categoria elegida
        """
        #Se muestran las categorias
        os.system("clear")
        print("\nElige una de las siguientes categorias: ")
        for i, x in enumerate(self.diccionario_palabras, start=1):
            print(f"{i}) {x}")
        print(f"{i+1}) Aleatorio")

        #Bucle para asegurar que se ingresa una opcion valida
        while True: 
            eleccion = int(input("\n")) 
            if 0 < eleccion <= len(self.diccionario_palabras) + 1: 
                break

        #Si elige aleatorio, se elige una categoria aleatoria
        if eleccion == len(self.diccionario_palabras) + 1:  
            eleccion = random.randint(1, len(self.diccionario_palabras))

        llaves = list(self.diccionario_palabras.keys())
        categoria = llaves[eleccion-1]
        return random.choice(self.diccionario_palabras[categoria])
    
    def letra_acentuada(self, letra):
        """
        Devuelve una letra acentuada en caso de ser vocal
        """
        acentos={"a":"á", "e":"é", "i":"í", "o":"ó", "u":"ú", 
                 "A":"Á", "E":"É", "I":"Í", "O":"Ó", "U":"Ú"}
        if letra.lower() in "aeiou":
            return acentos[letra]
        else:
            return letra
        
    def formarPalabra(self):
        """
        Forma la lista de _ y de letras adivinadas
        """
        cadena = ""
        for letra in self.palabra_secreta:
            if letra in self.letras_adivinadas or letra == " ": 
                cadena += letra + " "
            else: 
                cadena += "_ "
        self.palabra_usuario = cadena

    def mostrarTablero(self):
        """
        Muestra el tablero de juego
        """
        print(f"""
Haz intentado:{self.intentos}
{self.diagramas_ahorcado[self.errores]}
        {self.palabra_usuario}
              """)
    
    def verificarFin(self):
        """
        Devuelve verdadero si el jugador gana o pierte
        """
        if "_" not in self.palabra_usuario:
            print("Felcicidades ganaste")
            return True
        if self.errores == len(self.diagramas_ahorcado)-1:
            print("Perdiste, la palabra secreta es:", self.palabra_secreta)
            return True

    def verificarLetra(self,letra):
        """
        Devuelve verdadero si se adivino la letra
        """
        if letra in self.palabra_secreta:
            self.letras_adivinadas.append(letra)
            return True

    def solicitarLetra(self):
        """
        Solicita una letra y verifica si ya la intento, la adivino o es incorrecta.
        Esto lo hace para minusculas, mayusculas y letras acentuadas solo ingresando una de estas opciones
        """
        letra = input("Ingresa una letra: ").lower()
        letras = [letra, letra.upper(), self.letra_acentuada(letra.lower()), self.letra_acentuada(letra.upper())]

        if letra not in self.intentos:
            self.intentos.append(letra)
            aciertos = list(filter(self.verificarLetra, letras))
            if len(aciertos) == 0:
                self.errores += 1

    def ejecucion(self):
        os.system("clear")
        while True:   
            self.formarPalabra()
            self.mostrarTablero()
            if self.verificarFin(): break
            self.solicitarLetra()
            os.system("clear")

ahorcado().ejecucion()