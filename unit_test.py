import unittest
from my_functions import Validation


class NameValidator(unittest.TestCase):
    def setUp(self):
        self.validation = Validation()
        self.valid_name = "Omar Teresa Sanchez"
        self.valid_name_space = "     Omar    "
        self.valid_name_number = "222"
        self.valid_name_alpha = "0M49%$+"
        self.invalid_name_none = None
        self.invalid_name_blank = ""
        self.invalid_name_space = "      "
        self.exit = "exit"

    def test_valid_name(self):
        self.assertTrue(self.validation.greet(self.valid_name))
        self.assertTrue(self.validation.greet(self.valid_name_space))
        self.assertTrue(self.validation.greet(self.valid_name_number))
        self.assertTrue(self.validation.greet(self.valid_name_alpha))

    def test_invalid_name(self):
        self.assertIsNone(self.validation.greet(self.invalid_name_none))
        self.assertIsNone(self.validation.greet(self.invalid_name_blank))
        self.assertIsNone(self.validation.greet(self.invalid_name_space))
        self.assertFalse(self.validation.greet(self.exit))


class InputValue(unittest.TestCase):
    def setUp(self):
        self.validation = Validation()
        self.valid_int = 2
        self.valid_int2 = 1000000
        self.valid_int3 = -50
        self.valid_int4 = 0
        # Floats are sent in a string but returned by the method as float
        self.valid_float = "3.5"
        self.valid_float2 = "10000000000000009.1234567890"
        self.valid_float3 = "-.5"
        self.invalid1 = "Test"
        self.invalid2 = ""
        self.invalid3 = " "
        self.invalid4 = "+"

    def test_valid_int(self):
        self.assertEqual(self.validation.check_user_input(self.valid_int), 2)
        self.assertEqual(self.validation.check_user_input(self.valid_int2), 1000000)
        self.assertEqual(self.validation.check_user_input(self.valid_int3), self.valid_int3)
        self.assertEqual(self.validation.check_user_input(self.valid_int4), self.valid_int4)

    def test_valid_float(self):
        self.assertEqual(self.validation.check_user_input(self.valid_float), float(self.valid_float))
        self.assertEqual(self.validation.check_user_input(self.valid_float2), float(self.valid_float2))
        self.assertEqual(self.validation.check_user_input(self.valid_float3), float(self.valid_float3))

    def test_invalid_input(self):
        self.assertIsNone(self.validation.check_user_input(self.invalid1))
        self.assertIsNone(self.validation.check_user_input(self.invalid2))
        self.assertIsNone(self.validation.check_user_input(self.invalid3))
        self.assertIsNone(self.validation.check_user_input(self.invalid4))


