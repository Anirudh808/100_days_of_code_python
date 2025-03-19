import random

# Hangman Title
hangman_title = """
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \\ / _' | '_ \\ / _' | '_ ' _ \\ / _' | '_ \\
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                    __/ |                      
                   |___/
"""

# Hangman stages
hangman_stages = [
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    (Game Over!)
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    (1 life left)
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    (2 lives left)
    """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    (3 lives left)
    """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    (4 lives left)
    """,
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    (5 lives left)
    """,
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    (6 lives left)
    """
]

# Word List
words = ["aardvark", "baboon", "camel"]
random_generated_word = random.choice(words)
blanks = ["_"] * len(random_generated_word)
lives_remaining = 6


def is_correct_guess(letter):
    return letter in random_generated_word


def replace_letter_in_blanks(letter):
    for i in range(len(random_generated_word)):
        if random_generated_word[i] == letter:
            blanks[i] = letter


# Game start
print(hangman_title)

while "_" in blanks and lives_remaining > 0:
    print(hangman_stages[lives_remaining])
    print(f"Word to guess: {" ".join(blanks)}")
    user_guess = input("Guess a letter: ").lower()

    if len(user_guess) != 1 or not user_guess.isalpha():
        print("Invalid input. Please enter a single letter.")
        continue

    if user_guess in blanks:
        print(f"You already guessed '{user_guess}'")
        continue

    if is_correct_guess(user_guess):
        replace_letter_in_blanks(user_guess)
        print("Correct guess!")
    else:
        lives_remaining -= 1
        print(f"Wrong guess! You have {lives_remaining} lives left.")

# Game Over message
print(hangman_stages[lives_remaining])  # Final stage display
if "_" not in blanks:
    print(f"🎉 Congratulations! You guessed the word: {random_generated_word} 🎉")
else:
    print(f"💀 Game Over! The word was: {random_generated_word} 💀")

