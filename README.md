# :1234: The Equation Game :1234:
## User Manual

### Introduction
The Equation Game is a simple, interactive maths quiz designed to help you practise solving basic arithmetic problems. In each round, you will be presented with an equation that has one missing number, shown as 𝑥. Your task is to work out the correct value of 𝑥.

The game tracks your score throughout the session and provides feedback at the end. It runs in a terminal and is user-friendly to those with no prior knowledge of Python or programming. 

### Table of Contents
- [How to Run the Game](#how-to-run-the-game)
- [How to Play the Game](#how-to-play-the-game)
- [How to Quit the Game](#how-to-quit-the-game)
- [Example of the Game](#example-of-the-game)
  
### How to Run the Game
#### 1. Open a Terminal or Command Prompt
- On Mac, open Terminal from Applications > Utilities
- On Windows, press `Windows + R`, type `cmd`, and press Enter

#### 2. Go to the Folder Where the Game is Saved
Use the `cd` (change directory) command to move into the folder containing the game files. For example: <br>
`cd /Users/Olivia/Desktop/EquationGame`

#### 3. Launch the Game
Based on your system, type one of the following commands and press Enter: <br>
`python main.py`

If your system uses Python 3, type: <br>
`python3 main.py`

When the game starts, a welcome message will appear, followed by your first question.

### How to Play the Game


### How to Quit the Game
You can exit the game at any time by typing `quit` and pressing Enter. The game will then show a summary, which includes: 
- Your total score
- Your score as a percentage 
- Feedback based on your performance:
  - Well done! - for a score of 100%
  - Good try - for a score of 60% or more
  - Keep practising - for a score below 60%
  <div align="right"><kbd><a href="#table-of-contents">↑ Back to top ↑</a></kbd></div>

### Example of the Game
Below is an example of the game running in the terminal. 

```
🔢 The Equation Game 🔢
Try to solve each equation by finding the value of 𝑥.
Type 'quit' to stop the game.

Question 1: 𝑥 − 3 = -1
Please enter your answer or 'quit' to end game:2
✅ Correct! Score: 1/1

Question 2: 2 ＋ 𝑥 = 5
Please enter your answer or 'quit' to end game: 
✅ Correct! Score: 2/2

Question 3: 8 × 𝑥 = 40
Please enter your answer or 'quit' to end game:4
❌ Incorrect! The answer was 5. Score: 2/3

Question 4: 3 − 𝑥 = -2
Please enter your answer or 'quit' to end game: quit

Thanks for playing! Final score: 2/3
Score percentage: 66.7%
Good try
```
