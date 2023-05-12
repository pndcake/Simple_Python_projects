import random
num = 10
def guessGame(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        try:
            guess = int(input(f"Guess a number between 1 and {x}: "))
            if guess == random_number:
                print(f"Yay, congrats. You have guessed the number {random_number} correctly!")
            elif guess < random_number:
                print("Sorry guess again. Too low.")
            elif guess > random_number:
                print("Sorry guess again. Number too high")
        except ValueError:
            print("Please input valid number")
        
        
guessGame(100)