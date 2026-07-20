# Write a program to guess a number between 1 and 100 with 10 chances in hand
# If a user guesses the number say "Congrats your guess is correct. Game is over"
# If he fails to guess the number in 10 attempts, say "10 attempts completed. Game ended"

import random
correct_number= random.randint(1,100)
success=False
print(f"Welcome to the number guessing game. You can choose between 5 or 10 attempts to guess the number. 10 is easy level and 5 is hard level")
print(f"You have to guess a number between 1 and 100. All the best")
attempts=int(input("Choose your attempts (5 or 10)?: "))
while attempts>0:
    number=int(input("Enter your guess: "))
    if number==correct_number:
        print("Congrats! You have successfully guessed the correct number. Game Over")
        success=True
        break
    else:
        if number>correct_number:
            higher_or_lower="lower"
        else:
            higher_or_lower="higher"
    attempts-=1 # attempts=attempts-1
    if attempts>0:
        print(f"Your guess is wrong. Try {higher_or_lower} number")
        if attempts==1:
            print(f"You have only {attempts} chance left to guess the number")
        else:
            print(f"You have {attempts} chances to guess the number")
if not success:  #if success==False
    print(f"You have reached maximum attempts. The actual number is {correct_number}. Sorry Game ended")
  # elif number>correct_number:
    #     print(f"Your guess is wrong, Try lower number")
    #     print(f"You have {attempts-n} chances left to guess the number")
    #     n=n+1
    # else:
    #     print(f"Your guess is wrong, Try higher number")
    #     print(f"You have {attempts-n} chances left to guess the number")
    #     n=n+1