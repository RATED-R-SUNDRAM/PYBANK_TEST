from pybank.transactions import add, substract, area 
import unittest 


class test_area(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(area(1), 3.141592653589793, places=5)
        self.assertAlmostEqual(area(2), 12.566370614359172, places=5)   

class test_add(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1,2), 3)
        self.assertEqual(add(2,2), 4)
        self.assertEqual(add(0,2), 2)
        self.assertEqual(add(0,0), 0)
        self.assertEqual(add(-1,2), 1)

class test_substract(unittest.TestCase):
    def test_substract(self):
        self.assertEqual(substract(1,2), -1)
        self.assertEqual(substract(2,2), 0)
        self.assertEqual(substract(0,2), -2)
        self.assertEqual(substract(0,0), 0)
        self.assertEqual(substract(-1,2), -3)