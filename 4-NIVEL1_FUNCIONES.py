print(">> Program create by Luis Peralta. 3COM - Informatorio. \n")
#Ejercicios de funciones de empieza la acción, nivel 1.
"""Desafío 1
150 años es el tiempo que tarda una bolsa de plástico común en degradarse y una botella de PET puede tardar 1.000 años en desaparecer.
Por otro lado los Envases de tetrabrik pueden tardar hasta 30 años en degradarse.
Un trozo de chicle tarda 5 años en degradarse.
-> Se solicita una función para que dado el ingreso de un elemento, se solicite tipo: Bolsa de plástico, botella PET, envase tetrabrik o chicle,
e imprima la cantidad de años que tarda en degradarse."""

def se_degrada(tipo):
    #Recibe parametro y compara segun elemento elegido.
    if tipo == 1:
        print("Tu producto '" + elemento + "' tarda 150 años en degradarse!")
    elif tipo == 2:
        print("Tu producto '" + elemento + "' tarda 1000 años en degradarse!")
    elif tipo == 3:
        print("Tu producto '" + elemento + "' tarda 30 años en degradarse!")
    elif tipo == 4:
        print("Tu producto '" + elemento + "' tarda 5 años en degradarse!")
    else:
        print("Ingresaste una opción incorrecta!")
while True:
    elemento = input("Escriba un producto: ")
    print("De que tipo es este producto?: ")
    tipo = int(input("1- BOLSA DE PLASTICO\n2- BOTELLA PET\n3- TETRABRIK\n4- CHICLE\nN°"))
    se_degrada(tipo)
    salir = int(input("Desea ingresar otro producto?\n0-NO\nOTRO N°-SI:\n"))
    if salir == 0:
        print("Gracias, hasta luego!")
        break
    else:
        continue
print("\n__________________________________________________\n")

"""Desafío 2
Realiza una función llamada relacion(a, b) que a partir de toneladas recicladas de dos ciudades se cumpla lo siguiente:
Si el primer número es mayor que el segundo, debe devolver el nombre de la ciudad 1.
Si el primer número es menor que el segundo, debe devolver el nombre de la ciudad 2.
Si ambos números son iguales, debe devolver el nombre de ambas."""

def relacion(a, b):
    #recibe 2 parametros y los compara dependiendo su cantidad.
    if a > b:
        print(ciudad1)
    elif a == b:
        print(ciudad1,ciudad2)
    else:
        print(ciudad2)
while True:
    ciudad1 = input("Ingrese el nombre de la 1er ciudad: ")
    tonelada1 = int(input("cuantas toneladas recicla esta ciudad?: "))
    ciudad2 = input("Ingrese el nombre de la 2da ciudad: ")
    tonelada2 = int(input("cuantas toneladas recicla esta ciudad?: "))
    relacion(tonelada1,tonelada2)
    salir = int(input("Desea ingresar otras ciudades?\n1-SI\n2-NO:\n"))
    if salir == 2:
        print("Gracias, hasta luego!")
        break
    elif salir == 1:
        continue
    else:
        print("opc incorrecta, se saldra del programa,adios!")
        break
print("\n__________________________________________________\n")

"""Desafío 3
Realiza una función separar(lista) que tome una lista que tenga datos de
cantidad de árboles plantados en diferentes ciudades de Argentina durante la cuarentena.
Luego la función debe devolver dos listas ordenadas.
La primera con las cantidades que superen los 100 y la segunda con el resto.
Qué cantidad de ciudades han plantado más de 100 árboles durante cuarentena."""
ciudades = []
arboles = []
cont = int(input("Ingrese la cantidad de ciudades a escribir: "))
for i in range(cont):
    ciudades.append(input("Ingrese el nombre de la ciudad "+str(i+1)+": "))
    arboles.append(int(input("Ingrese la cantidad de arboles que planto esta ciudad: ")))
    arboles.sort()

def separar(lista):
    """Esta función recibe una lista y dependiendo
    la cantidad guarda en una(si es > 100) y en otra (si en menor).
    la lista ya viene ordenada del ciclo for con el metodo .sort()"""
    cantidad = 0
    mas100 = []
    menos100 = []
    for arbol in lista:
        if arbol > 100:
            mas100.append(arbol)
            cantidad += 1            
        else:
            menos100.append(arbol)
    print("Superan mas de 100:", mas100)
    print("menos de 100:", menos100)
    print("la cantidad de ciudades que plantaron mas de 100 es:", cantidad)

separar(arboles)