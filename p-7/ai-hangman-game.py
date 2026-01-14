import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
  api_key=os.environ.get(os.getenv("OPENAI_API_KEY")) 
)

print("Welcome to the hangman game!")

difficulty = input("Choose a difficulty. Type 'easy', 'medium', or 'hard': ").lower()

words_taken = []

print(f"Thinking a {difficulty} word for you to guess...")

response = client.responses.create(
  model="gpt-5-nano",
  instructions="You are a Hangman Game Expert. Your task is to give a word for the hangman game based on the chosen difficulty level. For 'easy', provide a common word with 4-6 letters. For 'medium', provide a moderately common word with 6-8 letters. For 'hard', provide a rare or complex word with 8 or more letters. Return ONLY the word without any additional text and ensure the word has not been used before provided in the 'words_taken' list.",
  input=f"Difficulty: {difficulty}\nWords taken: {', '.join(words_taken)}"
)
hangman_word = response.output_text.strip()
hangman_word_length = len(hangman_word)

words_taken.append(hangman_word)

print("Word found! Start guessing...")

for _ in range(hangman_word_length):
    print("_", end=" ")
print("\n")

turns_left = 6
guessed_letters = []
guessed_word = False

while turns_left > 0 and not guessed_word:
  guess = input("Guess a letter or the whole word: ").lower()

  if guess == hangman_word:
    guessed_word = True
    print(f"Congratulations! You've guessed the word: {hangman_word}")
    break

  if not guess in hangman_word:
    turns_left -= 1
    print(f"Wrong guess. The letter '{guess}' is not in the word. You have {turns_left} turns left.")
  
  for char in hangman_word:
    if char == guess:
      guessed_letters.append(guess)

  if len(guessed_letters) > 0:
    for letter in hangman_word:
      if letter in guessed_letters:
        print(letter, end=" ")
      else:
        print("_", end=" ")
    print("\n")

  if all(letter in guessed_letters for letter in hangman_word):
    guessed_word = True
    print(f"Congratulations! You've guessed the word: {hangman_word}")
    break
  


if guessed_word:
  print(f"Congratulations! You've guessed the word: {hangman_word}")
else:
  print("Sorry, you've run out of turns. Game over!")
