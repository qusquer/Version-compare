import unittest
from ver_compar import ver_compare

class TestVerCompare(unittest.TestCase):

    def test_accuracy(self):
        self.assertEqual(ver_compare('1.2', '1.3'), -1)
        self.assertEqual(ver_compare('1.3', '1.2'), 1)
        self.assertEqual(ver_compare('1.2', '1.2'), 0)
        self.assertEqual(ver_compare('1.0002.0.1', '1.3'), -1)
        self.assertEqual(ver_compare('1.020.00.01', '1.20.0.1'), 0)
        self.assertEqual(ver_compare('3462', '1.3'), 1)
        self.assertEqual(ver_compare('12423534.4352.12.0097.42.07.0', '5463.007.3.1'), 1)
    
    def test_values(self):
        self.assertRaises(ValueError, ver_compare, ('0.32f.0', '3.324.5.6'))
        self.assertRaises(ValueError, ver_compare, ('0.32f.0', '3.yt4.5.l'))
        self.assertRaises(ValueError, ver_compare, ('5456.46.4', 'fgf'))
        self.assertRaises(ValueError, ver_compare, ('0.32o.0', '3.324.5.6.o'))

    def test_types(self):
        self.assertRaises(TypeError, ver_compare, (32, '3.324.5.6'))
        self.assertRaises(TypeError, ver_compare, ('0.32.0', [3, 324, 5, 6]))
        self.assertRaises(TypeError, ver_compare, (True, '3.324.5.6'))
        self.assertRaises(TypeError, ver_compare, ((5 + 2j), '3.324.5.6'))
        
if __name__ == '__name__':
    unittest.main()