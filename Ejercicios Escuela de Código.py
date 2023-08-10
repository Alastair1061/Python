'''
Aqui se almacenan todos los ejercicios de Escuela de código de Python
voy a hacer un menu para ejecutar ejercicio por ejercicio.
'''

while True:
  print("""
Ingresa que ejercicio quieres ejecutar:
1) 4.1  
2) 4.2
3) 4.3
4) 4.4
5) 4.5
6) 6.1
7) 6.2
8) 6.3
9) 6.4
10) 8.1
11) 8.2
12) 8.3
13) 9.1
14) 9.2
15) 9.3
16) 9.4
0) Salir
""")
  ejercicio = int(input(""))

  if ejercicio == 1:
    
    print("4.1) Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) y posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo.\n")
    
    import random
    random.seed(None)

    #Inicializar la lista con  valores aleatorios entre 1 y 10
    lista1 = [random.randint(1, 10) for i in range(10)]

    #Mostrar en pantalla lo solicitado
    for x in lista1:
      print("Elemento:", x,"Cuadrado:", x**2,"Cubo:", x**3)

  elif ejercicio == 2:
  
    print("4.2) Crea una lista e inicializarla con 5 cadenas de caracteres leídas por teclado. Copialos elementos de la lista en otra lista pero en orden inverso, y muestra sus elementos por la pantalla.\n")  

    # Inicializar la lista y leer las 5 cadenas de caracteres por teclado
    lista2=[]
    for i in range(5):
      cadena=input("Ingresa una cadena de caracteres: ")
      lista2.append(cadena)

    # Copiar los elementos en otra lista en orden inverso utilizando slicing y mostrarlos en pantalla
    lista_inversa = lista2[::-1]
    print(lista_inversa)

  elif ejercicio == 3:
  
    print("4.3) Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10). A continuación debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor.\n")
    
    # Inicializar la lista y leer las 5 notas por teclado
    lista3=[]
    for i in range (5):
      
      # Bucle para asegurarse de que se ingrese una nota válida
      while True:
        nota=int(input("Ingresa la nota: "))
        if(0<=nota<=10): 
          lista3.append(nota)
          break
        else:
          print("Nota no valida, intenta de nuevo")

    #Mostrar en pantalla lo solicitado
    print("\nLas notas son:",lista3)
    print("La nota mas alta es: ", max(lista3))
    print("La nota menor es: ", min(lista3))
    print("El promedio de las notas es: ", sum(lista3)/len(lista3))

    '''
    4.4) Codifica un programa en python que nos permita guardar los nombres de los alumnos de una clase y las notas que han obtenido. 
    Cada alumno puede tener distinta cantidad de notas. 
    Guarda la información en un diccionario cuya claves serán los nombres de los alumnos y los valores serán listados con las notas de cada alumno.
    El programa pedirá el número de alumnos que vamos a introducir, pedirá su nombre e irá pidiendo sus notas hasta que introduzcamos un número negativo. Al final el programa nos mostrará la lista de alumnos y la nota media obtenida por cada uno de ellos. 
    Nota: si se introduce el nombre de un alumno que ya existe el programa nos dará un error.
    '''

    #Solicitar un numero positivo de alumnos
    while True:
      nAlumnos=int(input("Cuantos alumnos vamos a registrar: "))
      if(nAlumnos<=0): 
        print("Numero no valido\n")
      else: 
        break
        
    #Inicializar el diccionario/registro
    registro={}
    for x in range(nAlumnos):
      print("\nAlumno", x+1)
      
      nombreValido = False
      while not nombreValido: # Bucle para asegurarse de que se ingrese una nombre válido
        nombre=input("Ingresa su nombre: ")  
        
        if nombre not in registro:
          nombreValido = True
          notas=[]
          while True: #Solicitar e ingresar las notas hasta que se ingrese un numero negativo
            nota=int(input("Ingresa la nota: "))
            if sum(notas) == 0 and nota<0:
              print("Nota no valida, intenta de nuevo")
              continue
            elif nota>10:
              print("Nota no valida, intenta de nuevo")
              continue
            elif nota>=0:  
              notas.append(nota)
            else: 
              break    
          registro[nombre]=notas.copy()#Guardamos el nombre y sus notas en el registro 
        
        else:
          print("El alumno ya esta registrado, intenta de nuevo")
          
    for alumno in registro:
      print(alumno, "tiene un promedio de", sum(registro[alumno])/len(registro[alumno]))

    '''
    4.5) Crea una tupla con los meses del año, pide números al usuario, si el número está entre 1 y la longitud máxima de la tupla, muestra el contenido de esa posición sino muestra un mensaje de error. El programa termina cuando el usuario introduce un cero.
    '''

    meses=("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    while True:
      n=int(input("Ingresa un numero: "))
      if 1 <=n<= 12: print(meses[n-1])
      elif n==0: break
      else: print("Mensaje de error")

    '''
    6.1) Realizar un ejemplo de menú, donde podemos escoger las distintas opciones hasta que seleccionamos la opción de “Salir”.
    '''

    #Inicializar y mostrar el menu en forma de lista
    menu=("Sandia", "Melon", "Manzana", "Platano", "Uvas")
    print("El menú es:\n")
    for x in range(len(menu)):
      print(str(x+1) + ") " + menu[x])
    print("6) Salir")

    #Bucle para solicitar la opcion, verificarla y mostrarla o salir
    while (True):
      op=int(input("\nElige la opcion deseada: "))
      if(0<= op <=len(menu)): 
        print("Elegiste " + menu[op-1])
      elif(op == len(menu)+1): 
        break
      else: 
        print("Opcion no valida")
    print("\nAdios")
        
    '''
    6.2) Mostrar en pantalla los N primero número primos. Se pide por teclado la cantidad de números primos que queremos mostrar
    '''

    #Define una funcion que devuelve una lista con los n primeros números primos
    def obtener_numeros_primos(n):
      primos=[]
      x=2
      while(len(primos)<n):
        x_es_primo=True

        #En este bucle comparo a x con los primos de mi lista y si alguno lo divide ya no será primo
        for y in primos:
          if (x%y == 0):
            x_es_primo=False
            break

        #Si ninguno lo divide, se agrega a la lista
        if x_es_primo:
          primos.append(x)
        x+=1
      return primos
          
    n=int(input("\nIngresa cuantos numeros primos quieres: "))
    print("Los primeros", n, "números primos son:", obtener_numeros_primos(n))

    '''
    6.3) Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó10 €, el segundo 20 €, el tercero 40 € y así sucesivamente. Realizar un algoritmo
    para determinar cuánto debe pagar mensualmente y el total de lo que pagó
    después de los 20 meses.
    '''

    pago=10
    for x in range (20):
      print("El mes " + str(x+1) + " pago", pago)
      pago*=2

    '''
    6.4) Crea una aplicación que pida un número y calcule su factorial (El factorial de un número es el producto de todos los enteros entre 1 y el propio número y se
    representa por el número seguido de un signo de exclamación. Por ejemplo 5! =
    1x2x3x4x5=120).
    '''

    n=int(input("\nIngresa un numero para calcular su factorial: "))
    factorial=1
    for x in range (n):
      factorial*=x+1
    print("El factorial es:", factorial)

    """
    8.1 Ejercicio 1 (2 puntos)
    Escribe un programa python que pida un número por teclado y que cree un diccionario cuyas claves sean desde el número 1 hasta el número indicado, y los valores sean los cuadrados de las claves.
    """

    #Bucle para asegurar que se ingrese un número positivo
    while True:  
      n=int(input("Ingresa un numero: "))
      if(n>0):
        break

    #Inicializar el diccionario y en un bucle asignar las claves y valores.
    diccionario={}
    for i in range (n):
      diccionario[i+1]=(i+1)**2
      
    print(diccionario)

    """
    8.2 Ejercicio 2 (2 puntos)
    Escribe un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada carácter en la cadena.
    """

    #Recibe la cadena e inicializa el diccionario
    cadena=input("Escribe una cadena: ")
    diccionario={}

    #Bucle que recorre las letras de la cadena
    for x in cadena:
      if x not in diccionario:
        diccionario[x]=cadena.count(x)

    print(diccionario)

    """
    8.3 Ejercicio 3 (2 puntos)
    Vamos a crear un programa en python donde vamos a declarar un diccionario para guardar los precios de las distintas frutas. El programa pedirá el nombre de la fruta y la cantidad que se ha vendido y nos mostrará el precio final de la fruta a partir de los datos guardados en el diccionario. Si la fruta no existe nos dará un error. Tras cada consulta el programa nos preguntará si queremos hacer otra consulta.
    """

    #Se inicializa un diccionario con algunas claves y valores iniciales
    diccionario={
      "fresa" : 25,
      "pera" : 30,
      "sandia" : 10,
      "manzana" : 40,
      "uva" : 30,
      "melon" : 10,
      "mango" : 28,
      "naranja" : 30,
      "toronja" : 50,
      "granada" : 50,
      "kiwi" : 28
    }

    #Bucle que se repite mientras se quiera continuar
    continua = True
    while continua:
      fruta=input("\nQue fruta se vendio?: ")
      
      if fruta in diccionario: #Se revisa si la opcion es valida
        n=int(input("Cuantos kilos vendio?: "))
        print("Se vendio $" + str(n * diccionario[fruta]) )
      else:
        print("No tenemos esa fruta")
        
      x=int(input("Quieres continuar? si=1: "))#Se pregunta si se quiere continuar
      if x != 1:
        continua = False

    '''
    9.1 Ejercicio 1 (2 puntos)
    Realice un programa que pregunte aleatoriamente una multiplicación. El programa debe indicar si la respuesta ha sido correcta o no (en caso que la respuesta sea incorrecta el programa debe indicar cuál es la correcta). El programa preguntará 10 multiplicaciones, y al finalizar mostrará el número de aciertos.
    '''

    import random
    random.seed(None)

    #Define una funcion que toma como argumento una tupla de 2 números, y devuelve verdadero o falso dependiendo si el usuario hizo la multiplicacion correctamente
    def preguntar_multiplicacion(tupla_de_numeros): 
      
      respuesta_correcta = tupla_de_numeros[0] * tupla_de_numeros[1]
      respuesta_usuario = int(input( "\n¿Cuanto es", tupla_de_numeros[0], "x", tupla_de_numeros[1], "? "))
        
      if respuesta_usuario == respuesta_correcta:
        print("¡Respuesta correcta!")
        return True
      else:
        print("Respuesta incorrecta. La respuesta correcta es", respuesta_correcta)
        return False

    preguntas = list(map(lambda x: (random.randint(1, 10), random.randint(1, 10)), range(10)))
    #Preguntas es una lista de 10 tuplas de 2 numeros cada una
    #lambda genera 2 numeros aleatorios en forma de tupla
    #map ejecuta lambda de 0 a 9 (10 veces)
    #list convierte el objeto map en una lista

    respuestas_correctas = list(filter(preguntar_multiplicacion, preguntas))
    #filter ejecuta la funcion "preguntar_multiplicacion" iterando sobre los elementos de la lista "preguntas", cada vez que la funcion devuelva verdadero, se incluye en la lista de "respuestas_correctas" 
        
    print(f"\nJuego terminado. Obtuviste {len(respuestas_correctas)} aciertos.")

    '''
    9.2 Ejercicio 2 (2 puntos) Obtener el cuadrado de todos los elementos en la lista. Lista: 1,2,3,4,5,6,7,8,9,10
    '''

    lista=list(range(1,11))
    respuesta=list(map((lambda x: x**2), lista))
    print("\nLos cuadrados de los elementos de la lista", lista, "es", respuesta)

    '''
    9.3 Ejercicio 3 (2 puntos) Obtener la cantidad de elementos mayores a 5 en la tupla. tupla = (5,2,6,7,8,10,77,55,2,1,30,4,2,3)
    '''

    tupla = (5, 2, 6, 7, 8, 10, 77, 55, 2, 1, 30, 4, 2, 3)
    respuesta = len(list(filter(lambda x: x > 5, tupla)))
    print("\nHay", respuesta, "elementos mayores a 5 en la tupla", tupla)

    """
    9.4 Ejercicio 4 (2 puntos) Obtener la suma de todos los elementos en la lista
    """

    lista={i for i in range(1,11)}
    respuesta=sum(lista)
    print("\nLa suma de los elementos de la lista", lista, "es", respuesta)
  
  
  elif ejercicio == 0:
    break