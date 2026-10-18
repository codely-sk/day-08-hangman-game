
import random

words = ["python", "laptop", "puzzle", "coding", "planet"]

secret_word = random.choice(words)
guessed_letters = set()
attempts_left = 6

print("=" * 35)
print("       HANGMAN GAME")
print("=" * 35)

print("Guess the secret word, one letter at a time!")
print("Hint: The word starts with", secret_word[0].upper())

while attempts_left > 0:
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word.strip())
    print("Attempts left:", attempts_left)

    if all(letter in guessed_letters for letter in secret_word):
        print("Congratulations! You guessed the word!")
        break

    guess = input("Guess a letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one valid letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.add(guess)

    if guess in secret_word:
        print("Correct guess!")
    else:
        attempts_left -= 1
        print("Wrong guess!")

else:
    print("\nGame over! You ran out of attempts.")

print("The secret word was:", secret_word)
print("Thanks for playing!")
