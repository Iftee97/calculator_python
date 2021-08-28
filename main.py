# Calculator
from art import logo

print("\n")


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)

    num1 = float(input("\nWhat's the first number? "))

    print("\n")
    for operation in operations:
        print(operation)

    should_continue = True
    while should_continue:
        operation_symbol = input("\nPick an operation from above: ")
        num2 = float(input("\nWhat's the next number? "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"\n{num1} {operation_symbol} {num2} = {answer}")

        user_choice = input(
            f"\nType 'yes' to continue calculating with {answer} \nor, type 'new' to start a new calculation \nor, type 'exit' to stop calculation: ").lower()
        if user_choice == 'yes':
            num1 = answer
            continue
        elif user_choice == 'new':
            should_continue = False
            calculator()
        elif user_choice == 'exit':
            print("\nthat'll be all, goodbye!")
            should_continue = False
            # break


calculator()
