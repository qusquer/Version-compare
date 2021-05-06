import unittest
from ver_compar import ver_compare

class Test_VerCompare(unittest.TestCase):

    def test_accuracy(self):
        self.assertEqual(ver_compare('1.2', '1.3'), -1)
        self.assertEqual(ver_compare('1.3', '1.2'), 1)
        self.assertEqual(ver_compare('1.2', '1.2'), 0)
        self.assertEqual(ver_compare('1.0002.0.1', '1.3'), -1)
        self.assertEqual(ver_compare('1.020.00.01', '1.20.0.1'), 0)
        self.assertEqual(ver_compare('3462', '1.3'), 1)
        self.assertEqual(ver_compare('12423534.4352.12.0097.42.07.0', '5463.007.3.1'), 1)
    
    #def test_values(self):
        #self.assertRaises(ValueError,)
if __name__ == '__name__':
    unittest.main()