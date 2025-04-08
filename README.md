# :1234: The Equation Game :1234:
## User Manual

### Introduction
The Equation Game is a simple, interactive maths quiz that helps you practise basic arithmetic by solving equations with a missing value (𝑥), such as ```3 × 𝑥 = 12```. This beginner-friendly game runs in the terminal, tracks your score, and provides feedback after each answer. No prior experience of Python or programming is required.

### Table of Contents
- [How to Run the Game](#how-to-run-the-game)
- [How to Play the Game](#how-to-play-the-game)
- [How to Quit the Game](#how-to-quit-the-game)
- [Requirements](#Requirements)
  
### How to Run the Game
#### 1. Open a Terminal or Command Prompt
- On Mac, open Terminal from _Applications > Utilities_
- On Windows, press `Windows + R`, type `cmd`, and press Enter

#### 2. Go to the Folder Where the Game is Saved
Use the `cd` (change directory) command to move to the folder containing the game files. For example: <br>
`cd /Users/Olivia/Desktop/EquationGame`

#### 3. Launch the Game
Depending on your system, type one of the following commands and press Enter: <br>
`python main.py`

If your system uses Python 3, type: <br>
`python3 main.py`

When the game starts, a welcome message will appear followed by your first question.
<div align="right"><kbd><a href="#table-of-contents">↑ Back to top ↑</a></kbd></div>

### How to Play the Game
#### Objective
In each round, the game generates a random equation with one missing number, shown as 𝑥. Your task is to solve for 𝑥 using basic arithmetic operations such as addition, subtraction, or multiplication.

#### Example Equations
Below are some examples of the types of equations you might encounter:
- ```2 ＋ 𝑥 = 5```
- ```𝑥 − 3 = -1```
- ```8 × 𝑥 = 40```

#### Answering Equations
When an equation appears,type your answer and press Enter to submit.
There is no time limit - you can answer as many questions as you like.

#### Feedback
After you submit an answer, the games provide instant feedback:  
✅ If your answer is correct, it will be confirmed and add to your score.<br>
❌ If your answer is incorrect, the correct answer will be displayed.
<div align="right"><kbd><a href="#table-of-contents">↑ Back to top ↑</a></kbd></div>

### How to Quit the Game
You can exit the game at any time by typing `quit` and pressing Enter. A final summary will display: 
- Your total score
- Your score as a percentage 
- Feedback based on your performance:
  - Well done! - for a score of 100%
  - Good try - for a score of 60% or more
  - Keep practising - for a score below 60%
  <div align="right"><kbd><a href="#table-of-contents">↑ Back to top ↑</a></kbd></div>

