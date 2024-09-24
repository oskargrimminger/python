import hashlib

# Dictionary, um Benutzernamen als Schlüssel und gehashte Passwörter als Werte zu speichern
users = {}

# Funktion, um einen neuen Benutzer zu registrieren
def register():
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    salt = "5gz"
    dataBase_password = password + salt

    hashed_password = hashlib.md5(dataBase_password.encode()).hexdigest()

    users[username] = hashed_password

    print(f"Registered successfully! Username: {username}, Password (hashed): {hashed_password}")

def login():
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    # Salt für das Hashing des eingegebenen Passworts
    salt = "5gz"
    dataBase_password = password + salt
    
    # Hash das eingegebene Passwort mit MD5 und dem Salt
    hashed_password = hashlib.md5(dataBase_password.encode()).hexdigest()

    # Prüfe, ob der Benutzername existiert und das gehashte Passwort übereinstimmt
    if username in users and users[username] == hashed_password:
        print("Processing...")
        print(f"Welcome, {username}!")
    else:
        print("Password or Username is incorrect, please try again!")

# Funktion zur Auswahl zwischen Registrierung und Anmeldung
def choices():
    input_choice = input("Choose between a)Sign Up, b)Login: ")
    if input_choice == 'a':
        register()
    elif input_choice == 'b':
        login()
    else:
        print("Invalid choice, please choose 'a' or 'b'.")

# Hauptschleife, um das Programm fortlaufend auszuführen, bis der Benutzer es beenden möchte
while True:
    choices()
    cont = input("Do you want to continue? (yes/no): ")
    if cont.lower() != 'yes':
        print("Exiting...")
        break




