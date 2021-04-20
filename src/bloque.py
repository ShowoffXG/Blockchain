from hashlib import sha256
from bson import json_util
import json
from datetime import datetime

class Bloque:
    def __init__(self, i, email, motivo, hashArch, tiempo, hashAnt, zero_count):
        self.nonce = 0
        self.i = i
        self.email = email
        self.motivo = motivo
        self.hashArch = hashArch
        self.tiempo = tiempo
        self.hashAnt = hashAnt
        self.hashBlq = self.crearHashBlq(zero_count)

    def crearHashBlq(self, zero_count):
        if zero_count == 0:
            if datetime.strptime(self.tiempo, '%Y-%m-%d %H:%M:%S').day % 2 == 0:
                zero_count = 2
            else:
                zero_count = 1
        while self.nonce >= 0:
            hash = self.crearHash()
            if hash[0:zero_count] == '0' * zero_count:
                self.nonce = -1
            else:
                self.nonce += 1
        return hash

    def crearHash(self):
        hash = json.dumps(self.__dict__, sort_keys=True, default=json_util.default)
        return sha256(hash.encode()).hexdigest()