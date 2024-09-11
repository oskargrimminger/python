numbers = input("Enter your numbers: ")
list_of_numbers = numbers.split(",")

number_count = {}

for num in list_of_numbers:
	if num in number_count:
		number_count[num] += 1
	else:
		number_count[num] = 1
	



print(number_count)

