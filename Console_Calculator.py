from my_functions import Validation
# from methods import *

v = Validation()


# Method where user inputs data and other methods are called to make the proper validations
def calculate():
    n1 = None
    n2 = None
    op = None
    calculate_again = True

    print("-Type two values to work with, then use one of these operators: '+', '-', '*', '/'")
    print("-You're able to finish the program at any stage by typing 'exit'")

    name = v.greet("Omar")
    while name is None:
        name = input("You need to type your name: ")
        name = v.greet(name)
        if name is False:
            quit()

    while n1 is None:
        n1 = input('Type the first value: ')
        if n1 == "exit":
            quit()
        n1 = v.check_user_input(n1)

    while n2 is None:
        n2 = input('Type the second value: ')
        if n2 == "exit":
            quit()
        n2 = v.check_user_input(n2)

    while op is None:
        x = input('Type the operator symbol: ')
        if x == "exit":
            quit()
        op = v.operator(x)

    # this does the calculation
    result = v.do_math(n1, n2, op)
    print("{} {} {} = {}".format(round(n1, 3), x, round(n2, 3), str(result)))

    while calculate_again is True:
        calculate_again = input('''
    # Do you want to calculate again?
    # Please type Y for YES or N for NO.
    #         ''')
        if calculate_again.upper() == 'Y':
            calculate_again = False
        elif calculate_again.upper() == 'N':
            print('See you later!')
            quit()
        else:
            calculate_again = True

    calculate()


calculate()
