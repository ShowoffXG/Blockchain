import unittest
import os
import sys
ruta = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(ruta)
from src.bloque import Bloque

class BloquesIgualesTest(unittest.TestCase):
    def test_hashEquals_should_to_be_true_when_bloque1_and_bloque2_be_equals(self):
            bloque1 = Bloque(3, "alguien@gmail.com", "test", "hashArch", "2021-04-12 13:00:00", "hashAnt", 0)
            bloque2 = Bloque(3, "alguien@gmail.com", "test", "hashArch", "2021-04-12 13:00:00", "hashAnt", 0)
            self.assertEqual(bloque1.hashBlq, bloque2.hashBlq)

if __name__ == '__main__':
    unittest.main()