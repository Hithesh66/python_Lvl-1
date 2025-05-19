word = "uranus"  # The word to guess
guessed = []  # List to store guessed letters
attempts = 6  # Number of incorrect guesses allowed

# Start with the display as all underscores
display = ["_" for _ in word]

print("🐍 Welcome to Hangman Lite!")
print(" ".join(display))  # Print the initial blank word

while attempts > 0:
    guess = input("Guess a letter: ").lower()

    if guess in guessed:
        print("⚠️ You already guessed that!")
        continue

    guessed.append(guess)

    if guess in word:
        print("✅ Correct!")
    else:
        print("❌ Wrong!")
        attempts -= 1

    # Update the display with the guessed letters
    display = [letter if letter in guessed else "_" for letter in word]
    print(" ".join(display))  # Print the current state of the word

    if "_" not in display:  # Check if there are no underscores left
        print("🎉 You guessed the word! You win!")
        break

if "_" in display:
    print("💀 Out of attempts. You lose!")
    print(f"The word was: {word}")
