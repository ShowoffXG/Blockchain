from datetime import datetime

class Bloque:
    def __init__(self, email, motivo, archivo):
        self.email = email
        self.motivo = motivo 
        self.archivo = archivo
        self.tiempo = datetime.now()
