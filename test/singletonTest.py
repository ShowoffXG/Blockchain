import unittest
import os
import sys
ruta = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(ruta)
from src.blockchain import Blockchain

class SingletonTest(unittest.TestCase):
    def test_Singleton_should_to_be_true_when_Singleton_is_created(self):
            test1 = Blockchain()
            test2 = Blockchain()
            self.assertTrue(id(test1) == id(test2), "Test Singleton don't works")

if __name__ == '__main__':
    unittest.main()