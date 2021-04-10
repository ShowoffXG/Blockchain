import unittest
import os
import sys
ruta = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(ruta)
from src.blockchain import Bloque, Blockchain

class Test(unittest.TestCase):
    def test_bloqueGenesis(self):
        test = Blockchain()
        self.assertEqual(test.cadena[0].i, 0)
        self.assertEqual(test.cadena[0].email, "")
        self.assertEqual(test.cadena[0].motivo, "")
        self.assertEqual(test.cadena[0].hashArch, "0")
        self.assertEqual(test.cadena[0].hashAnt, "0")
        self.assertEqual("32448a9a2e0b20a10125aa5a1ebdb9eac8520b70bdea10450dbf0fd052f528a6", test.traeHashBloque(0))
    
if __name__ == '__main__':
    unittest.main()