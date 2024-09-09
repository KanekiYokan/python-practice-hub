import math
import sys


class Calculator:
    # Constructor - Initializes the Calculator and welcomes the user.
    def __init__(self):
        print("Welcome to the shell calculator!")

    # Core operation methods to perform arithmetic operations.
    def add(self, x, y): # sum
        return x + y

    def subtract(self, x, y): # subtraction
        return x - y

    def multiply(self, x, y): # multiplication
        return x * y

    def divide(self, x, y): # division
        if y == 0:
            return "Error! Division by zero."
        return x / y

    def power(self, x, y): # exponentiation
        return x ** y

    def root(self, x): # square root
        if x < 0:
            return "Error! Cannot take square root of a negative number."
        return math.sqrt(x)

    # Helper method to get a valid number from the user.
    # This loops until the user enters a valid numeric value.
    def get_valid_number(self, prompt):
        while True:
            try:
                # Get user input and try to convert it to a float
                value = float(input(prompt))
                return value
            except ValueError:
                # If the input is not a valid number, print an error and prompt again
                print("Invalid input! Please enter a numeric value.")

    # Method to retrieve numbers for the chosen operation.
    def get_nums(self, operation):

        # For binary operations (+, -, *, /, ^), two values are required.
        if operation in ["+", "-", "*", "/", "^"]:
            num1 = self.get_valid_number("Enter Value X: ")
            num2 = self.get_valid_number("Enter Value Y: ")
            return num1,num2

        # For square root (sqrt), only one value is needed.
        elif operation == "sqrt":
            num1 = self.get_valid_number("Enter Value: ")
            return num1

    # Method to perform the chosen operation based on the user input.
    def get_opertation(self, operation, num1, num2):
        if operation == '+':
            return self.add(num1,num2)

        elif operation == '-':
            return self.subtract(num1,num2)

        elif operation == '*':
            return self.multiply(num1,num2)

        elif operation == '/':
            return self.divide(num1,num2)

        elif operation == '^':
            return self.power(num1,num2)

        elif operation == 'sqrt':
            return self.root(num1)

        else:
            return "Invalid Operation!"

def main():
    calc = Calculator()

    result = 0 # Initialize result variable to hold calculation results.
    while True:

        # Prompt the user to enter an operation or exit the program.
        operation = input("\nEnter operation (+, -, *, /, ^, sqrt) or 'exit' to quit: ")

        # Exit the program if the user types 'exit'.
        if operation.lower() == "exit":
            sys.exit("You entered the 'exit' command, bye!")

        # Operation phase
        elif operation in ["+", "-", "*", "/", "^"]:
            num1, num2 = calc.get_nums(operation)
            result = calc.get_opertation(operation, num1, num2)

        elif operation.lower() == "sqrt":
            num1 = calc.get_nums(operation)
            result = calc.get_opertation(operation, num1= num1, num2 = None)

        # Handling Invalid Operations
        else:
            print("Invalid Operation!")
            print("Please Try Again...")
            continue

        # Output Result
        print(f"Your result: {result}")

main()