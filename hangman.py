import random

words = ["python", "apple", "chair", "tiger", "ocean"]

word = random.choice(words)
guessed = []
attempts = 6

while attempts > 0:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    if "_" not in display:
        print("🎉 You Win!")
        break

    guess = input("Enter a letter: ").lower()

    if guess in word:
        guessed.append(guess)
    else:
        attempts -= 1
        print("Wrong guess!")
        print("Attempts left:", attempts)

if attempts == 0:
    print("Game Over!")
    print("The word was:", word)