from hashlib import sha256
import json

class Bloque:
    def __init__(self, i, email, motivo, hashArch, tiempo, hashAnt):
        self.i = i
        self.email = email
        self.motivo = motivo
        self.hashArch = hashArch
        self.tiempo = tiempo
        self.hashAnt = hashAnt
        self.hashBlq = self.crearHash()

    def crearHash(self):
        hash = json.dumps(self.__dict__, sort_keys=True)
        return sha256(hash.encode()).hexdigest()
