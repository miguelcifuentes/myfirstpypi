import unittest
from desoper import myfirstpypi
import pandas as pd



class Test_hello(unittest.TestCase):
    def test__working1(self):
        ls1=myfirstpypi.principal(5,9,0,30,400000).z.to_numpy()
        self.assertEqual(12,ls1.shape[0], True)

    def test__working2(self):
        ls2=myfirstpypi.principal(6,9,0,30,400000).z.to_numpy()
        self.assertEqual(142,ls2.shape[0], True)
       


if __name__ == '__main__':
    unittest.main()

