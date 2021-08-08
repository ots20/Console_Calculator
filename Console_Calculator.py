# Function to validate if the user inputs a number
def check_user_input(string):
    while True:
        num = input("Type the {} value: ".format(string))
        exit_program(num)
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


# Validates the input entered by the user to whether or not to end the program on any stage
def exit_program(value):
    if value == "exit":
        print("Terminating program, bye")
        quit()
    else:
        return


# Function to greet only the 1st time the calculator is run
def greet():
    name = input('Hello, what is your name?: ')
    while len(name) < 1:
        name = input('You need to type your name: ')
    else:
        exit_program(name)
        print("Hello " + name)
        calculate()



def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        # print("Hello again!")
        calculate()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        again()


def calculate():
    # Validate the operator typed by the user is within the options
    import operator

    opValidation = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }

    # value1 = input('Type the first value: ')
    # print("Type the first value")
    first = "first"
    value1 = check_user_input(first)


    # print("Type the second value")
    second = "second"
    value2 = check_user_input(second)

    x = input('Type the operation to perform: ')
    exit_program(x)

    # validating the operator entered
    op = opValidation.get(x)

    while op is None:
        x = input("Unknown operator, enter it again: ")
        op = opValidation.get(x)
    else:
        op = opValidation.get(x)
        result = op(float(value1), float(value2))

    print("{} {} {} = ".format(value1, x, value2))
    print(str(result))
    again()


greet()
