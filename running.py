import words as w
import printed as p

def running():
    random_word = w.get_random_word()
    guessedWord = ['_'] * len(random_word)
    attemps = 6
    while attemps > 0:
        print(p.printed[6 - attemps])
        print("Current word: " + ' '.join(guessedWord))
        guess = input("Enter a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical character.")
            continue
        if guess in guessedWord:
            print("You've already guessed that letter. Try again.")
            continue
        if guess in random_word:
            for idx, char in enumerate(random_word):
                if char == guess:
                    guessedWord[idx] = guess
            if '_' not in guessedWord:
                print(f"Congratulations! You've guessed the word: {random_word}")
                break
        else:
            attemps -= 1
            if attemps == 0:
                print(p.printed[6])
                print(f"Game over! The word was: {random_word}")
            else:
                print(f"Wrong guess. You have {attemps} attempts left.")
