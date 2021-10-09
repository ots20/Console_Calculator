import unittest
from my_functions import Validation


class NameValidator(unittest.TestCase):
    def setUp(self):
        self.validation = Validation()
        self.valid_name = "Omar Teresa Sanchez"
        self.invalid_name_none = None

    def test_valid_name(self):
        self.assertTrue(self.validation.greet(self.valid_name))

    def test_invalid_name(self):
        self.assertIsNone(self.validation.greet(self.invalid_name_none))


class InputValue(unittest.TestCase):
    def setUp(self):
        self.validation = Validation()
        self.valid_int = 2
        self.valid_float2 = "10000000000000009.1234567890"
        self.invalid4 = "+"

    def test_valid_int(self):
        self.assertEqual(self.validation.check_user_input(self.valid_int), 2)

    def test_valid_float(self):
        self.assertEqual(self.validation.check_user_input(self.valid_float2), float(self.valid_float2))

    def test_invalid_input(self):
        self.assertIsNone(self.validation.check_user_input(self.invalid4))


class OperatorValidator(unittest.TestCase):

    def setUp(self):
        self.validation = Validation()
        self.valid_sum = "+"
        self.valid_subtraction = "-"
        self.valid_multiplication = "*"
        self.valid_division = "/"
        self.not_valid = "%"

    def test_valid_operators(self):
        self.assertIsNotNone(self.validation.operator(self.valid_sum))
        self.assertIsNotNone(self.validation.operator(self.valid_subtraction))
        self.assertIsNotNone(self.validation.operator(self.valid_multiplication))
        self.assertIsNotNone(self.validation.operator(self.valid_division))

    def test_invalid_operator(self):
        self.assertIsNone(self.validation.operator(self.not_valid))


class MathOperation(unittest.TestCase):

    def setUp(self):
        # built in method for setting the operation
        import operator
        op_validation = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }
        self.validation = Validation()
        # self.integer = 0
        self.integer2 = 1
        self.integer3 = -4
        self.sum = operator.add
        self.sub = operator.sub
        self.mul = operator.mul
        self.div = operator.truediv

    def test_sum(self):
        self.assertEqual(self.validation.do_math(self.integer2, self.integer3, self.sum), self.sum(self.integer2, self.integer3))

    def test_subtraction(self):
        self.assertEqual(self.validation.do_math(self.integer3, self.integer2, self.sub), self.sub(self.integer3, self.integer2))

    def test_multiplication(self):
        self.assertEqual(self.validation.do_math(self.integer3, self.integer2, self.mul), self.mul(self.integer3, self.integer2))

    def test_division(self):
        self.assertEqual(self.validation.do_math(self.integer3, self.integer2, self.div), self.div(self.integer3, self.integer2))

        # with self.assertRaises(ZeroDivisionError) as zd:
        #     self.assertEqual(self.validation.do_math(self.integer2, self.integer, self.div),
        #                      self.div(self.integer2, self.integer))
        # self.assertEqual(zd.exception.code, 1)


if __name__ == "__main__":
    unittest.main()
