numbers = input("Enter numbers:")
list_of_numbers = numbers.split(",")

numbers2 = input("Enter numbers:")
list_of_numbers2 = numbers2.split(",")

same_numbers= []

for x in list_of_numbers:
	if x in list_of_numbers2:
		same_numbers.append(x)


print(same_numbers)

