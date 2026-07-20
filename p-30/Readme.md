# Flashy 🇮🇹🇪🇸

A simple desktop flashcard app built with Python and Tkinter to help you learn Spanish vocabulary from Italian words. Cards flip automatically after a few seconds to reveal the translation, and you can mark words as known to remove them from your study deck.

## How It Works

- The app loads a deck of Italian/Spanish word pairs from a CSV file.
- A random card is shown with the **Italian** word on the front.
- After 4 seconds, the card automatically flips to reveal the **Spanish** translation.
- Use the buttons below the card to mark whether you know the word:
  - ✅ **Known** — removes the word from the deck and saves your remaining progress.
  - ❌ **Unknown** — moves on to the next random card, keeping the word in the deck.
- Progress is saved to `data/words_to_learn.csv` so you don't have to relearn words you already know in future sessions.

## Requirements

- Python 3.x
- [pandas](https://pypi.org/project/pandas/)
- Tkinter (usually included with Python; on some Linux distros install via `sudo apt-get install python3-tk`)

## Installation

1. Clone or download this repository.
2. Install the required dependency:
   ```bash
   pip install pandas
   ```
3. Make sure the following folders exist alongside the script:
   - `data/` — containing `italian_spanish_1000.csv` (word list with `italian` and `spanish` columns)
   - `images/` — containing:
     - `card_front.png`
     - `card_back.png`
     - `wrong.png`
     - `right.png`

## Usage

Run the app with:

```bash
python main.py
```

A window titled **Flashy** will open showing your first flashcard. Study away!

## Project Structure

```
.
├── main.py
├── data/
│   ├── italian_spanish_1000.csv
│   └── words_to_learn.csv   (generated as you learn words)
└── images/
    ├── card_front.png
    ├── card_back.png
    ├── wrong.png
    └── right.png
```

## Notes

- On subsequent runs, consider pointing the app at `data/words_to_learn.csv` instead of the original deck if you'd like to resume where you left off (this isn't currently automatic).
- The card flip timer is set to 4 seconds and can be adjusted by changing the `4000` (milliseconds) values in the code.

## License

This project is open source and available for personal or educational use.
