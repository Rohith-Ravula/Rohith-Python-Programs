#Dice game means rolling a dice to get any of the number between 1 and 6
import random

print("Welcome to the dice game")

while True:  #goes to infinite loop
    choice=input("Press 'Enter' to roll the dice and 'q' to quit the game")
    choice=choice.stripe()
    if choice=='q':
        print('You have quit the game. Thankyou')
        break
    elif choice=='':
        number=random.randint(1,6)
        print(f"Your number is {number}")
    else:
        print('Invalid input')
print("GAME OVER")




