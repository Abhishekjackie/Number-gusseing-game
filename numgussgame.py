import random  # random module import

#  Computer ek secret number generate karta  (1 se 50 ke beech)
secret_number = random.randint(1, 50)

# Loop start  Jab tak user sahi guess nhi karta


while True:
    #  User se guess input lena
    guess = int(input("Guess the number (1-50): "))


    # Guess check karna
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")


    else:
        print(" Congratulations! You guessed it right.")
        break
        #  Loop ko stop karna jab sahi guess ho jaye

