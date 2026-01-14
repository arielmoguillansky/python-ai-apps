# AI-Powered Hangman CLI

A technical implementation of the classic Hangman game utilizing the OpenAI GPT-5-Nano model to dynamically generate secret words based on user-selected difficulty levels.

## Features

Dynamic Word Generation: Uses LLM-driven logic to select words based on difficulty parameters (Easy, Medium, Hard).

Contextual Awareness: Passes a words_taken list to the model to ensure word uniqueness across sessions.

Interactive CLI: Real-time feedback on letter guesses, remaining attempts, and word visualization.

Environmental Security: Uses python-dotenv for secure API key management.

## Technical Architecture

The application follows a standard request-response pattern with the OpenAI Chat Completions API (specifically the responses.create interface).

### Prerequisites

Python 3.8+

OpenAI API Key

## Implementation Details

### Logic Flow

Initialization: The script loads environment variables and initializes the OpenAI client.

Prompt Engineering: The system instructions define strict constraints for word selection: | Difficulty | Constraints | | :--- | :--- | | Easy | Common words, 4–6 letters | | Medium | Moderately common, 6–8 letters | | Hard | Rare/Complex, 8+ letters |

Game Loop: A while loop manages state for turns_left, guessed_letters, and win/loss conditions.
