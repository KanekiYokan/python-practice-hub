
# Shell Calculator
___
## Project Goal

The goal of this project is to develop a basic command-line calculator that performs fundamental arithmetic operations (addition, subtraction, multiplication, and division) and more advanced operations such as exponentiation and square root. The calculator uses an Object-Oriented Programming (OOP) approach, which promotes code modularity, scalability, and maintainability.

This calculator accepts user input via the terminal and handles errors like division by zero and invalid inputs, ensuring a smooth user experience. The focus is on creating a simple yet robust solution that can be extended easily with more features in the future.

## Features

The calculator supports the following operations:

1. **Addition (`+`)** - Adds two numbers.
2. **Subtraction (`-`)** - Subtracts the second number from the first.
3. **Multiplication (`*`)** - Multiplies two numbers.
4. **Division (`/`)** - Divides the first number by the second (with division by zero handling).
5. **Exponentiation (`^`)** - Raises the first number to the power of the second.
6. **Square Root (`sqrt`)** - Computes the square root of a given number (with handling for negative inputs).

### Key Features:
- **Error Handling**: Ensures invalid inputs (e.g., non-numeric values or division by zero) are caught and handled gracefully.
- **Object-Oriented Approach**: The `Calculator` class encapsulates all operations, allowing easy maintenance and extension of the calculator’s functionality.
- **User-Friendly Prompts**: Provides clear guidance for user inputs, along with descriptive error messages.

## Solution Overview

The project uses Python's OOP principles to structure the solution. The `Calculator` class is the core component, encapsulating the calculator's functionality. This class contains methods for each operation and utility methods to handle user input and validation.

### Code Structure

1. **`Calculator` class**: Contains methods for:
   - Basic operations like `add()`, `subtract()`, `multiply()`, and `divide()`.
   - Advanced operations such as `power()` for exponentiation and `root()` for square root calculations.

2. **Error Handling**: 
   - The calculator ensures valid numeric input through the `get_valid_number()` method, which prompts the user repeatedly until a valid number is provided.
   - Handles division by zero in the `divide()` method and negative input in `root()` (square root).

3. **Main Logic**: The `main()` function handles the command-line interface, accepting user input to select the desired operation and returning the result after performing the calculation.

### Flow of Execution

1. The program starts by creating an instance of the `Calculator` class.
2. The user is prompted to enter an operation (`+`, `-`, `*`, `/`, `^`, or `sqrt`) or `exit` to quit.
3. Depending on the operation, the program asks for either one or two input values.
4. The selected operation is executed, and the result is displayed.
5. The user can continue performing calculations until they choose to exit the program.

### Example Usage

```shell
Welcome to the shell calculator!

Enter operation (+, -, *, /, ^, sqrt) or 'exit' to quit: +
Enter Value X: 10
Enter Value Y: 20
Your result: 30.0

Enter operation (+, -, *, /, ^, sqrt) or 'exit' to quit: sqrt
Enter Value: 9
Your result: 3.0

Enter operation (+, -, *, /, ^, sqrt) or 'exit' to quit: exit
You entered the exit command, bye!
```

## Requirements

- Python 3.x
- No external dependencies (uses only Python’s built-in `math` and `sys` modules)

## How to Run the Project

1. Clone the repository or download the `calculator.py` file to your local machine.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Run the `calculator.py` file using Python.

   ```bash
   python3 calculator.py
   ```

3. Follow the prompts in the terminal to perform calculations.

## Future Enhancements

- **Additional Features**: Support for more complex mathematical operations, such as trigonometric functions, logarithms, and factorials.
- **Memory Feature**: Allow users to store and recall previous results.
- **Input History**: Display the history of past calculations.
- **Graphical User Interface (GUI)**: Develop a GUI version of the calculator to make it more user-friendly.

___