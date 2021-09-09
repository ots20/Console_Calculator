class Validation:

    # Function to validate if the user inputs a number
    def check_user_input(self, val):
        num = val
        while True:
            try:
                value = int(num)
                return value
            except ValueError:
                try:
                    value = float(num)
                    return value
                except ValueError:
                    print("Not a number!")
                    return None

    # Validates the inputs typed by the user to whether or not to end the program on any stage
    def exit_program(self, value):
        if value == "exit":
            print("Terminating program, bye")
            return True
            # quit()
        else:
            return False

    # Method to greet only the 1st time the calculator is run
    def greet(self, username):
        name = username
        # if name is None or len(name) < 1 or name.isspace():
        #     print("Hey, you need to type your name")
        #     name = input()
        if name is None or len(name) < 1 or name.isspace():
            return None
            # print("You need to type your name")
            # name = input()
        else:
            if self.exit_program(name):
                return False
            print("Hello " + name)
            return True

    # Method to validate the operator typed by the user is within the supported math operations
    def op_validator(self, op):
        import operator
        op_validation = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }
        operation = op_validation.get(op)
        if operation is None:
            print("Unknown operator! type it again")
            return operation
        else:
            return operation

    def do_math(self, val1, val2, op):
        result = op(float(val1), float(val2))
        result = round(result, 3)
        # print("{} {} {} = {}".format(round(val1, 3), string, round(val2, 3), str(result)))
        return result

    # Method to ask to make another calculation or to exit
    def again(self, choice):
        if choice.upper() == 'Y':
            # calculate()
            return True
        elif choice.upper() == 'N':
            print('See you later!')
            return None
        else:
            return False
