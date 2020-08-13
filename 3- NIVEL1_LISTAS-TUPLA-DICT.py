print(">> Program create by Luis Peralta. 3COM - Informatorio. \n")

'''
Desafío 1
Escribir un programa que pregunte a diferentes personas cuánto
conocen sobre contaminación del 1 al 10, almacene estos valores en una lista y los muestre por pantalla ordenados de menor a mayor.
'''
lista = []

while True:
    pregunta = int(input("Cuanto sabes de contaminación(? del 1 al 10 | 0-Para salir:\n"))
    lista.append(pregunta)
    if pregunta == 0:
        lista.remove(0)
        break
lista.sort()
print(lista)
print("_________________________________________________________________________\n")
'''
Desafío 2
Crea una tupla con los factores que más afectan a los mares. Luego para jugar con niños y niñas,
aprendiendo sobre contaminación del agua crea un programa que pida números, si el numero esta entre 1 y
la longitud máxima de la tupla, muestra el contenido de esa posición sino muestra un mensaje de error.
-El programa termina cuando el usuario introduce un cero.
'''

factores = ("none","Las aguas residuales" , "Las sustancias químicas tóxicas" , "Las aguas pluviales" , "El vertido de plásticos"
, "Los vertidos de petróleo" , "La actividad minera en alta mar" , "El cambio climático")

while True:
    num = int(input("Enter a number!:\n"))
    try:
        if num >= 1 or num <= len(factores) and num != 0:
            print(factores[num])
        elif num == 0:
            print("Thanks for play")
            break
    except IndexError:
        print("Their input is an invalid value!")
print("_________________________________________________________________________\n")

'''
Desafío 3
Crea un diccionario donde la clave sea el nombre de biólogos y el valor sea el email (no es necesario validar).
Tendrás que ir pidiendo contactos hasta el usuario diga que no quiere insertar mas. No se podrán insertar nombres repetidos.
'''

biologos = dict()
while True:
    biologo = input("ingrese el nombre del biólogo:\n")
    if biologo in biologos:
        print("El nombre", biologo, "ya lo ingresaste!\n")
        continue
    email = input("ingrese el e-mail del biólogo:\n")
    biologos.setdefault(biologo,email)
    seguir = 0
    while seguir == 0:
        try:
            seguir = int(input("DESEA INGRESAR OTRO CONTACTO?: 1-SI | 2-NO\n"))
            if seguir == 1:
                continue
            elif seguir == 2:
                seguir = 2
            else:
                print("Ingresaste una opción incorrecta!")
                seguir = 0
        except ValueError:
            print("Tenes que ingresar numero!")
            seguir = 0
    if seguir == 2:
        break
lista = tuple(biologos)
for cont,bio in enumerate(lista):
    print("\nNombre del biólogo N°",cont+1,":", bio)
    print("E-mail:", biologos[bio],"\n")

print("_________________________________________________________________________\n")

"""Desafío 4
Escribir un programa que cargue una tupla con nombres de especie, y
para cada nombre de especie imprima el mensaje Hola soy ......, cuidame."""

especies = ("Animales", "Plantas", "Bacterias", "Virus","Arácnidos","Reptiles",
            "Insectos", "Peces", "Crustáceos", "Hongos", "Anfibios", "Mamíferos")
for especie in especies:
    print("Hola pertenezco a la especie de:",especie,", cuidame.")

"""Modificá el programa anterior y dada una posición inicial p y una cantidad n,
imprima el mensaje anterior para los n nombres que se encuentran a partir de la posición i."""
print("_________________________________________________________________________\n")
#ejemplo de posicion inicial:
p = 5
#ejemplo de cantidad de nombres a iterar:
n = especies[:7]

for especie in n[p::]:
    print("Hola pertenezco a la especie de:",especie,", cuidame.")
