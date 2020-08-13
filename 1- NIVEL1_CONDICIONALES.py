print(">> Program create by Luis Peralta. 3COM - Informatorio. \n")

print("SALVEMOS EL PLANETA!\n")
#DESAFIO 1:
ins = int(input("Cuantos años llevas usando insecticida en tu plantación (?: "))

if ins >= 10:
    print("Por favor solicite revisión de suelos en su plantación\n")
else:
    print("Intentaremos ayudarte con un nuevo sistema de control de plagas, y cuidaremos el suelo de tu plantación\n")
print("\n_______________________________________________________________________ \n")

#DESAFIO 2:
tamaño = int(input("HAS ENCONTRADO UN PEZ! INDIQUE SEGUN TUS CRITERIOS DE QUE TAMAÑO ES: \n1-NORMAL\n2-POR DEBAJO DE LO NORMAL\n3-POR ENCIMA DE LO NORMAL\n4-SOBREDIMENSIONADO: \n"))

if tamaño == 1:
    print("\nEl Pez esta en buenas condiciones")
elif tamaño == 2:
    print("\nEl pez tiene problemas de nutrición")
elif tamaño == 3:
    print("\nEl pez tiene síntomas de organismo contaminado")
elif tamaño == 4:
    print("\nEl pez esta contaminado")
else:
    print("\nNo has seleccionado una opción valida")
print("\n_______________________________________________________________________ \n")

#DESAFIO 3:
fert = int(input("Estas por utilizar un fertilizante, necesitamos saber en que cantidad de hectáreas tiendes a usarlo?: "))
porcen = int(input("El compuesto ha utilizar que porcenjate de abarcamiento por hectárea tiene?-MARCAR UNA OPCIÓN: \n1-DE ENTRE 0% A 9% \n2-DE ENTRE 10% A 29% \n3-DE ENTRE 30% A 59% \n4-DE ENTRE 60% A 100%\n"))
if porcen == 1 or porcen == 2 or porcen == 3 or porcen == 4:
    veget = int(input("Su tipo de suelo es de tipo matorral?: \n1-SI \n2-NO\n"))
    if porcen > 1 and veget == 2:
        print("Su tipo de suelo es factible para la utilización de fertilizantes.")
    else:
        print("Su tipo de suelo no puede utilizar fertilizantes.")
else:
    print("\nNo has seleccionado una opción valida")
print("\n_______________________________________________________________________ \n")

#DESAFIO 4:

receta = int(input("ELIJA LA RECETA ECOLOGICA QUE DESEA SABER: OPCION 1 | OPCION 2: \n"))

