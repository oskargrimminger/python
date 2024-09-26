contactbook = {}

def check_new_contact(email, adress, number):
    if '@' not in email or '.' not in email:
        print("Email is incorrect! Please try again!")
        return False
    elif not adress: 
        print("Address is incorrect!")
        return False
    elif '+' not in number:
    	print("Please enter your number with your country code!")
    	return False
    else:
        return True

def add_contact():
    while True:
        name = input("Enter your full name: ")
        email = input("Enter your email address: ")
        adress = input("Enter your address: ")
        number = input("Enter you number: ")

        if not check_new_contact(email, adress, number):
            continue 

        contactbook[name] = (email, adress,number)
        
        another = input("Do you want to add another contact? (yes/no): ").lower()

        if another != 'yes':
            break

    print("\nYour contact book:")
    for name, info in contactbook.items():
        print(f"Name: {name}, Email: {info[0]}, Address: {info[1]}, Number: {info[2]}")


add_contact()

