import unittest
import os
import sys
ruta = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(ruta)
from src.bloque import Bloque

class BloqueTest(unittest.TestCase):
    def test_bloque_should_to_be_true_when_bloque_is_created(self):
            test = Bloque(0, "alguien@gmail.com", "test", "hashArch", "2021-04-12 13:00:00", "hashAnt", 0)
            self.assertEqual(0, test.i)
            self.assertEqual("alguien@gmail.com", test.email)
            self.assertEqual("test", test.motivo)
            self.assertEqual("hashArch", test.hashArch)
            self.assertEqual("2021-04-12 13:00:00", test.tiempo)
            self.assertEqual("hashAnt", test.hashAnt)
            self.assertEqual("00d91aa5774a33f4da89c1ad502735f00e31ad756b3d9c5849dd9459ccef5ff1", test.hashBlq)

if __name__ == '__main__': unittest.main()