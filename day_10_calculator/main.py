logo = """ _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \\     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \\_|  | || |    / /\\ \\    | || |    | |       | || |  / .'   \\_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \\   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \\ '.___.'\\  | || | _/ /    \\ \\_ | || |   _| |__/ |  | || |  \\ '.___.'\\  | |
| | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|"""


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero"
    return num1 / num2


def calc(num1, num2, operand):
    if operand == "+":
        return add(num1, num2)
    elif operand == "-":
        return subtract(num1, num2)
    elif operand == "*":
        return multiply(num1, num2)
    elif operand == "/":
        return divide(num1, num2)
    else:
        return "Invalid operand"


def calculator(continue_with_result, result):
    if continue_with_result == "y":
        num1 = result
    else:
        num1 = float(input("What's the first number? "))
    operand = input("Pick an operation: +\n-\n*\n/\n")
    num2 = float(input("What's the second number? "))
    result = calc(num1, num2, operand)
    return {
        "num1": num1,
        "num2": num2,
        "operand": operand,
        "result": result
    }


is_calc_on = True

print(logo)
answer = calculator("n", 0)

print(f"{answer['num1']} {answer['operand']} {answer['num2']} = {answer['result']}")

while is_calc_on:
    user_choice = input(f"\nType 'y' to continue calculating with {answer['result']}, "
                        f"type 'n' to start a new calculation, or 'x' to exit: ")
    if user_choice == "x":
        is_calc_on = False
        print("Goodbye!")
    else:
        answer = calculator(user_choice, answer["result"])
        print(f"{answer['num1']} {answer['operand']} {answer['num2']} = {answer['result']}")
