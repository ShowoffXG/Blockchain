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
        bloque0 = test.getBloquePorId(0)
        self.assertEqual(0, bloque0.i)
        self.assertEqual("", bloque0.email)
        self.assertEqual("", bloque0.motivo)
        self.assertEqual("0", bloque0.hashArch)
        self.assertEqual("2021-04-12 12:00:00", bloque0.tiempo)
        self.assertEqual("0", bloque0.hashAnt)
        self.assertEqual("0d93cc02431f99450c6953ddb06ca1c853fe37c3b8383e9b703dc627eeb5e13d", test.traeHashBloque(0))

    def test_bloque_should_to_be_true_when_bloque_is_created(self):
        test = Bloque(0, "alguien@gmail.com", "test", "hashArch", "2021-04-12 13:00:00", "hashAnt", 0)
        self.assertEqual(0, test.i)
        self.assertEqual("alguien@gmail.com", test.email)
        self.assertEqual("test", test.motivo)
        self.assertEqual("hashArch", test.hashArch)
        self.assertEqual("2021-04-12 13:00:00", test.tiempo)
        self.assertEqual("hashAnt", test.hashAnt)
        self.assertEqual("02cabf80d186fd34a7e3298c4edd4961fe82e247c291af6d7b09f33233477443", test.hashBlq)
    
    def test_bloque1_should_to_be_true_when_bloque1_works(self):
        test = Blockchain()
        test._Blockchain__crearBloque("alguien@gmail.com", "test", "hashArch")
        bloque1 = test.getBloquePorId(1)
        self.assertEqual(1, bloque1.i)
        self.assertEqual("alguien@gmail.com", bloque1.email)
        self.assertEqual("test", bloque1.motivo)
        self.assertEqual("hashArch", bloque1.hashArch)
        self.assertEqual("2021-04-12 13:00:00", bloque1.tiempo)
        self.assertEqual("0d93cc02431f99450c6953ddb06ca1c853fe37c3b8383e9b703dc627eeb5e13d", bloque1.hashAnt)
        self.assertEqual("0b4f98810bf8e6f6d38abc0e3ae0c91b99e2b2e23e2177abd473410ee65397f5", test.traeHashBloque(1))

    def test_Singleton_should_to_be_true_when_Singleton_is_created(self):
        test1 = Blockchain()
        test2 = Blockchain()
        self.assertTrue(id(test1) == id(test2), "Test Singleton don't works")
        
if __name__ == '__main__':
    unittest.main()