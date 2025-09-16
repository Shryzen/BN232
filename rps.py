# Rock Paper Scissors game
import random

while True:
    choice = input('Want to play Rock Paper Scissors game (y/n)? : ').lower()
    if choice == 'y':
        # Define the choices
        rock = 'rock'
        paper = 'paper'
        scissors = 'scissors'

        # Get computer's choice
        computer_choice = random.choice([rock, paper, scissors])

        # Get user's choice
        user_choice = input('Enter your choice (rock, paper, scissors): ').lower()

        # Check if the user's choice is valid
        if user_choice not in [rock, paper, scissors]:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
            continue

        # Determine the winner
        if user_choice == computer_choice:
            print(f"Both chose {user_choice}. It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            print(f"You chose {user_choice} and the computer chose {computer_choice}. You win!")
        else:
            print(f"You chose {user_choice} and the computer chose {computer_choice}. You lose!")

    elif choice == 'n':
        print('Thank you for playing!')
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        