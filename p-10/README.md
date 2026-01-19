# Calculator Program

This Python script implements a recursive, stateful calculator that supports basic arithmetic operations through a modular, dictionary-based architecture.

## Technical Logic

1. Functional Mapping

- The program utilizes a dispatch table (the operations dictionary) to map string symbols to their respective mathematical functions. This decouples the user interface from the logic, allowing for easy extensibility.

- Functions: add, subtract, multiply, divide

- Data Structure: operations = {"+": add, ...}

2. Control Flow & State Management

- The core logic resides in the calculator() function, which manages state through a nested execution pattern:

- Accumulation Loop: A while loop tracks the variable should_accumulate. If the user selects 'y', the current answer is assigned to num1, and the loop continues, maintaining the calculation's running total.

- Recursion: If the user selects 'n', the loop terminates, and the program performs a recursive call to calculator(). This resets the entire state and clears the previous calculation.
