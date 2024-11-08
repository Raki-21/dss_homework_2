import random

def generate_random_integer(min_value, max_value):
    """
    Generate a random integer between min_value and max_value, inclusive.

    Args:
        min_value (int): The lower bound for the random integer.
        max_value (int): The upper bound for the random integer.

    Returns:
        int: A random integer between min_value and max_value.
    """
    return random.randint(min_value, max_value)


def select_random_operator():
    """
    Select a random arithmetic operator.

    Returns:
        str: A randomly chosen operator from '+', '-', or '*'.
    """
    return random.choice(['+', '-', '*'])


def generate_math_problem(number1, number2, operator):
    """
    Generate a math problem based on two numbers and an arithmetic operator.

    Args:
        number1 (int): The first operand.
        number2 (int): The second operand.
        operator (str): The arithmetic operator ('+', '-', or '*').

    Returns:
        tuple: A string representing the math problem and the correct answer.

    Raises:
        ValueError: If an invalid operator is provided.
    """
    problem_statement = f"{number1} {operator} {number2}"
    if operator == '+':
        answer = number1 + number2
    elif operator == '-':
        answer = number1 - number2
    elif operator == '*':
        answer = number1 * number2
    else:
        raise ValueError("Invalid operator. Choose from '+', '-', or '*'.")

    return problem_statement, answer


def math_quiz():
    """
    Run the math quiz game, presenting random math problems and calculating the user's score.

    This function generates random arithmetic problems, gets user answers, and checks
    correctness, tallying the score at the end.
    """
    score = 0
    total_questions = 3  # Number of questions to be asked in the quiz

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        # Generate two random numbers and an operator
        number1 = generate_random_integer(1, 10)
        number2 = generate_random_integer(1, 5)
        operator = select_random_operator()

        # Create the problem and calculate the correct answer
        problem_statement, correct_answer = generate_math_problem(number1, number2, operator)
        print(f"\nQuestion: {problem_statement}")

        # Get user input and validate it
        try:
            user_answer = int(input("Your answer: "))
            if user_answer == correct_answer:
                print("Correct! You earned a point.")
                score += 1
            else:
                print(f"Wrong answer. The correct answer is {correct_answer}.")
        except ValueError:
            print("Invalid input! Please enter a numerical answer.")

    # Final score output
    print(f"\nGame over! Your score is: {score}/{total_questions}")


# Run the quiz game if this script is run directly
if __name__ == "__main__":
    math_quiz()

