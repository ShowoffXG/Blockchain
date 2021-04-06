import unittest
import os
import sys
ruta = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(ruta)
from src.blockchain import Bloque, Blockchain

class Test(unittest.TestCase):
    def test(self):
        test = Blockchain()
        self.assertEqual(test.cadena[0].email, "")
        self.assertTrue(test.cadena[0].hashBlq)
    
if __name__ == '__main__':
    unittest.main()