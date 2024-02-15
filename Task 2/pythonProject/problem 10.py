import random

secret_number = random.randint(1, 100)
attempts = 0

print("Can you guess the secret number between 1 and 100?")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == secret_number:
        print(f"Congratulations! You've guessed the number {secret_number} correctly in {attempts} attempts!")
        break
    elif guess < secret_number:
        print("Too low! Try guessing higher.")
    else:
        print("Too high! Try guessing lower.")



