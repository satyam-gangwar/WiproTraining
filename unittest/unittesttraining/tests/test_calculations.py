import sys
import unittest

from src.calculations import add, sub, mul, div, ne


class TestCalculations(unittest.TestCase):

    def test_add(self):
        res = add(10, 5)
        self.assertEqual(15, res, msg='AdditionError')

    def test_sub(self):
        res = sub(10, 5)
        self.assertEqual(5,res,  msg='SubtractionError')

    def test_mul(self):
        res = mul(10, 5)
        self.assertEqual(50, res,  msg='MultiplicationError')

    def test_div(self):
        res = div(10, 5)
        self.assertEqual(2.0, res, msg='DivisionError')

    @unittest.skipIf(sys.version_info < (3, 13), reason='Not implemented yet')
    def test_ne(self):
        res = ne(10, 10)
        self.assertTrue(res, msg='NE')

    def test_dive(self):

           with self.assertRaises(ZeroDivisionError,msg='No Exception'):
               div(10, 0)

