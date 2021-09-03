from methods import Validation
# from methods import *

v = Validation()


# Method where user inputs data and other methods are called to make the proper validations
def calculate():
    n1 = False
    n2 = False
    op = None
    calc_again = False

    v.greet("Omar")

    while not n1:
        n1 = input('Type the first value: ')
        v.exit_program(n1)
        n1 = v.check_user_input(n1)

    while not n2:
        n2 = input('Type the second value: ')
        v.exit_program(n2)
        n2 = v.check_user_input(n2)

    while op is None:
        x = input('Type the operator symbol: ')
        v.exit_program(x)
        op = v.op_validator(x)

    # this does the calculation
    v.do_math(n1, n2, op, x)

    while not calc_again:
        calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
        ''')
        calc_again = v.again(calc_again)

    calculate()


calculate()
