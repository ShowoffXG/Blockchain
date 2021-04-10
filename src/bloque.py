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
