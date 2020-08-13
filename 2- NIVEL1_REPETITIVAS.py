print(">> Program create by Luis Peralta. 3COM - Informatorio. \n")
#EJERCICIOS DE APLICACIÓN DE ESTRUCTURAS DE CONTROL REPETITIVAS.
#Empieza la acción!: - Nivel 1 - Desafíos
#DESAFIO 1:
print("\n>>>ESTAS POR CREAR TU CUENTA EN WWW.NOSE.COM<<<\n")
user = input("Ingrese un nombre de usuario: \n") #Esta variable no tiene utilidad.
print("TU USUARIO ES: ", user)
contra = input("Ingrese una contraseña nueva: \n")
validar = input("PERFECTO! HAZ CREADO TU CUENTA.\n- TU CONTRASEÑA ES: " + contra + "\n- INGRESALA NUEVAMENTE PARA INICIAR SESION: \n")
cont = 5 #cantidad de intentos a realizar.
if validar == contra:
    print(" \nFELICITACIONES TE HAS LOGUEADO CORRECTAMENTE!.\nBIENVENIDO/A: " + user)
while validar != contra:
    validar = input(" \nUPS!...HAZ INGRESADO MAL TU CONTRASEÑA.TE QUEDAN " + str(cont) + " INTENTOS! \nNO SE PUDO INICIAR SESION. \nINGRESE NUEVAMENTE LA CONTRASEÑA: \n")
    cont -= 1
    if validar == contra:
        print(" \nFELICITACIONES TE HAS LOGUEADO CORRECTAMENTE!.\nBIENVENIDO/A: " + user)
    elif cont < 1:
        print("NO TE QUEDAN MAS INTENTOS...VUELVA A INTENTAR EN 30 MINUTOS.")
        break
print("\n_________________________________________________________________\n")

#DESAFIO 2:
print("\n>>>BIENVENIDO AL PROGRAMA DE RECOLECCIÓN DE PUCHOS<<<\n")
while True: #para que no tire error al dividir por cero.
    try:#excepcion para que no tire ValueError al ingresar una letra.
        n = int(input("Ingrese la cantidad de personas que trabajaron:\n"))
    except ValueError:
        print("Ingresaste una letra!!\n")
        continue
    if n != 0:
        break
    else:
        print("Ingresaste '0' personas, ingrese otro valor:\n")
        continue
Tcolillas = 0 #acumulador
menos100 = entre100y200 = mas200 = 0 #contadores
for i in range(n):
    colillas = int(input("La persona n°" + str(i+1) + "; Cuantas colillas recolecto?:\n"))
    Tcolillas = Tcolillas + colillas
    if colillas < 100 and colillas > 0:
        menos100 += 1
    elif colillas >= 100 and colillas < 200:
        entre100y200 += 1
    elif colillas >= 200:
        mas200 += 1
    else:
        print("\nEl trabajador no recolecto nada!")
P_100 = (menos100 * 100) / n
P_100Y200 = (entre100y200 * 100) / n
P_200 = (mas200 * 100) / n
print("\n-El total de colillas recolectadas es de: " + str(Tcolillas))
print("\n ESTADISTICAS:\nUN " + str("{0:.2f}".format(P_100)) +"% de personas han recolectado menos de 100 colillas")
print("\nUN " + str("{0:.2f}".format(P_100Y200)) +"% de personas han recolectado entre 100 colillas y 199 colillas")
print("\nUN " + str("{0:.2f}".format(P_200)) +"% de personas han recolectado 200 o mas colillas")
print("\n_________________________________________________________________\n")

#DESAFIO 3:
print("\n>>>LA TIENDA DE VENTAS DE ARTICULOS ESTA ABIERTA!<<<\n")
salir = 1
while salir != 0:
    monto = float(input("Ingrese el monto total de la compra del cliente:\n$"))
    tapita = int(input("Ingrese la cantidad de tapitas que entrego:\n"))
    if tapita < 50:
        print("\nETIQUETA BLANCA:\nLas tapitas recolectadas no son suficientes para un descuento!")
        print("El monto total de la compra es de: $" + str("{0:.2f}".format(monto)))
    elif tapita > 50 and tapita <= 150:
        print("\nETIQUETA AMARILLA:\nLas tapitas recolectadas tienen un 25% de descuento sobre el total de la compra!")
        descuento = (25 * monto) / 100
        print("El monto total de la compra es de: $" + str("{0:.2f}".format(monto - descuento)))
    else:
        print("\nETIQUETA ROJA:\nLas tapitas recolectadas SUPERAN LAS 150!, esta compra tiene un 40% de descuento sobre el total")
        descuento = (40 * monto) / 100
        print("El monto total de la compra es de: $" + str("{0:.2f}".format(monto - descuento)))
    salir = int(input("\nPRESIONE UN NUMERO CUALQUIERA PARA SEGUIR OPERANDO | PARA CERRAR LA CAJA PRESIONE 0:\n"))
print("\nEspero que os haya iluminado!, GRACIAS VUELVAN PRONTO.")
print("\n_________________________________________________________________\n")

#DESAFIO 4:
print("\n>>>CREACIÓN DE TABLERO MANUAL<<<\n")
filas = int(input("ingrese la cantidad de filas de su tablero:\n"))
columnas = int(input("ingrese la cantidad de columnas de su tablero:\n"))
v = ("|_V_|") #cuadrados verdes
b = ("|_B_|") #cuadrados blancos
ab =""
ab2 =""
print("TABLERO ECOLÓGICO:\n")
for i in range(columnas):
    if i % 2 == 0:
        ab = ab + v
        ab2 = ab2 + b
    else:
        ab = ab + b
        ab2 = ab2 + v
for i in range(filas):
    if i % 2 == 0:
        print(ab)
    else:
        print(ab2)
print("\n_________________________________________________________________\n")

#DESAFIO 5:
print("\n>>>BIENVENIDO AL SISTEMA DE CONTROL DE VEHÍCULOS PARA GENTE QUE TIRA BASURA<<<\n")
vcont = 0 #contador de cantidad de vehículos
vbas = 0 #contador de personas que tiraron o no basura.
baymult = 0 #contador de personas que tiraron basura y habian sido multadas.
si = "s" #variable que me permite salir del ciclo.
while si == "s":
    patente = input("Ingrese la patente del vehículo(6 digitos): ")
    if len(patente) < 6 or len(patente) > 6:
        print("Ingresaste mal la cantidad de digitos de tu patente!.")
        continue
    vcont += 1
    while True:
        tiro = int(input("tiro basura? 1-SI | 0-NO\n"))
        if tiro > 1:
            continue
        else:
            break
    while True:
        multa = int(input("habia sido multado? 1-SI | 0-NO\n"))
        if multa > 1:
            continue
        else:
            break
    if tiro == 1:
        vbas += 1
        if multa == 1:
            baymult += 1
    print("La patente tiene el siguiente codigo: " + patente + str(tiro) + str(multa))
    si = input("Desea ingresar otra patente?: s-SI | n-NO\n")

print("\nla cantidad de vehículos observados fue de: " + str(vcont))
print("la cantidad de vehículos que han tirado basura fue de: " + str(vbas))
try:#excepcion que realizo por si tira error de division por cero.
    porcenM = (baymult * 100) / vbas #variable que saca el porcentaje.
    print("El porcentaje de personas que tiraron basuras y ya habian sido multados es de: " + str("{0:.2f}".format(porcenM)) +"%")
except:
    print("El porcentaje de personas que tiraron basuras y ya habian sido multados es de: 0.0%")

print("\nGRACIAS Y HASTA LUEGO!.")
