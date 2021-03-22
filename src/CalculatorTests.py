import unittest
from Calculator import Calculator


class MyTestCase(unittest.TestCase):

    def test_instantiate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)


    def test_sub_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.subtract(2,2), 0)
        self.assertEqual(calculator.result, 0)

    def test_mul_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.multiply(2,2), 4)
        self.assertEqual(calculator.result, 4)

    def test_div_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.divide(2,4), 2)
        self.assertEqual(calculator.result, 2)

    def test_sqrt_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.sqrt(4)
        self.assertEqual(calculator.result, 2)

    def test_square_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.sqr(3), 9)
        self.assertEqual(calculator.result, 9)

if __name__ == '__main__':
    unittest.main()