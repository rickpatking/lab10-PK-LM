# https://github.com/rickpatking/lab10-PK-LM.git
# Partner 1: Patrick King
# Partner 2: Logan Mears

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    # Partner 2
    def test_add(self): # 3 assertions
        expected = 7
        actual = add(3, 4)
        self.assertEqual(expected, actual)
        expected = -3
        actual = add(-3, 0)
        self.assertEqual(expected, actual)
        expected = 17
        actual = add(9, 8)
        self.assertEqual(expected, actual)

    def test_subtract(self): # 3 assertions
        expected = -1
        actual = subtract(3, 4)
        self.assertEqual(expected, actual)
        expected = 4
        actual = subtract(8, 4)
        self.assertEqual(expected, actual)
        expected = 0
        actual = subtract(4, 4)
        self.assertEqual(expected, actual)
    ##########################

    # Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(3, 3), 9)
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(-3, 3), -9)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(3, 3), 1)
        self.assertEqual(div(3, 6), 2)
        self.assertEqual(div(-3, 3), -1)
    ##########################

    # Partner 2
    def test_divide_by_zero(self): # 1 assertion
        # call division function inside, example:
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        expected = 2
        actual = logarithm(10, 100)
        self.assertEqual(expected, actual)
        expected = 2
        actual = logarithm(2, 4)
        self.assertEqual(expected, actual)
        expected = 2
        actual = logarithm(3, 9)
        self.assertEqual(expected, actual)

    def test_log_invalid_base(self): # 1 assertion
        # use same technique from test_divide_by_zero
        with self.assertRaises(ValueError):
            logarithm(1, 5)
    ##########################
    
    # Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     logarithm(0, 5)
        self.assertRaises(logarithm(1, 5), ValueError)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(6, 8), 10)
        self.assertEqual(hypotenuse(20, 21), 29)

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #    square_root(NUM)
        # Test basic function
        self.assertRaises(square_root(9), ValueError)
        self.assertRaises(square_root(27), ValueError)
        self.assertRaises(square_root(4), ValueError)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()