# Python Projects

A collection of small Python programs I'm building while learning to code.

## Number Guessing Game

A command-line game where the computer picks a secret number between 1 and 100 and you try to guess it. After each guess, the game tells you whether you were too high or too low, and when you win, it shows how many attempts it took.

### Features

- Random secret number from 1 to 100 using Python's `random` module
- Higher/lower hints after every guess
- Attempt counter reported at the end
- Built with `while` loops, `if / elif / else`, and f-strings

### How to run

1. Install [Python 3](https://www.python.org/downloads/).
2. Clone this repo (or download `main.py`):
   ```
   git clone https://github.com/diaoawa001/python-projects.git
   cd python-projects
   ```
3. Run the game:
   ```
   python main.py
   ```

### Example

```
Welcome to the Number Guessing Game!

Guess a number between 1 and 100: 50
Your guess is too high. Try again!
Guess a number between 1 and 100: 25
Your guess is too low. Try again!
Guess a number between 1 and 100: 37
Congratulations, you guessed the correct number!
It took you 3 attempt(s).
```

### Planned improvements

- [ ] Handle invalid input (letters, empty entries) with `try / except`
- [ ] "Play again?" option
- [ ] Limit the number of guesses
- [ ] Save high scores to a file

## About

Built by Awa Diao, a Computer Science student at NYU.
