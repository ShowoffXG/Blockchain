import os
import sys
from datetime import datetime
ruta = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(ruta)
from src.bloque import Bloque
from src.singleton import Singleton

class Blockchain(metaclass = Singleton):
    def __init__(self):     #Constructor de la clase Blockchain
        self.__zero_count = 0       #Dificultad para calcular el hash del bloque
        self.__cadena = []      #Lista que contendra a la Blockchain
        self.__crearGenesis()       #Llamado al metodo para crear el bloque Genesis una vez que se crea una Blockchain

    def __crearGenesis(self):       #Metodo privado para crear el bloque Genesis, el cual debera estar en la posicion 0 de la Blockchain y sin ningun otro dato relevante, mas que la dificultad y la fecha para crear su hash
        bloqueGenesis = Bloque(0, "", "", "0", "2021-04-12 12:00:00", "0", self.__zero_count)
        self.__cadena.append(bloqueGenesis)

    def __crearBloque(self, email, motivo, hashArch, tiempo):       #Metodo privado para crear un bloque e insertarlo en la Blockchain, el cual solo es usado solo para comprobar si se crea en los Tests
        bloqueNuevo = Bloque(self.__bloqueSig(), email, motivo, hashArch, tiempo, self.__traeHashAnt(), self.__zero_count)
        self.__cadena.append(bloqueNuevo)

    def crearBloque(self, email, motivo, hashArch):     #Metodo principal para crear un bloque e insertarlo en la Blockchain
        bloqueNuevo = Bloque(self.__bloqueSig(), email, motivo, hashArch, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), self.__traeHashAnt(), self.__zero_count)
        self.__cadena.append(bloqueNuevo)

    def traeHashBloque(self, i):        #Metodo para traer el hash de un bloque x mediante su posicion en la Blockchain
        return self.__cadena[i].hashBlq

    def __bloqueSig(self):          #Metodo privado que devuelve la longitud de la Blockchain y es usado para darle indice a los siguientes bloques de la Blockchain
        return len(self.__cadena)

    def __traeHashAnt(self):        #Metodo privado que devuelve el hash del bloque anterior a un bloque x
        return self.traeHashBloque(self.__bloqueSig() - 1)

    def traeBlqXHash(self, hashBlq):        #Metodo que busca y devuelve, si existe, un bloque mediante su hash
        for bloque in self.__cadena:
            if hashBlq == bloque.hashBlq:
                return bloque

    def getBloquePorId(self, i):        #Metodo que devuelve un bloque x mediante su posicion en la Blockchain
        return self.__cadena[i]

    def cambiarZero_count(self, zero_count):        #Metodo para cambiar el valor de la variable zero_count
        self.__zero_count = zero_count

    def validar(self):      #Metodo que validara cada uno de los bloques de la Blockchain y comparara si el hash del bloque x es igual al hashAnt del bloque y
        hash = '0'      #Sabemos que el hashAnt del bloque Genesis es 0
        for bloque in self.__cadena:        #Recorre la lista y va comparando los hashs
            if bloque.hashAnt == hash:      #Si es verdad cambia el valor del hash para seguir comparando
                hash = bloque.hashBlq
            else:
                return False
        if self.ultimoBlq().hashBlq == hash:        #Como la variable hash va a almacenar el hash del ultimo bloque verificamos mediante el metodo ultimoBlq() si son iguales y devolvera bloolean
            return True     #Si los hashs coinciden devuelve True
        else:
            return False        #Si no, devuelve False
    
    def ultimoBlq(self):        #Metodo que devolvera el ultimo bloque de la Blockchain
        return self.__cadena[-1]