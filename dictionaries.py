numbers = input("Enter your numbers: ")
list_of_numbers = numbers.split(",")


def add_number():
	if num in number_count:
		number_count[num] += 1
	else:
		number_count[num] = 1
	return number_count


number_count = {}

for num in list_of_numbers:
	number_count = add_number()


print(number_count)


