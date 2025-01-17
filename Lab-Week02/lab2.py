import random
def number_guessing_game():
    targetNumber = random.randrange(1,100)
    play =input("Do you want to play number guessing game? (yes/no)").strip().lower
    attempts = 0
    max_attempts =10
    while attempts < max_attempts:
        try:
            userGuess = int( input("Enter your guess:"))
            attempts += 1
            if userGuess < targetNumber:
                if(userGuess - targetNumber)<=5:
                    print("Too low! You are very close! Try again")
                else:
                    print("Too Low, Try Again")
            elif userGuess > targetNumber:
                if abs(userGuess - targetNumber)<=5:
                    print("Too high!You are very closed! Try again")
                else:
                    print("Too high! Try aggin")
            else:
                print(f"Congragulation! You've guessed it in {attempts} attemps.")
            return True
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 100")
    print(f"Game over! The target number was {targetNumber}.")
    return True
number_guessing_game()