if receta == 1:
    opcing = int(input(" \nElija (CON NUMEROS), los ingredientes que desea,solo puedes elegir 3 y son los siguientes: \n1)COMUNES>> \nVerduras \nBerenjena \n \n2)ECOLOGICOS>> \nLentejas \nApio: \n"))
    if opcing == 1:
        ingComun = int(input("Elija entre los siguientes ingredientes comunes: \n1- Verduras  \n2- Berenjena \n3- Los Dos\n"))
        if ingComun == 1:
            print("PERFECTO! ELEGISTE VERDURAS!\n. \n. \n.\nESTA ES TU RECETA:\n____________\nRECETA ECOLOGICA N°1:\nINGREDIENTES:\nVERDURAS, LENTEJAS Y APIO.")
        elif ingComun == 2:
            print("PERFECTO! ELEGISTE BERENJENA!\n. \n. \n.\nESTA ES TU RECETA:\n____________\nRECETA ECOLOGICA N°1:\nINGREDIENTES:\nBERENJENA, LENTEJAS Y APIO.")
        elif ingComun == 3:
            ingrec1 = int(input("PERFECTO! ELEGISTE LOS 2 INGREDIENTES COMUNES!\nElija entre los siguientes 2 ingredientes: \n1- Lentejas  \n2- Apio\n"))
            if ingrec1 == 1:
                print("PERFECTO! AGREGASTE LENTEJAS!\n. \n. \n.\nESTA ES TU RECETA:\n____________\nRECETA ECOLOGICA N°1:\nINGREDIENTES:\nVERDURAS, BERENEJA Y LENTEJAS.")
            elif ingrec1 == 2:
                print("PERFECTO! AGREGASTE APIO!\n. \n. \n.\nESTA ES TU RECETA:\n____________\nRECETA ECOLOGICA N°1:\nINGREDIENTES:\nVERDURAS, BERENEJA Y APIO.")
            else:
                print("elejiste la opcion incorrecta,te quedas sin comer,lo siento :(")
        else:
            print("elejiste la opcion incorrecta,te quedas sin comer,lo siento :(")
    elif opcing == 2:
        ingrec1 = int(input("Elija entre los siguientes ingredientes de la Receta1: \n1- Lentejas  \n2- Apio \n3- Los Dos\n"))
        if ingrec1 == 1:
            print("PERFECTO! ELEGISTE LENTEJAS!\n. \n. \n.\nESTA ES TU RECETA:\n____________\nRECETA ECOLOGICA N°1:\nINGREDIENTES:\nVERDURAS, BERENJENA Y LENTEJAS.")
        elif ingrec1 == 2:
            print("PERFECTO! ELEGISTE APIO!\n. \n. \n.\nESTA ES TU RECETA:\n____________\nRECETA ECOLOGICA N°1:\nINGREDIENTES:\nVERDURAS, BERENJENA Y APIO.")
        elif ingrec1 == 3:
            ingComun = int(input("PERFECTO! ELEGISTE LOS 2 INGREDIENTES ECO!\nElija entre los siguientes 2 ingredientes: \n1- VERDURAS \n2- BERENJENA\n"))
            if ingComun == 1:
                print("PERFECTO! ELEGISTE VERDURAS!\n. \n. \n.\nESTA ES TU RECETA:\n____________\nRECETA ECOLOGICA N°1:\nINGREDIENTES:\nVERDURAS, LENTEJAS Y APIO.")
            elif ingComun == 2:
                print("PERFECTO! ELEGISTE BERENJENA!\n. \n. \n.\nESTA ES TU RECETA:\n____________\nRECETA ECOLOGICA N°1:\nINGREDIENTES:\nBERENJENA, LENTEJAS Y APIO.")
            else:
                print("elejiste la opcion incorrecta,te quedas sin comer,lo siento :(")
        else:
            print("elejiste la opcion incorrecta,te quedas sin comer,lo siento :(")
    else:
        print("elejiste la opcion incorrecta,te quedas sin comer,lo siento :(")
