'''
print("========================")
print("   NUMBER GUESSING GAME")
print("========================")

secret_number = 7

for attempt in range(1, 4):

    print("Attempt", attempt)

    guess = int(input("Enter your guess: "))

    if guess == secret_number:
        print("🎉 Correct!")
        print("You won the game!")
        break

    elif guess > secret_number:
        print("Too high! Try again.")

    else:
        print("Too low! Try again.")

else:
    print("Game Over!")
    print("The correct number was", secret_number)
'''    
#
'''
import random

print("=============================")
print("    ROCK PAPER SCISSORS")
print("=============================")

print("1. Rock")
print("2. Paper")
print("3. Scissors")

choice = int(input("Enter your choice: "))

computer_choice = random.randint(1, 3)

if choice == 1:
    player = "Rock"
elif choice == 2:
    player = "Paper"
elif choice == 3:
    player = "Scissors"
else:
    print("Invalid choice!")
    exit()

if computer_choice == 1:
    computer = "Rock"
elif computer_choice == 2:
    computer = "Paper"
else:
    computer = "Scissors"

print()
print("Your Choice     :", player)
print("Computer Choice :", computer)

if player == computer:
    print("🤝 It's a Draw!")

elif player == "Rock" and computer == "Scissors":
    print("🎉 You Win!")

elif player == "Paper" and computer == "Rock":
    print("🎉 You Win!")

elif player == "Scissors" and computer == "Paper":
    print("🎉 You Win!")

else:
    print("😞 Computer Wins!")
'''
