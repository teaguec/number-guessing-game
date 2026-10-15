import random

number = random.randint(1, 100)
attempts = 0
success = False
print("Welcome to the number guessing game!\nHere are the rules: You will have a certain number of guesses based on the difficulty you choose"
". If you are correct, you win! If you do not get the answer within the number of attempts, you lose! The number is between 1-100. Good luck!")

yes = True
while yes == True:
    difficulty = input("Select difficulty: Enter 1 for Easy, 2 for Medium and 3 for Hard")

    if(difficulty not in ["1","2","3"]):
        print("Invalid entry. Please try again.")
    else:
        match difficulty:
            case "1":
                attempts = 3
            case "2":
                attempts = 2
            case "3":
                attempts = 1
        break

count = 0
while attempts > 0:

    count += 1
    guess = int(input("Enter a guess:"))
    if guess == number:
        print(f"You win! This took you {count} attempts!")
        success = True
        break
    else:
        print("Incorrect!")
        if number > guess:
            print("The number is higher than that!")
        else:
            print("The number is lower than that!")
        attempts -= 1

if not success:
    print(f"You lose! The number was {number}.")
