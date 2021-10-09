class Validation:


    # Function to validate if the user inputs a number
    def check_user_input(self, val):
        num = val
        while True:
            # try:
            #     value = int(num)
            #     return value
            # except ValueError:
            try:
                value = float(num)
                return value
            except ValueError:
                print("Not a number!")
                return

    # Method to greet only the 1st time the calculator is run
    def greet(self, username):
        name = username
        if name is None or len(name) < 1 or name.isspace():
            return
            # return None
        else:
            if name == "exit":
                quit()
            print("Hello " + name)
            return True

    # Method to validate the operator typed by the user is within the supported math operations
    def operator(self, op):
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
        else:
            return operation

    def do_math(self, val1, val2, op):
        result = op(float(val1), float(val2))
        result = round(result, 3)
        return result
