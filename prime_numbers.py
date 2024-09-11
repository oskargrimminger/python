def isprime(num):
	flag = 0
	for i in range (2,num):
		if num%i == 0:
			flag = 1
			break

	return flag != 1




numbers = input("Enter numbers:")

list_of_numbers = numbers.split(",")
print(list_of_numbers)

prime_numbers = []

for number in list_of_numbers:
	print(number)
	if isprime(int(number)):
		prime_numbers.append(number)



if number == 'True':
	append.number 







