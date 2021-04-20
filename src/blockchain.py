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