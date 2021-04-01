import unittest
import os
import sys
ruta = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(ruta)
from src.blockchain import Bloque

class Test(unittest.TestCase):
    def test(self):
        test = Bloque("stefano.simoni.10.xg@gmail.com", "Certificado", "txt")
        self.assertEqual(test.archivo, "txt")
        self.assertEqual(test.email, "stefano.simoni.10.xg@gmail.com")
    
if __name__ == '__main__':
    unittest.main()