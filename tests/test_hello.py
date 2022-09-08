import unittest
from desoper import  myfirstpypi



class Test_hello(unittest.TestCase):
    def test__working(self):
        self.assertEqual(myfirstpypi.hello(),
                         'Hello, World!', True)


if __name__ == '__main__':
    unittest.main()
#n estudiaa esta parte,clas test evalua la funcion
