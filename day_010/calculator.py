from calculator_art import logo
print(logo)

def add(n1, n2):
    """A function that takes two inputs and add 'em together"""
    return n1 + n2

def subtract(n1, n2):
    """A function that takes two inputs and subtract 'em together"""
    return n1 - n2

def multiply(n1, n2):
    """A function that takes two inputs and multiply 'em together"""
    return n1 * n2

def divide(n1, n2):
    """A function that takes two inputs and multiply 'em together"""
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    num1 = float(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)

    operation_symbol = input("Pick an operation from line above: ")

    num2 = float(input("What's the second number?: "))

    is_continue = True

    while is_continue == True:
        calc_function = operations[operation_symbol]
        answer = calc_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} is {answer}")

        continue_calc = input(f"Type 'y' to continue calculating with {answer} or 'n' to start a new calculation.: ")

        if continue_calc == "y":
            num1 = answer
            operation_symbol = input("Type an operation: ")
            num2  = float(input("What's the next number?: "))
            is_continue = True
        elif continue_calc == "n":
            is_continue = False
            calculator()

calculator()
            