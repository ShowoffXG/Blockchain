from datetime import datetime
from hashlib import sha256
import json

class Bloque:
    def __init__(self, i, email, motivo, hashArch, hashAnt):
        self.i = i
        self.email = email
        self.motivo = motivo
        self.hashArch = hashArch
        #self.tiempo = datetime.now()
        self.hashAnt = hashAnt
        self.hashBlq = self.crearHash()

    def crearHash(self):
        hash = json.dumps(self.__dict__, sort_keys=True)
        return sha256(hash.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.cadena = []
        self.crearGenesis()

    def crearGenesis(self):
        bloqueGenesis = Bloque(0, "", "", "0", "0")
        self.cadena.append(bloqueGenesis)

    def traeHashBloque(self, i):
        return self.cadena[i].hashBlq