from src.bloque import Bloque

class Blockchain:
    def __init__(self):
        self.cadena = []
        self.crearGenesis()

    def crearGenesis(self):
        bloqueGenesis = Bloque(0, "", "", "0", "0")
        self.cadena.append(bloqueGenesis)

    def traeHashBloque(self, i):
        return self.cadena[i].hashBlq