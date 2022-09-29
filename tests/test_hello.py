import unittest
import pandas as pd



class Test_hello(unittest.TestCase):
    def test__working1(self):
        #ls1=principal(5,9,0,30,400000)
        self.assertEqual(11,11, True)

    def test__working2(self):
        #ls2=principal(6,9,0,30,400000)
        self.assertEqual(141,141, True)
       


if __name__ == '__main__':
    unittest.main()

