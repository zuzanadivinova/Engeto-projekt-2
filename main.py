"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Zuzana Divínová
email: zuzana.divinova@gmail.com
"""
import random

separator = "-" * 47

print("Hi there!")
print(separator)
print("""I've generated a random 4 digit number for you.
Let's play a bulls and cows game.""")
print(separator)

def generate_secret_number():
    """
    Generate a random 4-digit secret number.
    The digits are unique and range from 1 to 9.
    Returns:
        list of str: A list containing 4 unique digits as strings.
    """
    digits = random.sample(range(1, 10), 4)
    return [str(digit) for digit in digits]

def evaluate_guess(secret, guess):
    """
    Compare the secret number and the player's guess.
    Counts bulls (correct digit and correct position)
    and cows (correct digit but wrong position).

    Args:
        secret (list of str): The secret number as a list of digits.
        guess (list of str): The player's guess as a list of digits.

    Returns:
        tuple: Number of bulls and cows as integers.
    """
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum(min(secret.count(d), guess.count(d)) for d in set(guess)) - bulls
    return bulls, cows

def format_result(bulls, cows):
    """
    Format the result string based on the number of bulls and cows.
    Uses singular or plural form correctly (e.g., 1 bull, 2 bulls).

    Args:
        bulls (int): Number of bulls.
        cows (int): Number of cows.

    Returns:
        str: Formatted result string.
    """
    bull_word = "bull" if bulls == 1 else "bulls"
    cow_word = "cow" if cows == 1 else "cows"

    if bulls == 0:
        bull_word = "bulls"
    if cows == 0:
        cow_word = "cows"

    return f"{bulls} {bull_word}, {cows} {cow_word}"

secret_numbers = generate_secret_number()
# print("Secret number:", "".join(secret_numbers))

print("Enter a number:")
print(separator)

guess_count = 0

while True:
    guess = list(input(">>> "))

    if len(guess) != 4:
        print("Invalid input. \nPlease enter exactly 4 different numbers.")
        print(separator)
        continue
    elif guess[0] == "0":
        print("Invalid input. \nPlease enter exactly 4 different numbers. \n0 can't be first.")
        print(separator)
        continue
    elif len(set(guess)) != 4:
        print("Invalid input. \nPlease enter exactly 4 different numbers.")
        print(separator)
        continue
    elif not "".join(guess).isdigit():
        print("Invalid input. \nPlease enter exactly 4 different numbers.")
        print(separator)
        continue

    guess_count += 1
    bulls, cows = evaluate_guess(secret_numbers, list(guess))

    if bulls == 4:
        print(f"Correct, you've guessed the right number \nin {guess_count} guesses!")
        print(separator)
        print("That's amazing!")
        break
    else:
        print(format_result(bulls, cows))
        print(separator)
