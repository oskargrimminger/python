import math

def calculator():
	num1 = input("Enter your first Number: " )
	print(num1)
	operator = input("Enter operator (+,-,*,/):")
	print(operator)
	num2 = input("Enter your second Number: " )
	print(num2)

	if  operator == '+':
		print(add(num1 , num2) )	

	elif operator == '-':
		print(sub (num1 ,num2) )

	elif operator == '*':
		print(multi(num1 , num2) )

	elif operator == '/':
		print(div (num1 , num2) )


		
def	add(num1, num2):
	return float(num1) + float(num2)

def sub(num1, num2):
	return float(num1) - floa(num2)

def multi(num1, num2):
	return float(num1) * float(num2)

def div(num1, num2):
	return float(num1) / float(num2)




def main():
	calculator()
	prompt = "\nEnter 'go on' to repeat the program."
	prompt += "\nEnter 'quit' to end the program. "



	message = input(prompt)

	while message != 'quit':
		calculator()
		message = input(prompt)
	
if __name__ == "__main__":
	main()



