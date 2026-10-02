import random

def get_hangman_art(lives):
    """
    Returns the ASCII art corresponding to the number of lives remaining.
    """
    # Stages ordered from 0 lives to 6 lives
    stages = [
        # 0 lives (Dead)
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        # 1 life
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     /
           -
        """,
        # 2 lives
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |
           -
        """,
        # 3 lives
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |
           -
        """,
        # 4 lives
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |
           -
        """,
        # 5 lives
        """
           --------
           |      |
           |      O
           |
           |
           |
           -
        """,
        # 6 lives (Initial state)
        """
           --------
           |      |
           |
           |
           |
           |
           -
        """,
    ]
    return stages[lives]


def play_game():
    words = [
        "APPLE",
        "BICYCLE",
        "CLOUD",
        "DOLPHIN",
        "ECHO",
        "FOREST",
        "GALAXY",
        "HORIZON",
        "ISLAND",
        "JUNGLE",
        "KANGAROO",
        "LEMON",
        "MOUNTAIN",
        "BREAD",
    ]

    word = random.choice(words).upper()
    word_letters = set(word)
    alphabet = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    used_letters = set()
    lives = 6

    print("Welcome to Hangman!")

    while len(word_letters) > 0 and lives > 0:
        print(get_hangman_art(lives))
        print(f"Lives remaining: {lives}")
        print("Guessed letters: ", " ".join(sorted(used_letters)))

        # Display progress
        word_list = [letter if letter in used_letters else "_" for letter in word]
        print("Current word: ", " ".join(word_list))
        print("-" * 20)

        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)

            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print(f"Good job! {user_letter} is in the word.")
            else:
                lives -= 1
                print(f"Sorry, {user_letter} is not there.")

        elif user_letter in used_letters:
            print(f"You have already used the letter {user_letter}. Try again.")
        else:
            print("Invalid character. Please type a single letter.")

    # End Game Conditions
    print(get_hangman_art(lives))
    if lives == 0:
        print(f"You died, sorry. The word was {word}")
    else:
        print(f"You guessed the word {word}!!")


if __name__ == "__main__":
    play_game()

print('Bananenbrot!!!!')
