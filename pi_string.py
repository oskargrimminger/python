filename = 'pi_digits.txt'

with open(filename) as file_object:
   lines = file_object.readlines()

pi_string = ''
for line in lines:
   pi_string += line.rstrip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
   print("Your birthday is in pi")
else:
   print("your birthday doesnt appear in pi!")

   