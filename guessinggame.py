#guessing gAME 
import random

while True:
    choice = input('want to play the guessing game ?(y/n):').lower()
    if choice == 'y':
        number = random.randint(1, 100)  # simulate a random number between 1 and 100
        attempts = 10  # number of chances
        print('you have 10 chances to guess the number between 1 to 100')
        while attempts > 0:
            try:
                guess = int(input('guess the number:'))
                if guess < number:
                    print('too low!')
                elif guess > number:
                    print('too high!')
                else:
                    print('wow you guessed the correct number!')
                    break
                attempts -= 1  # decrement in the number of the attempts
                print(f'you have {attempts} attempts left')
                if attempts == 0:
                    print(f'sorry you have used all of your attempts. Better luck next time! The number was {number}')
            except ValueError:
                print("Invalid input! Please enter a valid number.")
    elif choice == 'n':
        print('thank you for playing!')
        break
    else:
        print('Invalid input, please enter y or n.')
            
            
   