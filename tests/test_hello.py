import unittest
from desoper import myfirstpypi
import pandas as pd



class Test_hello(unittest.TestCase):
    def test__working(self):
        ls1=pd.DataFrame(myfirstpypi.principal(5,9,0,30,400000))
        self.assertEqual(12,ls1.shape[0], True)
 
class Test_hello(unittest.TestCase):
    def test__working(self):
        ls2=myfirstpypi.principal(6,9,0,30,400000)
        self.assertEqual(142,ls2.shape[0], True)
       


if __name__ == '__main__':
    unittest.main()
#n estudiaa esta parte,clas test evalua la funcion
