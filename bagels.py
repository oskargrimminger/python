import random

def main():
    print("I am thinking of a 3-digit number. Try to guess what it is.\n\
            Here are some clues:\n\
            When I say: That means:\n\
                Pico            One digit is correct but in the wrong position.\n\
                Fermi           One digit is correct and in the right position.\n\
                Bagels          No digit is correct.\n\
            I have thought up a number.\n\
            You have 10 guesses to get it.")

    while True:
        secretNumber = getSecretNumber()
        print("I thought up a number.")
        print("You have 10 guesses to get it!")

        numGuesses = 1
        while numGuesses <= 10:
            guess = ""
            while len(guess) != 3 or not guess.isdecimal():
                print(f"Guess #{numGuesses}: ")
                guess = input("> ")

            clues = getClues(guess, secretNumber)
            print(clues)
            numGuesses += 1

            if guess == secretNumber:
                break
            if numGuesses > 10:
                print("You ran out of guesses.")
                print(f"The number was {secretNumber}")

        print("Would you like to play again (yes or no)?")
        if input("").lower() != "yes":
            break
    print("Thanks for playing!")

def getSecretNumber():
    numbers = list(range(10))
    random.shuffle(numbers)

    secretNumber = ""
    for digit in range(3):
        secretNumber += str(numbers[digit])
    return secretNumber

def getClues(guess, secretNumber):
    if guess == secretNumber:
        return "You got it!"

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNumber[i]:
            clues.append("Fermi")
        elif guess[i] in secretNumber:
            clues.append("Pico")

    if len(clues) == 0:
        return "Bagels"
    else:
        clues.sort()
        return " ".join(clues)

if __name__ == '__main__':
    main()





