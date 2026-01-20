# Blackjack Game - Technical Overview

A command-line Blackjack implementation in Python demonstrating core programming concepts and game logic.

## Key Technical Concepts

### 1. Dynamic Ace Conversion

Implemented iterative logic to convert multiple Aces from 11 to 1 when a hand busts. Used a `while` loop to handle edge cases where multiple Aces need sequential conversion.

### 2. Modular Function Design

Separated concerns into three specialized functions: card distribution, score calculation with Ace handling, and win/loss determination.

### 3. Game State Management

Maintained separate state for player and dealer hands with proper score recalculation after every card draw and turn.

### 4. Probability Modeling

Modeled real Blackjack card probabilities using list composition where 10-value cards appear 4× more frequently than other values.

### 5. Nested Loop Control

Three iteration levels manage game flow: session replay, player turn decisions with early exit capability, and automated dealer behavior.

### 6. Rule-Based Logic

Implemented win condition checking in priority order: blackjack detection, bust checks, then score comparison to avoid invalid comparisons.

## Skills Demonstrated

- Algorithm design for edge case handling
- Control flow with nested loops and conditional branching
- Function composition and modular organization
- List manipulation (appending, indexing, searching, membership testing)
- State mutation and data structure modification
- Random selection and probability distribution
- Turn-based game loop architecture

## What I Learned

- Iterative problem-solving over trying to predict all scenarios upfront
- Importance of conditional logic ordering in game rules
- How to structure turn-based gameplay with proper state updates
- Managing mutable state across multiple game sessions
- Building simple but effective rule-based AI