elif receta == 2:
    opcing = int(input(" \nElija (CON NUMEROS), los ingredientes que desea,solo puedes elegir 3 y son los siguientes: \n1)COMUNES>> \nVerduras \nBerenjena \n \n2)ECOLOGICOS>> \nMorron \nCebolla: \n"))
    if opcing == 1:
        ingComun = int(input("Elija entre los siguientes ingredientes comunes: \n1- Verduras  \n2- Berenjena \n3- Los Dos\n"))
        if ingComun == 1:
            print("PERFECTO! ELEGISTE VERDURAS!\n. \n. \n.\nESTA ES TU RECETA:\n____________\nRECETA ECOLOGICA N°2:\nINGREDIENTES:\nVERDURAS, MORRON Y CEBOLLA.")
        elif ingComun == 2:
            print("PERFECTO! ELEGISTE BERENJENA!\n. \n. \n.\nESTA ES TU RECETA:\n____________\nRECETA ECOLOGICA N°2:\nINGREDIENTES:\nBERENJENA, MORRON Y CEBOLLA.")
        elif ingComun == 3:
            ingrec1 = int(input("PERFECTO! ELEGISTE LOS 2 INGREDIENTES COMUNES!\nElija entre los siguientes 2 ingredientes: \n1- Morron  \n2- Cebolla\n"))
            if ingrec1 == 1:
                print("PERFECTO! AGREGASTE MORRON!\n. \n. \n.\nESTA ES TU RECETA:\n____________\nRECETA ECOLOGICA N°2:\nINGREDIENTES:\nVERDURAS, BERENEJA Y MORRON.")
            elif ingrec1 == 2:
                print("PERFECTO! AGREGASTE CEBOLLA!\n. \n. \n.\nESTA ES TU RECETA:\n____________\nRECETA ECOLOGICA N°2:\nINGREDIENTES:\nVERDURAS, BERENEJA Y CEBOLLA.")
            else:
                print("elejiste la opcion incorrecta,te quedas sin comer,lo siento :(")
        else:
            print("elejiste la opcion incorrecta,te quedas sin comer,lo siento :(")
    elif opcing == 2:
        ingrec1 = int(input("Elija entre los siguientes ingredientes de la Receta1: \n1- Morron  \n2- Cebolla \n3- Los Dos\n"))
        if ingrec1 == 1:
            print("PERFECTO! ELEGISTE MORRON!\n. \n. \n.\nESTA ES TU RECETA:\n____________\nRECETA ECOLOGICA N°2:\nINGREDIENTES:\nVERDURAS, BERENJENA Y MORRON.")
        elif ingrec1 == 2:
            print("PERFECTO! ELEGISTE CEBOLLA!\n. \n. \n.\nESTA ES TU RECETA:\n____________\nRECETA ECOLOGICA N°2:\nINGREDIENTES:\nVERDURAS, BERENJENA Y CEBOLLA.")
        elif ingrec1 == 3:
            ingComun = int(input("PERFECTO! ELEGISTE LOS 2 INGREDIENTES ECO!\nElija entre los siguientes 2 ingredientes: \n1- VERDURAS \n2- BERENJENA\n"))
            if ingComun == 1:
                print("PERFECTO! ELEGISTE VERDURAS!\n. \n. \n.\nESTA ES TU RECETA:\n____________\nRECETA ECOLOGICA N°2:\nINGREDIENTES:\nVERDURAS, MORRON Y CEBOLLA.")
            elif ingComun == 2:
                print("PERFECTO! ELEGISTE BERENJENA!\n. \n. \n.\nESTA ES TU RECETA:\n____________\nRECETA ECOLOGICA N°2:\nINGREDIENTES:\nBERENJENA, MORRON Y CEBOLLA.")
            else:
                print("elejiste la opcion incorrecta,te quedas sin comer,lo siento :(")
        else:
            print("elejiste la opcion incorrecta,te quedas sin comer,lo siento :(")
    else:
        print("elejiste la opcion incorrecta,te quedas sin comer,lo siento :(")
else:
    print("elejiste la opcion incorrecta,te quedas sin comer,lo siento :(")
print("\n_______________________________________________________________________ \n")

#DESAFIO 5:

barrio = input("Escriba el nombre del barrio: \n  \n")
tipoBa = int(input(" \nEl barrio, es de tipo centrico? \n1-SI|\n2-NO|\n"))
abc = "abcdefghijklmnopqrstuvwxyz"

if barrio[0].lower() <= abc[12]:
    if tipoBa == 1:
        print(" \nEl servicio de recoleccion corresponde a la SECCIÓN A.")
    elif tipoBa == 2:
        print(" \nEl servicio de recoleccion corresponde a la SECCIÓN B.")
    else:
        print("\nNo has seleccionado una opción valida")
elif barrio[0].lower() >= abc[13]:
    if tipoBa == 1:
        print(" \nEl servicio de recoleccion corresponde a la SECCIÓN B.")
    elif tipoBa == 2:
        print(" \nEl servicio de recoleccion corresponde a la SECCIÓN A.")
    else:
        print("\nNo has seleccionado una opción valida")
