import unittest
import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate("1 1 +")
        self.assertEqual(2, result)
    def test_sub(self):
        result = rpn.calculate("5 3 -")
        self.assertEqual(2, result)
    def test_exp(self):
        result = rpn.calculate("5 2 ^")
        self.assertEqual(25, result)
    def test_mult(self):
        result = rpn.calculate("5 5 *")
        self.assertEqual(25, result)
   # def test_div(self):
   #     result = rpn.calculate("10 5 /")
   #     self.assertEqual(2, result)    
    def test_badinput(self):
        with self.assertRaises(TypeError):
            rpn.calculate("1 2 3 +")
         
        
