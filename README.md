# :1234: The Equation Game :1234:
## User Manual

### Introduction
The Equation Game is a simple, interactive maths quiz that helps you practise basic arithmetic by solving equations with a missing value (𝑥), such as ```3 × 𝑥 = 12```. This beginner-friendly game runs in the terminal, keeps tracks of your score, and shows the correct answers after each question. No prior experience with Python or programming is required.

### Table of Contents
- [Requirements](#requirements)
- [How to Run the Game](#how-to-run-the-game)
- [How to Play the Game](#how-to-play-the-game)
- [How to Quit the Game](#how-to-quit-the-game)
- [Example Gameplay](#example-gameplay)
  
### Requirements
- Python version 3.9 or later. (To check your Python, run: ```python --version``` or ```python3 --version``` in the terminal)
- A terminal or commpand prompt
- The ganme files (```main.py``` and ```game_functions.py```) saved in a folder on your computer
<div align="right"><kbd><a href="#table-of-contents">↑ Back to top ↑</a></kbd></div>

### How to Run the Game
#### 1. Open a Terminal or Command Prompt
- On Mac: Open Terminal from _Applications > Utilities_
- On Windows: Press `Windows + R`, type `cmd`, and press Enter

#### 2. Go to the Folder Where the Game is Saved
Use the `cd` (change directory) command to move to the folder containing the game files. For example: <br>
`cd /Users/Olivia/Desktop/EquationGame`

#### 3. Launch the Game
Depending on your system, type the following command and press Enter: <br>
`python main.py`

If your system uses Python 3: <br>
`python3 main.py`

Once the game starts, a welcome message will appear, followed by your first question.
<div align="right"><kbd><a href="#table-of-contents">↑ Back to top ↑</a></kbd></div>

### How to Play the Game
#### Objective
In each round, the game generates a random equation with one missing number, shown as 𝑥. Your task is to solve for 𝑥 using basic arithmetic operations such as addition (+), subtraction (-), or multiplication(×).

#### Example Equations
Below are some examples of the types of equations you might encounter:
- ```2 ＋ 𝑥 = 5```
- ```𝑥 − 3 = -1```
- ```8 × 𝑥 = 40```

#### Answering Equations
Simply type your answer and press Enter to submit.
There is no time limit - you can answer as many questions as you like.

#### Game Response
After you submit an answer, the game responds instantly:  
✅ If your answer is correct, it will be acknowledged and your score will increase by 1 point.<br>
❌ If your answer is incorrect, the correct answer will be shown.
<div align="right"><kbd><a href="#table-of-contents">↑ Back to top ↑</a></kbd></div>

### How to Quit the Game
You can exit the game at any time by typing `quit` and pressing Enter. The game will display a final summary including: 
- Your total score
- Your score as a percentage 
- A message based on your final score:
  - Well done! - for a score of 100%
  - Good try - for a score of 60% or more
  - Keep practising - for a score below 60%
  <div align="right"><kbd><a href="#table-of-contents">↑ Back to top ↑</a></kbd></div>

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
<div align="right"><kbd><a href="#table-of-contents">↑ Back to top ↑</a></kbd></div>
