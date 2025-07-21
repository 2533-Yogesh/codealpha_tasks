import random

def play_hangman():
    words = ["Python", "Firewall", "Compiler", "Perceptron", "MongoDB"]
    word_to_guess = random.choice(words)
    word_lower = word_to_guess.lower()
    guessed_letters = []
    tries = 6

    def display_word(word, guessed):
        return " ".join([letter if letter.lower() in guessed else "_" for letter in word])

    print("\n🎮 Welcome to Hangman!")
    print("Guess the word, one letter at a time.\n\tHint: All Wwords are of IT domain.")
    print("Fail to Guess... and you will never know the word.")
    print("You have", tries, "wrong attempts allowed.\n")

    while tries > 0:
        print("Word:", display_word(word_to_guess, guessed_letters))
        print("Guessed letters so far:", " ".join(sorted(guessed_letters)))
        guess = input("Enter a letter: ").lower()

        # Validate input
        if not guess.isalpha() or len(guess) != 1:
            print("!!Please enter a single alphabetic character.\n")
            continue

        if guess in guessed_letters:
            print("!* You already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in word_lower:
            print("|O| Good guess!\n")
        else:
            tries -= 1
            print("|X| Wrong guess! Attempts left:", tries, "\n")

        # Check win condition
        if all(letter.lower() in guessed_letters for letter in word_to_guess):
            print("Congratulations!!! You guessed the word:", word_to_guess)
            break
    else:
        print(" You've run out of tries. The word will be a mystery for you...FOREVER")
        print("\n Kidding, word was.....", word_to_guess)

    print("Game Over!")
    

# Replay Loop
while True:
    play_hangman()
    replay = input("\n Do you want to play again? (yes/no): ").strip().lower()
    if replay not in ['yes', 'y']:
        print("}Thanks for playing Hangman!{")
        break
