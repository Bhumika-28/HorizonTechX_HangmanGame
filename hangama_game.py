import random

def hangman():
    words = ["python", "coding", "laptop", "gaming", "rocket"]
    word = random.choice(words)

    guessed_letters = []
    incorrect_guesses = 0
    max_guesses = 6

    print("🎮 Welcome to Hangman!")
    print("Guess the word one letter at a time.")
    print(f"You have {max_guesses} incorrect guesses.\n")

    while incorrect_guesses < max_guesses:

        display_word = ""

        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("Word:", display_word)

        if "_" not in display_word:
            print("\n🎉 Congratulations! You guessed the word:", word)
            break

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter a single alphabet letter.\n")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✅ Correct!\n")
        else:
            incorrect_guesses += 1
            remaining = max_guesses - incorrect_guesses
            print(f"❌ Wrong guess! Attempts left: {remaining}\n")

    else:
        print("\n💀 Game Over!")
        print("The word was:", word)

hangman()