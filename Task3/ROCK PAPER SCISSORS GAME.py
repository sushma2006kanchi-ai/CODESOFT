import random

print("=" * 60)
print("         ROCK PAPER SCISSORS GAME")
print("=" * 60)

print("\nGame Rules")
print("-" * 25)
print("Rock     beats Scissors")
print("Scissors beats Paper")
print("Paper    beats Rock")

user_score = 0
computer_score = 0
tie_score = 0

choices = ["rock", "paper", "scissors"]

while True:

    print("\nChoose One")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    user_choice = input("\nEnter your choice: ").lower()

    if user_choice == "1":
        user_choice = "rock"
    elif user_choice == "2":
        user_choice = "paper"
    elif user_choice == "3":
        user_choice = "scissors"

    if user_choice not in choices:
        print("\nInvalid Choice! Please try again.")
        continue

    computer_choice = random.choice(choices)

    print("\n" + "=" * 45)
    print("Your Choice     :", user_choice.capitalize())
    print("Computer Choice :", computer_choice.capitalize())
    print("=" * 45)

    if user_choice == computer_choice:
        print("Result : It's a Tie!")
        tie_score += 1

    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):

        print("Congratulations! You Win!")
        user_score += 1

    else:
        print("Computer Wins!")
        computer_score += 1

    print("\nCurrent Score")
    print("-" * 20)
    print("You      :", user_score)
    print("Computer :", computer_score)
    print("Tie      :", tie_score)

    play_again = input("\nDo you want to play again? (Y/N): ").upper()

    if play_again != "Y":
        break

print("\n" + "=" * 50)
print("             FINAL SCORE")
print("=" * 50)
print("Your Score      :", user_score)
print("Computer Score  :", computer_score)
print("Tie Matches     :", tie_score)

if user_score > computer_score:
    print("\nOverall Winner : YOU")
elif computer_score > user_score:
    print("\nOverall Winner : COMPUTER")
else:
    print("\nOverall Result : DRAW")

print("\nThank you for playing!")
print("Program Closed Successfully.")