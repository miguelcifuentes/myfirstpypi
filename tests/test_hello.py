import unittest
from desoper import myfirstpypi



class Test_hello(unittest.TestCase):
    def test__working(self):
        lsl=myfirstpypi.principal(5,9,0,30,400000)
        self.assertEqual(11,lsl.shape[0], True)
 
class Test_hello(unittest.TestCase):
    def test__working(self):
        lsl=myfirstpypi.principal(5,9,0,30,400000)
        self.assertEqual(11,lsl.shape[0], True)
       


if __name__ == '__main__':
    unittest.main()
#n estudiaa esta parte,clas test evalua la funcion
