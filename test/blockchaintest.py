import unittest
import os
import sys
ruta = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(ruta)
from src.blockchain import Bloque, Blockchain

class Test(unittest.TestCase):
    def test_bloqueGenesis_i_debe_ser_verdad_cuando_i_es_0(self):
        test = Blockchain()
        self.assertEqual(test.cadena[0].i, 0)

    def test_bloque_genesis_email_debe_ser_verdad_cuando_email_esta_vacio(self):
        test = Blockchain()
        self.assertEqual(test.cadena[0].email, "")

    def test_bloqueGenesis_motivo_debe_ser_verdad_cuando_motivo_esta_vacio(self):
        test = Blockchain()
        self.assertEqual(test.cadena[0].motivo, "")

    def test_bloqueGenesis_hasArch_debe_ser_verdad_cuando_hashArch_es_string_0(self):
        test = Blockchain()
        self.assertEqual(test.cadena[0].hashArch, "0")

    def test_bloqueGenesis_hashAnt_debe_ser_verdad_cuando_hashAnt_es_string_0(self):
        test = Blockchain()
        self.assertEqual(test.cadena[0].hashAnt, "0")

    def test_bloqueGenesis_hashBlq_debe_ser_verdad_cuando_hashBlq_es_igual_a_lo_que_devuelve_traeHashBloque(self):
        test = Blockchain()
        self.assertEqual("32448a9a2e0b20a10125aa5a1ebdb9eac8520b70bdea10450dbf0fd052f528a6", test.traeHashBloque(0))
    
if __name__ == '__main__':
    unittest.main()