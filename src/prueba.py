import os
import sys
ruta = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(ruta)
from src.blockchain import Blockchain

bc = Blockchain()

def menu():
    os.system("CLS")
    print("Universidad de la Cuenca del Plata")
    dash()
    print("\t1 - Registrar certificado")
    print("\t2 - Mostrar Blockchain")
    print("\t3 - Buscar un certifido determinado")
    print("\t0 - Salir")
    try:
        opcionMenu = int(input(">> Inserta un numero valor >> "))
    except ValueError:
        menu()
    while True:
        if opcionMenu == 1:
            registrarCertif(bc)
            atras()
        elif opcionMenu == 2:
            mostrarBlockchain(bc)
            atras()
        elif opcionMenu == 3:
            mostrar(bc)
            atras()
        elif opcionMenu == 0:
            exit(1)
        else:
            menu()

def registrarCertif(blockchain):
    os.system("CLS")
    print("Registro unico de documentacion")
    dash()
    print("Ingrese los datos requeridos")
    dash()
    email = str(input("Ingrese su email: "))
    motivo = str(input("Motivo: "))
    hashArch = str(input("Nombre de su documento o archivo a registrar: "))
    blockchain.crearBloque(email, motivo, hashArch)
    dash()
    print("Su informacion fue registrada con el hash:")
    print(blockchain.traeHashBloque(-1))

def dash():
    dash = '-' * 64
    print(dash)

def atras():
    dash()
    input(">> Presione una tecla para volver al menu <<")
    menu()

def mostrarBlockchain(blockchain):
    os.system("CLS")
    print ("Blockchain")
    bloqueFinal = blockchain.getBloquePorId(-1).i
    print ("Registro unico de documentacion")
    for i in range(0, bloqueFinal + 1):
        bloque = blockchain.getBloquePorId(i)
        if i == 0:
            dash()
            print ("Bloque 0/Genesis:")
            print ("Hash del Bloque:", bloque.hashBlq)
        else:
            dash()
            print ("Bloque:", i)
            print ("A nombre de:", bloque.email)
            print ("Motivo:", bloque.motivo)
            print ("Fecha:", bloque.tiempo)
            print ("Hash del Bloque:", bloque.hashBlq)

def mostrar(blockchain):
    os.system("CLS")
    hash = str(input("Hash del certificado que busca: "))
    bloque = blockchain.traeBlqXHash(hash)
    if  hash == blockchain.traeHashBloque(0):
        dash()
        print ("Registro unico de documentacion")
        print ("Bloque 0/Genesis:")
    else:
        dash()
        print ("Registro unico de documentacion")
        print ("Bloque", bloque.i)
        print ("A nombre de:", bloque.email)
        print ("Motivo:", bloque.motivo)
        print ("Fecha:", bloque.tiempo)

menu()