class OperatorValidator(unittest.TestCase):

    def setUp(self):
        self.validation = Validation()
        self.valid_sum = "+"
        self.valid_subtraction = "-"
        self.valid_multiplication = "*"
        self.valid_division = "/"
        self.not_valid = "%"
        self.not_valid2 = " "
        self.not_valid3 = "Test"
        self.not_valid4 = 2

    def test_valid_operators(self):
        self.assertIsNotNone(self.validation.operator(self.valid_sum))
        self.assertIsNotNone(self.validation.operator(self.valid_subtraction))
        self.assertIsNotNone(self.validation.operator(self.valid_multiplication))
        self.assertIsNotNone(self.validation.operator(self.valid_division))

    def test_invalid_operator(self):
        self.assertIsNone(self.validation.operator(self.not_valid))
        self.assertIsNone(self.validation.operator(self.not_valid2))
        self.assertIsNone(self.validation.operator(self.not_valid3))
        self.assertIsNone(self.validation.operator(self.not_valid4))


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
        self.integer = 0
        self.integer2 = 1
        self.integer3 = -4
        self.integer4 = 999999
        self.float = 0.5
        self.float2 = -0.5
        self.float3 = 100.234
        self.sum = operator.add
        self.sub = operator.sub
        self.mul = operator.mul
        self.div = operator.truediv

    def test_sum(self):
        result = self.validation.do_math(self.float2, self.float2, self.sum)
        self.assertEqual(self.validation.do_math(self.integer, self.integer2, self.sum), 1)
        self.assertEqual(self.validation.do_math(self.integer, self.integer, self.sum), 0)
        self.assertEqual(self.validation.do_math(self.integer2, self.integer3, self.sum), self.sum(self.integer2, self.integer3))
        self.assertEqual(self.validation.do_math(self.integer4, self.integer2, self.sum), self.sum(self.integer4, self.integer2))
        self.assertEqual(self.validation.do_math(self.integer3, self.integer3, self.sum), self.sum(self.integer3, self.integer3))
        self.assertEqual(self.validation.do_math(self.integer2, self.float, self.sum), self.sum(self.integer2, self.float))
        self.assertEqual(self.validation.do_math(self.integer2, self.float2, self.sum), self.sum(self.integer2, self.float2))
        self.assertEqual(self.validation.do_math(self.integer3, self.float, self.sum), self.sum(self.integer3, self.float))
        self.assertEqual(self.validation.do_math(self.integer3, self.float2, self.sum), self.sum(self.integer3, self.float2))
        self.assertEqual(self.validation.do_math(self.integer4, self.float3, self.sum), self.sum(self.integer4, self.float3))
        self.assertEqual(self.validation.do_math(self.float, self.float, self.sum), self.sum(self.float, self.float))
        self.assertEqual(self.validation.do_math(self.float2, self.float, self.sum), self.sum(self.float2, self.float))
        self.assertEqual(self.validation.do_math(self.float2, self.float2, self.sum), self.sum(self.float2, self.float2))

    def test_subtraction(self):
        result = self.validation.do_math(self.integer3, self.integer4, self.sub)
        self.assertEqual(self.validation.do_math(self.integer2, self.integer, self.sub), self.sub(self.integer2, self.integer))
        self.assertEqual(self.validation.do_math(self.integer3, self.integer2, self.sub), self.sub(self.integer3, self.integer2))
        self.assertEqual(self.validation.do_math(self.integer3, self.integer3, self.sub), self.sub(self.integer3, self.integer3))
        self.assertEqual(self.validation.do_math(self.integer3, self.integer4, self.sub), self.sub(self.integer3, self.integer4))
        self.assertEqual(self.validation.do_math(self.integer4, self.integer3, self.sub), self.sub(self.integer4, self.integer3))
        self.assertEqual(self.validation.do_math(self.integer4, self.float, self.sub), self.sub(self.integer4, self.float))
        self.assertEqual(self.validation.do_math(self.float, self.float2, self.sub), self.sub(self.float, self.float2))
        self.assertEqual(self.validation.do_math(self.float, self.float2, self.sub), self.sub(self.float, self.float2))
        self.assertEqual(self.validation.do_math(self.float2, self.float3, self.sub), self.sub(self.float2, self.float3))

    def test_multiplication(self):
        self.assertEqual(self.validation.do_math(self.integer2, self.integer, self.mul), self.mul(self.integer2, self.integer))
        self.assertEqual(self.validation.do_math(self.integer3, self.integer2, self.mul), self.mul(self.integer3, self.integer2))
        self.assertEqual(self.validation.do_math(self.integer3, self.integer3, self.mul), self.mul(self.integer3, self.integer3))
        self.assertEqual(self.validation.do_math(self.integer3, self.integer4, self.mul), self.mul(self.integer3, self.integer4))
        self.assertEqual(self.validation.do_math(self.integer4, self.integer3, self.mul), self.mul(self.integer4, self.integer3))
        self.assertEqual(self.validation.do_math(self.integer4, self.float, self.mul), self.mul(self.integer4, self.float))
        self.assertEqual(self.validation.do_math(self.float, self.float2, self.mul), self.mul(self.float, self.float2))
        self.assertEqual(self.validation.do_math(self.float, self.float2, self.mul), self.mul(self.float, self.float2))
        self.assertEqual(self.validation.do_math(self.float2, self.float3, self.mul), self.mul(self.float2, self.float3))

    def test_division(self):
        result = self.validation.do_math(self.float2, self.float3, self.div)
        self.assertEqual(self.validation.do_math(self.integer2, self.integer2, self.div), self.div(self.integer2, self.integer2))
        self.assertEqual(self.validation.do_math(self.integer3, self.integer2, self.div), self.div(self.integer3, self.integer2))
        self.assertEqual(self.validation.do_math(self.integer3, self.integer3, self.div), self.div(self.integer3, self.integer3))
        # self.assertEqual(self.validation.do_math(self.integer3, self.integer4, self.div), self.div(self.integer3, self.integer4))
        self.assertEqual(self.validation.do_math(self.integer4, self.integer3, self.div), self.div(self.integer4, self.integer3))
        self.assertEqual(self.validation.do_math(self.integer4, self.float, self.div), self.div(self.integer4, self.float))
        self.assertEqual(self.validation.do_math(self.float, self.float2, self.div), self.div(self.float, self.float2))
        self.assertEqual(self.validation.do_math(self.float, self.float2, self.div), self.div(self.float, self.float2))
        self.assertAlmostEqual(self.validation.do_math(self.float2, self.float3, self.div), self.div(self.float2, self.float3), places=3)

        with self.assertRaises(ZeroDivisionError) as zd:
            self.assertEqual(self.validation.do_math(self.integer2, self.integer, self.div),
                             self.div(self.integer2, self.integer))
        self.assertEqual(zd.exception.code, 1)


if __name__ == "__main__":
    unittest.main()
