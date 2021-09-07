import unittest
from methods import Validation


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


class ExitValidator(unittest.TestCase):

    def setUp(self):
        self.validation = Validation()
        self.exit_valid = "exit"
        self.exit_invalid = "exits"
        self.exit_invalid_2 = " "
        self.exit_invalid_3 = 2

    def test_exit(self):
        self.assertTrue(self.validation.exit_program(self.exit_valid))

    def test_exit_false(self):
        self.assertFalse(self.validation.exit_program(self.exit_invalid))
        self.assertFalse(self.validation.exit_program(self.exit_invalid_2))
        self.assertFalse(self.validation.exit_program(self.exit_invalid_3))


class OperatorValidator(unittest.TestCase):

    def setUp(self):
        self.validation = Validation()
        self.valid_sum = "+"
        self.valid_subtraction = "-"
        self.valid_multiplication = "*"
        self.valid_division = "/"
        self.not_valid = "%"

    def test_valid_operators(self):
        self.assertIsNotNone(self.validation.op_validator(self.valid_sum))
        self.assertIsNotNone(self.validation.op_validator(self.valid_subtraction))
        self.assertIsNotNone(self.validation.op_validator(self.valid_multiplication))
        self.assertIsNotNone(self.validation.op_validator(self.valid_division))

    def test_invalid_operator(self):
        validate = self.validation.op_validator(self.not_valid)
        self.assertIsNone(validate)


# class Greetings(unittest.TestCase):
#
#     # def setUp(self):
#
#
# class SumValues(unittest.TestCase):
#
#
# class TerminateProgram(unittest.TestCase):
#
#
# class Greetings(unittest.TestCase):

if __name__ == "__main__":
    unittest.main()
