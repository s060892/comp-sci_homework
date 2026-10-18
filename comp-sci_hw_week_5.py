import random


def hangman():
    with open("dictionary.txt", "r") as file:
        words = file.readlines()
        word = random.choice(words).strip()
        guessed = []
        wrong = 0
        max_wrong = 5


    print("Welcome to Hangman!")
    print("You have " + str(max_wrong) + " wrong guesses allowed.")

    while True:
        display_word = ""
        for letter in word:
            if letter in guessed:
                display_word += letter + " "
            else:
                display_word += "_ "
        print(display_word)

        guess = input("Guess a letter: ").lower()

        if guess in guessed:
            print("You already guessed that letter.")
            continue

        guessed.append(guess)

        if guess not in word:
            wrong += 1
            print("Wrong guess! You have " + str(max_wrong - wrong) + " guesses left.")

        if wrong == max_wrong:
            print("You lost! The word was '" + word + "'.")
            break

        if all(letter in guessed for letter in word):
            print("Congratulations! You guessed the word " + word + "!")
            break
        
def play_again():
    while True:
        again = input("Do you want to play again? (y/n): ").lower()
        if again == "y":
            with open("dictionary.txt", "r") as file:
                words = file.readlines()
                word = random.choice(words).strip()
                guessed = []
                wrong = 0
                max_wrong = 5
            hangman()
        elif again == "n":
            print("Thanks for playing!")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")


hangman()
play_again()
