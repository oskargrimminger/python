import math


while True:
	num1 = input("Enter your first Number: " )
	print(num1)
	operator = input("Enter operator (+,-,*,/):")
	print(operator)
	num2 = input("Enter your second Number: " )
	print(num2)
	if operator == '+':
		print(float(num1) + float(num2))
	elif operator == '-':
		print(float(num1) - float(num2))
	elif operator == '*':
		print(float(num1) * float(num2))
	elif operator == '/':
		print(float(num1) / float(num2))




	prompt = "\nEnter 'go on' to repeat the program."
	prompt += "\nEnter 'quit' to end the program. "



	message = input(prompt)

	if message == 'quit':
		break

	
	
























