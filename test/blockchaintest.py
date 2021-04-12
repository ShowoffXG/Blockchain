import unittest
import os
import sys
ruta = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(ruta)
from src.blockchain import Blockchain
from src.bloque import Bloque

class Test(unittest.TestCase):
    def test_bloqueGenesis_should_to_be_true_when_bloqueGenesis_is_created(self):
        test = Blockchain()
        self.assertEqual(0, test.cadena[0].i)
        self.assertEqual("", test.cadena[0].email)
        self.assertEqual("", test.cadena[0].motivo)
        self.assertEqual("0", test.cadena[0].hashArch)
        self.assertEqual("2021-04-12 12:00:00", test.cadena[0].tiempo)
        self.assertEqual("0", test.cadena[0].hashAnt)
        self.assertEqual("37e8cba7ad921c1d6a511656a36b7ff08fa5c6881c743b3226ad91bff6cf8212", test.traeHashBloque(0))

    def test_bloque_should_to_be_true_when_bloque_is_created(self):
        test = Bloque(0, "alguien@gmail.com", "test", "hashArch", "2021-04-12 13:00:00", "hashAnt")
        self.assertEqual(0, test.i)
        self.assertEqual("alguien@gmail.com", test.email)
        self.assertEqual("test", test.motivo)
        self.assertEqual("hashArch", test.hashArch)
        self.assertEqual("2021-04-12 13:00:00", test.tiempo)
        self.assertEqual("hashAnt", test.hashAnt)
        self.assertEqual("b9c6c4d882656839d0b7af121820e128a5c91e01f54ef8d737d5aef8caf3943c", test.hashBlq)
    
    def test_bloque1_should_to_be_true_when_bloque1_is_created(self):
        test = Blockchain()
        test.crearBloque("alguien@gmail.com", "test", "hashArch")
        self.assertEqual(1, test.cadena[1].i)
        self.assertEqual("alguien@gmail.com", test.cadena[1].email)
        self.assertEqual("test", test.cadena[1].motivo)
        self.assertEqual("hashArch", test.cadena[1].hashArch)
        self.assertEqual("2021-04-12 13:00:00", test.cadena[1].tiempo)
        self.assertEqual("37e8cba7ad921c1d6a511656a36b7ff08fa5c6881c743b3226ad91bff6cf8212", test.cadena[1].hashAnt)
        self.assertEqual("c56c63268f28202ff06f1c8984eda738eebfffb658be64054fdd133f44f53b17", test.traeHashBloque(1))

if __name__ == '__main__':
    unittest.main()