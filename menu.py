import running as r


def menu():
    print("Choose an option:")
    print("1. Start Game")
    print("2. Exit")
    choice = input("Enter your choice: ")
    return choice

def work():
    print("Welcome to Hangman!")
    print("-------------------")
    print("This is a simple word guessing game. You have 6 attempts to guess the word. \nIf you guess a letter correctly, it will be revealed in the word. If you guess incorrectly, you lose an attempt. \n\nGood luck!")
    while True:
        user_choice = menu()
        if user_choice == '1':
            r.running()
        elif user_choice == '2':
            print("Thank you for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1 or 2.")