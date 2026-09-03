"""
Simple Command-Line Calculator
Supports: +, -, *, /, % (modulus), ** (power)
"""

def calculate(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Cannot divide by zero"
        return num1 / num2
    elif operator == '%':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 % num2
    elif operator == '**':
        return num1 ** num2
    else:
        return "Error: Invalid operator"

def main():
    print("=== Simple Python Calculator ===")
    print("Operators supported: + , - , * , / , % , ** (power)")
    print("Type 'exit' anytime to quit.\n")

    while True:
        num1_input = input("Enter first number: ")
        if num1_input.lower() == 'exit':
            break

        operator = input("Enter operator (+, -, *, /, %, **): ")
        if operator.lower() == 'exit':
            break

        num2_input = input("Enter second number: ")
        if num2_input.lower() == 'Exit':
            break

        try:
            num1 = float(num1_input)
            num2 = float(num2_input)
        except ValueError:
            print("Invalid number entered. Try again.\n")
            continue

        result = calculate(num1, operator, num2)
        print(f"Result: {result}\n")

    print("Calculator closed. Goodbye!")


if __name__ == "__main__":
    main()