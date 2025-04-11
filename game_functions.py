"""
Functions for the Equation Game.

Creates random equations with a missing value, handles user input,
checks answers, and displays results at the end.
"""

import random
import operator

def create_equation():
    """
    Generates a simple equation with one missing value.
    
    Randomly selects two numbers and arithmetic operator (+, ×, or -), 
    missing part of equation (num1, num2, or answer) and replaces it with 𝑥.
    
    Returns: 
        tuple:
            A pair containing: 
            str: The equation with missing value replaced by 𝑥.
            int: The correct value that was hidden
    """

    # Define arithmetic operators and their function
    symbols = {
        "+": operator.add,
        "×": operator.mul,
        "-": operator.sub,
    }

    # Randomly select two numbers
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 5)

    # Randomly choose an operation (add, multiply, or subtract)
    operation = random.choice(list(symbols.keys()))
    
    # Calculate the answer to the equation 
    answer = symbols[operation](num1, num2)

    # Randomly choose a part of the equation to hide
    hide = random.choice(["num1", "num2", "answer"])

    # Generate the equation with 𝑥 as the missing value 
    if hide == "num1":
        equation = f"𝑥 {operation} {num2} = {answer}"
        missing = num1
    elif hide == "num2":
        equation = f"{num1} {operation} 𝑥 = {answer}"
        missing = num2
    else:
        equation = f"{num1} {operation} {num2} = 𝑥"
        missing = answer

    # Return the equation string and answer (missing value)
    return equation, missing


def valid_input(prompt_user):
    """
    Prompts user for input until they enter a number or 'quit'.
    
    Parameters:  
    prompt_user (str): The message displayed to the user when asking for input.

    Returns:
    int or str:
        int: If valid, the user's reponse is converted to an integer.
        str: The string 'quit' if the user chooses to exit the game.
    """

    while True:
        # Strip spaces and convert input to lowercase 
        response = input(prompt_user).strip().lower()

        # If user types 'quit', exit the loop
        if response == "quit":
            return response
        
        try:
            # Try converting input to an integer
            return int(response)
        except ValueError:
            # Handle invalid input and repeat the prompt
            print("\nYour answer is not a valid number. Please try again.")



def check_answer(user_answer, correct_answer):
    """
    Compares the user's answer to the correct answer for the equation.

    Parameters:
    int: user_answer (The value by the user).
    int: correct_answer (The correct value for the equation).

    Return:
    bool: True if the user's answer is correct, otherwise it is false (incorrect).
    """

    # Compare the user's answer with correct answer and return result
    return user_answer == correct_answer


def show_result(score, total):
    """
    Displays the final score, percentage, and provides feedback based on score.

    Parameters:
    int: total - The total number of questions
    int: score - The number of correct answers
    """

    print(f"\nThanks for playing! Final score: {score}/{total}")

    if total > 0:
        percent = (score / total) * 100
        print(f"Score percentage: {percent:.1f}%")
        
        # Provide feedback based on score percentage
        if percent == 100:
            print("Well done!")
        elif percent >= 60:
            print("Good try")
        else:
            print("Keep practising")
    else:
        print("No questions were answered")

def play_game():
    """
    Runs the main game loop:
    
    Continuously generates equations, prompts the user for input,
    checks answers, keeps score, and provides final score when user quits.
    """

    # Display the game title and instructions
    welcome_message()

    # Track the number of correct answers
    score = 0

    # Track the total number of questions 
    questions = 0

    while True:
        # Generate a new equation and get the correct answer
        equation, correct_answer = create_equation()
        print(f"\nQuestion {questions + 1}: {equation}")

        # Prompt user for input or show results if user enters quit
        user_answer = valid_input("Please enter your answer or 'quit' to end game: ")
        if user_answer == "quit":
            show_result(score, questions)
            break
        
        # Update the number of questions 
        questions += 1

        # Check user's answer and update score
        if check_answer(user_answer, correct_answer):
            score += 1
            print(f"✅ Correct! Score: {score}/{questions}")
        else:
            print(f"❌ Incorrect! The answer was {correct_answer}. Score: {score}/{questions}")


def welcome_message():
    """
    Displays the game title and instructions.
    """
    print("🔢 The Equation Game 🔢")
    print("Try to solve each equation by finding the value of 𝑥.")
    print("\nType 'quit' to stop the game.")
