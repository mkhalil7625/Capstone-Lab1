import random

random_number = random.randint(1,10)

user_guess = int(input("guess a number between 1 and 10"))

while random_number != user_guess:
    if user_guess<random_number:
        print("too low")

    elif user_guess>random_number:
        print("too high")

    user_guess = int(input("Try again, guess a number between 1 and 10"))

print("Good job!! you guessed the correct number")