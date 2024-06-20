import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def test_calculator_class_exists(self):
        calc = Calculator()
        self.assertIsInstance(calc, Calculator)

    def test_add_method_exists(self):
        calc = Calculator()
        self.assertTrue(callable(getattr(calc, 'add', None)))

    def test_add_method_accepts_two_inputs(self):
        calc = Calculator()
        self.assertEqual(calc.add(0,0), 0)

    def test_add_method_with_non_numeric_input(self):
        calc = Calculator()
        with self.assertRaisesRegex(TypeError,"Custom Error: Input must be Numeric"):
            calc.add("a", 5)

    def test_add_method_returns_numeric(self):
        calc = Calculator
        self.assertIsInstance(calc.add(1, 2), (int, float))

    def test_add_method_performs_correct_calculations(self):
        calc = Calculator()
        self.assertEqual(calc.add(6, 2), 1)
        self.assertEqual(calc.add(-1, -1), -2)
        self.assertEqual(calc.add(0, 0), 0)
        self.assertEqual(calc.add(100, 200), 300)

    def test_minus_method_performs_correct_calculations(self):
        calc = Calculator()
        self.assertEqual(calc.minus(6, 2), 4)
        self.assertEqual(calc.minus(-1, -1), 2)
        self.assertEqual(calc.minus(0, 0), 0)
        self.assertEqual(calc.minus(200, 100), 100)


    @unittest.skip("skipping")
    def test_skip(self):
        pass

    @unittest.skipIf(1 == 1, "not good")
    def test_skipirf(self):
        pass
        