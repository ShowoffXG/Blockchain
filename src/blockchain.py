from datetime import datetime
from src.bloque import Bloque

class Blockchain:
    def __init__(self):
        self.cadena = []
        self.crearGenesis()

    def crearGenesis(self):
        bloqueGenesis = Bloque(0, "", "", "0", "2021-04-12 12:00:00", "0")
        self.cadena.append(bloqueGenesis)

    def crearBloque(self, email, motivo, hashArch):
        bloqueNuevo = Bloque(self.bloqueSig(), email, motivo, hashArch, "2021-04-12 13:00:00", self.traeHashAnt())
        self.cadena.append(bloqueNuevo)

    def traeHashBloque(self, i):
        return self.cadena[i].hashBlq

    def bloqueSig(self):
        return len(self.cadena)

    def traeHashAnt(self):
        return self.traeHashBloque(self.bloqueSig()-1)

    def getDateTimeString(self):
        dt = datetime.now()
        return dt.isoformat()

    def getFormatDate(self, tiempo):
        return datetime.strptime(tiempo, '%Y-%m-%d %H:%M:%S')