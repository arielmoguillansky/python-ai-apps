# Quiz Application

A command-line quiz game demonstrating object-oriented programming principles in Python.

## Technical Overview

**Architecture**: Three-class system following separation of concerns

- `Question`: Data model for quiz questions
- `QuizBrain`: Game logic and state management
- `main.py`: Application entry point and orchestration

## Key Concepts Demonstrated

**Object-Oriented Design**

- Encapsulation of question data in dedicated class
- Separation of data model from business logic
- State management through class attributes

**Core Logic**

- Question iteration using `question_number` counter
- Score tracking throughout quiz lifecycle
- Input validation and case-insensitive answer checking
- Loop control with `still_has_questions()` method

**Data Flow**

1. Question data imported and instantiated into `Question` objects
2. Question bank passed to `QuizBrain` for management
3. User input processed and validated per question
4. Real-time feedback with progressive score display

## What Was Learned

- Building maintainable class structures
- Managing application state across object instances
- Implementing clean separation between data and logic
- User interaction through console I/O
- List iteration and boundary checking

## Usage

Run with: `python main.py`
