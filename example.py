# Global lists to store usernames and passwords
usernames = []
passwords = []

# Function to register a new user
def register():
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    
    # Append the username and password to the respective lists
    usernames.append(username)
    passwords.append(password)
    
    print(f"Registered successfully! Username: {username}, Password: {password}")

# Function to login a user
def login():
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    
    # Check if the username exists and the password matches
    if username in usernames and password in passwords:
        print("Processing...")
        print(f"Welcome, {username}!")
    else:
        print("Password or Username is incorrect, please try again!")

# Function to choose between sign up and login
def choices():
    input_choice = input("Choose between a)Sign Up, b)Login: ")
    if input_choice == 'a':
        register()
    elif input_choice == 'b':
        login()
    else:
        print("Invalid choice. Please choose 'a' or 'b'.")

# Main loop to continue prompting user
while True:
    choices()
    cont = input("Do you want to continue? (yes/no): ")
    if cont.lower() != 'yes':
        print("Exiting...")
        break

