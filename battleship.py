from random import randint

def build_board():
	return [['O' for _ in range(5)] for _ in range(5)]

def print_board(board):
	for row in board:
		print(''.join(row))

def random_postion():
	row = randint(0,4)
	col = randint(0,4)
	return [row, col]

def check_battleship_position(number_row, number_col, battleship_position):
	return int(number_row) == battleship_position[0] and int(number_col) == battleship_position[1]

battleship_position = random_postion()
i = 1 
while i <= 10:
	number_row = input("Enter first number: ")
	number_col = input("Enter second number: ")
	picks = [number_row, number_col]
	if check_battleship_position(number_row, number_col, battleship_position):
		print("you got a ship")
		break
	else:
		print(" you didnt get a ship")
		i += 1
	









	







