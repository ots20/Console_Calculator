# Fcuntion to validate if the user inputs a number
def check_user_input(string):
    while True:
        num = input("Type the {} value: ".format(string))
        try:
            value = int(num)
            return value
        except ValueError:
            # print("Not a number!")
            try:
                value = float(num)
                return value
            except ValueError:
                print("Not a number!")




def calculate():
    # Validate the operator typed by the user is within the options
    import operator

    opValidation = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }

    name = input('Hello, what is your name?: ')

    while len(name) < 1:
        name = input('You need to type your name: ')
    else:
        print("Hello " + name)

    # value1 = input('Type the first value: ')
    # print("Type the first value")
    first = "first"
    value1 = check_user_input(first)

    # print("Type the second value")
    second = "second"
    value2 = check_user_input(second)

    x = input('Type the operation to perform: ')

    # validating the operator entered
    op = opValidation.get(x)

    while op is None:
        x = input("Unknown operator, enter it again: ")
        op = opValidation.get(x)
    else:
        op = opValidation.get(x)
        result = op(float(value1), float(value2))

    print("result is: " + str(result))
    again()



def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        again()


calculate()

