"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Zuzana Divínová
email: zuzana.divinova@gmail.com
"""
import random

separator = "-" * 57

NUM_DIGITS = 4  

def generate_secret_number() -> list[str]:
    """
    Generate a random secret number.
    The digits are unique and from 0-9, but the first digit is not 0.
    """
    digits = random.sample(range(0, 10), NUM_DIGITS)
    while digits[0] == 0:
        digits = random.sample(range(0, 10), NUM_DIGITS)
    return [str(d) for d in digits]

def evaluate_guess(secret: list[str], guess: list[str]) -> tuple[int, int]:
    """
    Count bulls (correct position) and cows (correct digit wrong position).
    """
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum(min(secret.count(d), guess.count(d)) for d in set(guess)) - bulls
    return bulls, cows

def format_result(bulls: int, cows: int) -> str:
    """
    Format result message based on the count of bulls and cows.
    """
    bull_word = "bull" if bulls == 1 else "bulls"
    cow_word = "cow" if cows == 1 else "cows"
    return f"{bulls} {bull_word}, {cows} {cow_word}"

def is_valid_guess(guess: str) -> bool:
    """
    Validate the user's guess.
    Must be a digit string of correct length, no duplicate digits.
    """
    if not guess.isdigit():
        return False
    if len(guess) != NUM_DIGITS:
        return False
    if guess[0] == "0":
        return False
    if len(set(guess)) != NUM_DIGITS:
        return False
    return True

def main() -> None:
    print("Hi there!")
    print(separator)
    print(f"I've generated a random {NUM_DIGITS}-digit number for you.\nLet's play a bulls and cows game.")
    print(separator)

    secret_numbers = generate_secret_number()
    # print("Secret:", "".join(secret_numbers))  # For testing

    print("Enter a number:")
    print(separator)

    guess_count = 0

    while True:
        try:
            guess_input = input(">>> ")
        except Exception as e:
            print(f"An error occurred: {e}")
            continue

        if not is_valid_guess(guess_input):
            print("Invalid input.\nPlease enter exactly 4 different digits.\n"
                  "Digits must be unique and the number cannot start with 0.")
            print(separator)
            continue

        guess_count += 1
        guess = list(guess_input)
        bulls, cows = evaluate_guess(secret_numbers, guess)

        if bulls == NUM_DIGITS:
            print(f"Correct, you've guessed the right number \nin {guess_count} guesses!")
            print(separator)
            print("That's amazing!")
            break
        else:
            print(format_result(bulls, cows))
            print(separator)

if __name__ == "__main__":
    main()
