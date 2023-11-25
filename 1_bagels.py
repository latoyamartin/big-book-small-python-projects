"""
A deductive logic game where you must guess a number based on clues.
A version of this game is featured in the book 'Invent Your Own Computer Games with Python' by Al Sweigart"""

import random

NUM_DIGITS = 5
MAX_GUESS = 10


def main():
    print(f"""    Bagels, a deductive logic game.\n
    I am thinking of a {NUM_DIGITS}-digit number with no repeated digits.
    Try to guess what it is. Here are some clues:\n
    What I say:    What it means:
    🟢              One digit is Correct and in the Correct position.
    🟡              One digit is Correct but in the Incorrect position.
    🔴              No correct digits
    For example, if the secret number was 248 and your guess was 843, the clues would be 🟢🟡\n""")

    while True:  # Main game loop.
        # This stores the secret number the player needs to guess:
        secret_num = get_secret_num()
        print(
            f'    I have thought up a {NUM_DIGITS}-digit number. You have {MAX_GUESS} guesses to get it.')

        num_guesses = 1
        while num_guesses <= MAX_GUESS:
            guess = ''
            # Keep looping until they enter a valid guess:
            while len(guess) != NUM_DIGITS:
                print(f'Guess #{num_guesses}:')
                guess = input('> ')
                # split guess into a list of integers
                guess = list(guess)

            clues = get_clues(guess, secret_num)
            print(clues)
            num_guesses += 1

            if guess == secret_num:
                break  # They're correct so break out of this loop.
            if num_guesses > MAX_GUESS:
                print(f'You ran out of guesses. The answer was {secret_num}.')

        # Ask player if they want to play again:
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')


def get_secret_num():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = list('0123456789')  # Create a list of digits 0 to 9.
    random.shuffle(numbers)  # Shuffle them into random order.

    # Get the first NUM_DIGITS in the list for the secret number:
    secret_num = ''
    for i in range(NUM_DIGITS):
        # append the number to a list of integers
        secret_num += str(numbers[i])
        secret_num = list(secret_num)
    return secret_num


def get_clues(guess, secret_num):
    """Returns a string withthe pico, fermi, bagels clues for a guess and secret number pair."""
    if guess == secret_num:
        return 'You got it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            # A correct digit is in the correct place.
            clues.append('🟢')
        elif guess[i] in secret_num:
            # A correct digit is in the incorrect place.
            clues.append('🟡')
    if len(clues) == 0:
        return "🔴"  # There are no correct digits at all.
    else:
        # Sort the clues into alphabetical order so their original order doesn't give information away.
        clues.sort()
        # Make a single string from the list of string clues.
        return ' '.join(clues)


# If the program is run (intead of imported), run the game:
if __name__ == '__main__':
    main()
