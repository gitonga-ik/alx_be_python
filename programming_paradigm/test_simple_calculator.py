import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        # Add more assertions to thoroughly test the add method.
        self.assertEqual(self.calc.add(4, 6), 10)
        self.assertEqual(self.calc.add(8, 9), 17)
# Remember to write additional test methods for subtract, multiply, and divide.

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(6, 3), 3)
        self.assertEqual(self.calc.subtract(10, 3), 7)
        self.assertEqual(self.calc.subtract(4, -2), 6)
        self.assertEqual(self.calc.subtract(0, 3), -3)
        
    def test_multilplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(5, 2), 10)
        self.assertEqual(self.calc.multiply(4, 2), 8)
        self.assertEqual(self.calc.multiply(7, -1), -7)
        self.assertEqual(self.calc.multiply(0, 3), 0)

    def test_division(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.divide(5, 0), None)
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(7, 7), 1)
        self.assertEqual(self.calc.divide(5, 10), 0.5)  