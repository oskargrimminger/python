

numbers = input("Enter numbers:")
list_of_numbers = numbers.split(",")

largest = 0

for x in list_of_numbers:
	if int(x) > int(largest):
		largest = x
		
print(largest)




