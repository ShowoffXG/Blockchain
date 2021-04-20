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
    print ("Blockchain")
    bloqueFinal = blockchain.getBloquePorId(-1).i
    for i in range(0, bloqueFinal):
        bloque = blockchain.getBloquePorId(i)
        if i == 0:
            dash()
            print ("Registro unico de documentacion")
            print ("Bloque 0/Genesis:")
            print ("Hash del Bloque:", bloque.hashBlq)
        else:
            dash()
            print ("Registro unico de documentacion")
            print ("Bloque:", i)
            print ("A nombre de:", bloque.email)
            print ("Motivo:", bloque.motivo)
            print ("Fecha:", bloque.tiempo)
            print ("Hash del Bloque:", bloque.hashBlq)

def mostrar(blockchain, i):
    bloque = blockchain.getBloquePorId(i)
    print ("Bloque", bloque.i)
    print ("Registro unico de documentacion")
    print ("A nombre de:", bloque.email)
    print ("Motivo:", bloque.motivo)
    print ("Fecha:", bloque.tiempo)
    print ("Hash del Bloque:", bloque.hashBlq)

menu()