#dice rolling game 
import random

while True: 
	choice = input('want to roll the dice? (y/n): ').lower()
	if choice == 'y':
		dice1 = random.randint(1, 6) # Simulates rolling a dice
		dice2 = random.randint(1, 6) # Simulates rolling a dice
		total = dice1 + dice2
		print(f'You rolled ({dice1}, {dice2})so you will move {total} steps forward')
		if dice1 == 6 and dice2 == 6:
			print(' wow You got the biggest number possible and wll move 12 steps further !')
		elif dice1== 1 and dice2== 1:
			print(' you got the smallest numberpossible and will move 2 steps further !')
		
	elif choice == 'n':
		print('thank you for playing!')
		break
	else:
		print('Invalid input, please enter y or n.')
	
	