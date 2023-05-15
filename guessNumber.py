import random
num = 10
def guessGame(x):
    random_number = random.randint(1, x)
    guess = 0
    counter = 10
    while guess != random_number and counter > 0:
        try:
            guess = int(input(f" You have {counter} trys, guess the number between 1 and {x}: "))
            if guess == random_number:
                print(f"Yay, congrats. You have guessed the number {random_number} correctly!")
            elif guess < random_number:
                print("Sorry guess again. Too low.")
            elif guess > random_number:
                print("Sorry guess again. Number too high")
            counter -= 1
        except ValueError:
            print("Please input valid number")
    if guess != random_number:
        print("GAME OVER")

        
        
guessGame(100)