# :1234: The Equation Game :1234:

## User Manual

### Introduction
The Equation Game is a simple, interactive maths quiz that helps you practise basic arithmetic by solving equations with a missing value (𝑥), such as `3 × 𝑥 = 12`. This beginner-friendly game runs in the terminal, keeps track of your score, and shows the correct answers after each question. No prior experience with Python or programming is required.

### User Manual Overview
- [Requirements](#requirements)
- [How to Run the Game](#how-to-run-the-game)
- [How to Play the Game](#how-to-play-the-game)
- [How to Quit the Game](#how-to-quit-the-game)
- [Example Gameplay](#example-gameplay)
  
### Requirements
- Python version 3.9 or later. (To check your Python, run: `python --version` or `python3 --version` in the terminal)
- A terminal or command prompt
- The game files (`main.py` and `game_functions.py`) saved in a folder on your computer

<div align="right"><kbd><a href="#user-manual-overview">↑ Back to top ↑</a></kbd></div>

### How to Run the Game
#### 1. Open a Terminal or Command Prompt
- On Mac: Open Terminal from _Applications > Utilities_
- On Windows: Press `Windows + R`, type `cmd`, and press Enter

#### 2. Go to the Folder Where the Game is Saved
Use the `cd` (change directory) command to move to the folder containing the game files. For example:  
`cd /Users/Olivia/Desktop/EquationGame`

#### 3. Launch the Game
Depending on your system, type the following command and press Enter:  
`python main.py`

If your system uses Python 3:  
`python3 main.py`

Once the game starts, a welcome message will appear, followed by your first question.

<div align="right"><kbd><a href="#user-manual-overview">↑ Back to top ↑</a></kbd></div>

### How to Play the Game
#### Objective
In each round, the game generates a random equation with one missing number, shown as 𝑥. Your task is to solve for 𝑥 using basic arithmetic operations such as addition (+), subtraction (−), or multiplication (×).

#### Example Equations
Below are some examples of the types of equations you might encounter:
- `2 ＋ 𝑥 = 5`
- `𝑥 − 3 = -1`
- `8 × 𝑥 = 40`

#### Answering Equations
Simply type your answer and press Enter to submit.  
There is no time limit — you can answer as many questions as you like.

#### Game Response
After you submit an answer, the game responds instantly:  
✅ If your answer is correct, it will be acknowledged and your score will increase by 1 point.  
❌ If your answer is incorrect, the correct answer will be shown.

<div align="right"><kbd><a href="#user-manual-overview">↑ Back to top ↑</a></kbd></div>

### How to Quit the Game
You can exit the game at any time by typing `quit` and pressing Enter. The game will display a final summary including: 
- Your total score
- Your score as a percentage 
- A message based on your final score:
  - Well done! – for a score of 100%
  - Good try – for a score of 60% or more
  - Keep practising – for a score below 60%

<div align="right"><kbd><a href="#user-manual-overview">↑ Back to top ↑</a></kbd></div>

### Example Gameplay
```🔢 Welcome to The Equation Game! 🔢  
Try to solve each equation by finding the value of 𝑥.
Type 'quit' to stop the game.

Question 1: 2 × x = 12  
Please enter your answer or 'quit' to end game: 6
✅ Correct! Score: 1/1

Question 2: x - 5 = 5  
Please enter your answer or 'quit' to end game: 9
❌ Incorrect! The answer was 10. Score: 1/2

Question 3: 8 + x = 10  
Please enter your answer or 'quit' to end game: quit

Thanks for playing! Final score: 1/2
Keep practising
Good try
```
<div align="right"><kbd><a href="#user-manual-overview">↑ Back to top ↑</a></kbd></div>


<div align="right"><kbd><a href="#user-manual-overview">↑ Back to top ↑</a></kbd></div>

## Technical Documentation

### Introduction
This document provides a technical overview of the Equation Game, a Python-based terminal program. It has been created for developers or reviewers with a basic understanding of Python and outlines the program's structure, core logic, and key functions.

### Table of Contents
- [File Structure](#file-structure)
- [Game Flow and Logic](#game-flow-and-logic)
- [Overview of Game Functions](#overview-of-game-functions)

### File Structure
The Equation Game consists of two main Python files:

- `main.py`  
  This script functions as the game launcher. It imports the `play_game()` function from `game_functions.py` and executes it when the script is run.

```python
from game_functions import play_game
if __name__ == "__main__":
    play_game()
```

- ```game_functions.py```

  This module contains the core logic of the game. It defines the main functionality through various functions, which are designed to handle a specific task such as:
  - Generating random equations
  - Prompting and validating user input
  - Evaluating player responses
  - Tracking and updating the player's score

<div align="right"><kbd><a href="#table-of-contents">↑ Back to top ↑</a></kbd></div>

### Game Flow and Logic
As outlined below, the Equation Game follows a straightforward terminal-based logic flow.

#### 1. Launching the Game
The game starts when main.py is executed. This calls the play_game() function from the game_functions.py file, initiating the main game loop.

#### 2. Equation Creation
A random mathematical equation is generated using basic arithmetic operations, such as addition (+), subtraction (−), or multiplication (×). The equation is then displayed in the terminal for the user to solve.

#### 3. User Prompt and Input
The user is prompted to solve the displayed equation and enter their answer via the terminal input.

#### 4. Input Validation and Feedback
The program checks whether the user's input is numeric. If the input is invalid, the user is prompted to try again. Once a valid input is entered, it is compared to the correct answer.

Feedback is provided immediately to inform the user if their answer is correct or incorrect, along with the correct answer if needed.

#### 5. Scoring
The game keeps track of the user's score, which increases by 1 point for each correct answer. The current score with feedback is displayed after each round.

#### 6. Game Continuation or Exit
After each round, the loop repeats until the user enters quit, which ends the game with a final score and a message based on their performance.

<div align="right"><kbd><a href="#table-of-contents">↑ Back to top ↑</a></kbd></div>

### Overview of Game Functions
The ```game_functions.py``` module contains the core logic and functionality of the Equation Game. The following section outlines the key functions and their roles within the program.

#### play_game() 
This is the main loop of the game, which incorporates everything together by calling all the other functions in the right order to ensure the game is running smoothly. 

#### welcome_message()
Displays the game's title and instructions at the start of the game. This function is called at the start of  ```play_game() ``` so users are aware of what to do.

#### generate_equation() 
This function creates a random mathematical equation with one missing number, using one of the basic arithmetic operations: addition (+), subtraction (−), or multiplication (×). It returns the equation and the correct answer as a string so it can be checked and compared later.

#### get_user_input() 
Prompts the user to type in an answer via the terminal. It handles basic input and returns the user's response as a string so it can be checked and validated against the correct solution.

#### validate_input(user_input)
Checks whether the user's input is a valid number. If the input cannot be converted to an integer, the function prompts the user again until a valid response is provided.

#### check_answer(user_answer, correct_answer)
Check_answer compares the validated user input to the correct answer. It returns a Boolean value (True if correct, False otherwise) and also provides feedback.

<div align="right"><kbd><a href="#table-of-contents">↑ Back to top ↑</a></kbd></div>
