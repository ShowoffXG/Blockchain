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

    def __crearBloque(self, email, motivo, hashArch):
        bloqueNuevo = Bloque(self.__bloqueSig(), email, motivo, hashArch, "2021-04-12 13:00:00", self.__traeHashAnt(), self.__zero_count)
        self.__cadena.append(bloqueNuevo)

    def traeHashBloque(self, i):
        return self.__cadena[i].hashBlq

    def __bloqueSig(self):
        return len(self.__cadena)

    def __traeHashAnt(self):
        return self.traeHashBloque(self.__bloqueSig()-1)

    def __getDateTimeString(self):
        dt = datetime.now()
        return dt.isoformat()

    def __getFormatDate(self, tiempo):
        return datetime.strptime(tiempo, '%Y-%m-%d %H:%M:%S')

    def getBloquePorId(self, i):
        return self.__cadena[i]