from hashlib import sha256
from bson import json_util
import json
from datetime import datetime

class Bloque:
    def __init__(self, i, email, motivo, hashArch, tiempo, hashAnt, zero_count):        #Constructor de la clase Bloque
        self.nonce = 0
        self.i = i      #Indice del bloque
        self.email = email
        self.motivo = motivo
        self.hashArch = hashArch
        self.tiempo = tiempo
        self.hashAnt = hashAnt
        self.hashBlq = self.crearHashBlq(zero_count)

    def crearHashBlq(self, zero_count):     #Metodo que calcula el hash del bloque dependiendo de la dificultad para calcularlo
        if zero_count == 0:     #Si la dificultad esta en default, osea igual a 0, significa que el hash se calculara en base a si el dia de la fecha es par o impar
            if datetime.strptime(self.tiempo, '%Y-%m-%d %H:%M:%S').day % 2 == 0:        #Si el dia de la fecha es par la dificultad cambiara de 0 a 2, es decir, el hash debera comenzar con 2 ceros al principio
                zero_count = 2
            else:       #Si es impar, sera un solo 0 al principio del hash
                zero_count = 1
        while self.nonce >= 0:      #Calculo para dar con el hash correspondiente
            hash = self.crearHash()     #Se crea el hash y se lo asigna a una variable
            if hash[0:zero_count] == '0' * zero_count:      #Si el hash desde su primer digito hasta el valor que indica la dificultad es igual a la cantidad de ceros que se busca, devuelve ese hash y sale del metodo
                self.nonce = -1
            else:       #Si no, seguira buscando hasta dar con el hash necesario
                self.nonce += 1
        return hash

    def crearHash(self):        #Metodo para crear un hash
        hash = json.dumps(self.__dict__, sort_keys=True, default=json_util.default)     #hash guardara, en formato json, los datos proporcionados en el constructor de la clase, en el orden en el que estan definidos
        return sha256(hash.encode()).hexdigest()        #Se regresa en formato sha256, es decir, el hash, el formato json de todos los datos proporcionados