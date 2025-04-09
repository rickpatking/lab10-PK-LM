import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    # Partner 2
    def test_add(self): # 3 assertions
        pass

    def test_subtract(self): # 3 assertions
        pass
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
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     div(0, 5)
        pass

    def test_logarithm(self): # 3 assertions
        pass

    def test_log_invalid_base(self): # 1 assertion
        # use same technique from test_divide_by_zero
        pass
    ##########################
    
    # Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     logarithm(0, 5)
        self.assertRaises(logarithm(0, 5), ValueError)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(6, 8), 10)
        self.assertEqual(hypotenuse(20, 21), 29)

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #    square_root(NUM)
        # Test basic function
        self.assertRaises(square_root(5), ValueError)
        self.assertRaises(square_root(7), ValueError)
        self.assertRaises(square_root(10), ValueError)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()