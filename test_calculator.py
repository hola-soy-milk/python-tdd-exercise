import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_addition(self):
        result = self.calc.add(3, 5)
        self.assertEqual(result, 8)

    def test_subtraction(self):
        result = self.calc.subtract(10, 3)
        self.assertEqual(result, 7)

    def test_multiplication(self):
        result = self.calc.multiply(4, 6)
        self.assertEqual(result, 24)

if __name__ == '__main__':
    unittest.main()