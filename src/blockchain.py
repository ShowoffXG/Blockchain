from datetime import datetime
from src.bloque import Bloque
from src.singleton import Singleton

class Blockchain(metaclass = Singleton):
    def __init__(self):
        self.__zero_count = 0
        self.__cadena = []
        self.__crearGenesis()

    def __crearGenesis(self):
        bloqueGenesis = Bloque(0, "", "", "0", "2021-04-12 12:00:00", "0", self.__zero_count)
        self.__cadena.append(bloqueGenesis)

    def __crearBloque(self, email, motivo, hashArch, tiempo):
        bloqueNuevo = Bloque(self.__bloqueSig(), email, motivo, hashArch, tiempo, self.__traeHashAnt(), self.__zero_count)
        self.__cadena.append(bloqueNuevo)

    def crearBloque(self, email, motivo, hashArch):
        bloqueNuevo = Bloque(self.__bloqueSig(), email, motivo, hashArch, datetime.utcnow, self.__traeHashAnt(), self.__zero_count)
        self.__cadena.append(bloqueNuevo)

    def traeHashBloque(self, i):
        return self.__cadena[i].hashBlq

    def __bloqueSig(self):
        return len(self.__cadena)

    def __traeHashAnt(self):
        return self.traeHashBloque(self.__bloqueSig() - 1)

    def traeBlqXHash(self, hashBlq):
        for bloque in self.__cadena:
            if hashBlq == bloque.hashBlq:
                return bloque
        return "No se encontro el Bloque mediante el hash ofrecido"

    def mostrarBlockchain(self):
        print ("Blockchain")
        for i in range(self.__bloqueSig()):
            print ("Registro unico de documentacion")
            print ("Se registro correctamente el documento")
            print ("A nombre de: %s", self.__cadena[i].email)
            print ("Motivo: %s", self.__cadena[i].motivo)
            print ("Fecha: %s", self.__cadena[i].tiempo)
            print ("Hash del Bloque: %s", self.__cadena[i].hashBlq)

    def mostrar(self, i):
        print ("Bloque %d", i)
        print ("Registro unico de documentacion")
        print ("Se registro correctamente el documento")
        print ("A nombre de: %s", self.__cadena[i].email)
        print ("Motivo: %s", self.__cadena[i].motivo)
        print ("Fecha: %s", self.__cadena[i].tiempo)
        print ("Hash del Bloque: %s", self.__cadena[i].hashBlq)

    def getBloquePorId(self, i):
        return self.__cadena[i]