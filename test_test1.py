import unittest


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b != 0:
        return a / b
    else:
        raise ValueError("Division by zero is not allowed")


class TestArithmeticFunctions(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(addition(3, 5), 8)
        self.assertEqual(addition(-2, 2), 0)
        self.assertEqual(addition(0, 0), 0)

    def test_subtraction(self):
        self.assertEqual(subtraction(8, 3), 5)
        self.assertEqual(subtraction(5, 5), 0)
        self.assertEqual(subtraction(0, 0), 0)

    def test_multiplication(self):
        self.assertEqual(multiplication(4, 6), 24)
        self.assertEqual(multiplication(-3, 5), -15)
        self.assertEqual(multiplication(0, 7), 0)

    def test_division(self):
        self.assertEqual(division(10, 2), 5)
        self.assertEqual(division(-15, 3), -5)

        with self.assertRaises(ValueError):
            division(8, 0)  # Division by zero should raise ValueError

ahvdghasvfjahfbaehjfe
if __name__ == '__main__':
    unittest.main()
