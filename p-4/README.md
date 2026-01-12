# Rock-Paper-Scissors CLI

A Python-based implementation of Rock-Paper-Scissors utilizing terminal output and the random library.

## Technical Specifications

- Modules: random (Standard Library)
- Interface: Command Line Interface (CLI)

## Logic & Architecture

The application follows a linear execution flow with the following technical components:

- Data Structures: \* ASCII Assets: Multiline strings stored in variables for visual rendering.
- List Mapping: A list choices maps integer indices ($0, 1, 2$) to the corresponding ASCII art variables.
- Input Handling: Captures user input as an int. Includes a boundary check to prevent IndexError when accessing the choices list.
- RNG Logic: Uses random.randint(0, 2) to generate the AI opponent's move, ensuring an equal probability ($1/3$) for each outcome.
- Decision Matrix: Uses a nested if-elif-else structure to evaluate the win/loss/draw conditions.
