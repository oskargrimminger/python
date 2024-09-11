expression = input("enter your expression:")


expression_list = expression.split('+')

print(expression_list)
result = 0

for num in expression_list:
	result += float(num)

print (result)




