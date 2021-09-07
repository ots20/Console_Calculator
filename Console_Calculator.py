from methods import Validation
# from methods import *

v = Validation()


# Method where user inputs data and other methods are called to make the proper validations
def calculate():
    n1 = False
    n2 = False
    op = None
    calc_again = False

    print("-Type two values to work with, then use one of these operators: '+', '-', '*', '/'")
    print("-You're able to finish the program at any stage by typing 'exit'")

    name = v.greet("Omar")
    while name is None:
        name = input("You need to type your name: ")
        name = v.greet(name)
        if name is False:
            quit()

    # if not v.greet("Omar"):
    #     quit()

    while not n1:
        n1 = input('Type the first value: ')
        if v.exit_program(n1):
            quit()
        n1 = v.check_user_input(n1)

    while not n2:
        n2 = input('Type the second value: ')
        if v.exit_program(n2):
            quit()
        n2 = v.check_user_input(n2)

    while op is None:
        x = input('Type the operator symbol: ')
        if v.exit_program(x):
            quit()
        op = v.op_validator(x)

    # this does the calculation
    v.do_math(n1, n2, op, x)

    while not calc_again:
        calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
        ''')
        if v.exit_program(calc_again):
            quit()
        calc_again = v.again(calc_again)
        if calc_again is None:
            quit()

    calculate()


calculate()
