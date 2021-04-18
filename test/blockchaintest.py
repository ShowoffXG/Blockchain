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
        self.assertEqual("00dda3a30da67fb02b580932fad8985acba1fb141179a2552238c0b968f8c71d", test.traeHashBloque(0))

    def test_bloque_should_to_be_true_when_bloque_is_created(self):
        test = Bloque(0, "alguien@gmail.com", "test", "hashArch", "2021-04-12 13:00:00", "hashAnt", 0)
        self.assertEqual(0, test.i)
        self.assertEqual("alguien@gmail.com", test.email)
        self.assertEqual("test", test.motivo)
        self.assertEqual("hashArch", test.hashArch)
        self.assertEqual("2021-04-12 13:00:00", test.tiempo)
        self.assertEqual("hashAnt", test.hashAnt)
        self.assertEqual("00d91aa5774a33f4da89c1ad502735f00e31ad756b3d9c5849dd9459ccef5ff1", test.hashBlq)
    
    def test_bloque1_should_to_be_true_when_bloque1_works(self):
        test = Blockchain()
        test._Blockchain__crearBloque("alguien@gmail.com", "test", "hashArch", "2021-04-12 13:00:00")
        bloque1 = test.getBloquePorId(1)
        self.assertEqual(1, bloque1.i)
        self.assertEqual("alguien@gmail.com", bloque1.email)
        self.assertEqual("test", bloque1.motivo)
        self.assertEqual("hashArch", bloque1.hashArch)
        self.assertEqual("2021-04-12 13:00:00", bloque1.tiempo)
        self.assertEqual("00dda3a30da67fb02b580932fad8985acba1fb141179a2552238c0b968f8c71d", bloque1.hashAnt)
        self.assertEqual("003f2f68f8602962d2274a1beb6639c3b0c78b172fe04c9ef4e744d33a6d125b", test.traeHashBloque(1))

    def test_bloque2_should_to_be_true_when_bloque2_works(self):
        test = Blockchain()
        test._Blockchain__crearBloque("otro@gmail.com", "test2", "hashArch2", "2021-04-12 13:00:00")
        bloque2 = test.getBloquePorId(2)
        self.assertEqual(2, bloque2.i)
        self.assertEqual("otro@gmail.com", bloque2.email)
        self.assertEqual("test2", bloque2.motivo)
        self.assertEqual("hashArch2", bloque2.hashArch)
        self.assertEqual("2021-04-12 13:00:00", bloque2.tiempo)
        self.assertEqual("003f2f68f8602962d2274a1beb6639c3b0c78b172fe04c9ef4e744d33a6d125b", bloque2.hashAnt)
        self.assertEqual("00877321b660e070e3940a5e96783e4382e3081a843a2a8a9d83b0482bbd2a2c", test.traeHashBloque(2))

    def test_hashEquals_should_to_be_true_when_bloque1_and_bloque2_be_equals(self):
        bloque1 = Bloque(3, "alguien@gmail.com", "test", "hashArch", "2021-04-12 13:00:00", "hashAnt", 0)
        bloque2 = Bloque(3, "alguien@gmail.com", "test", "hashArch", "2021-04-12 13:00:00", "hashAnt", 0)
        self.assertEqual(bloque1.hashBlq, bloque2.hashBlq)

    def test_giveBloque1ForHash_should_to_be_true_when_giveBloque1ForHash_works(self):
        test = Blockchain()
        test._Blockchain__crearBloque("alguien@gmail.com", "test", "hashArch", "2021-04-12 13:00:00")
        bloque1 = test.getBloquePorId(1)
        self.assertEqual(test.traeBlqXHash("003f2f68f8602962d2274a1beb6639c3b0c78b172fe04c9ef4e744d33a6d125b"), bloque1)

    def test_Singleton_should_to_be_true_when_Singleton_is_created(self):
        test1 = Blockchain()
        test2 = Blockchain()
        self.assertTrue(id(test1) == id(test2), "Test Singleton don't works")
        
if __name__ == '__main__':
    unittest.main()