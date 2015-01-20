import random


def new_word():
    """Imports dictionary, breaks into list, cleans whitespace and lowercases
    everything. Then returns one random choice word from the list"""
    with open("/usr/share/dict/words") as word_list:
        word_list = word_list.readlines()  # breaks into a list of strings
        word_list = [word.strip().lower() for word in word_list]  # cleans list
        new_word = random.choice(word_list)
        return new_word  # as a string


def difficulty(level="n"):
    """determines length of the random word based on level function below"""
    if level == "e":
        word = new_word()
        if len(word) > 6:
            return difficulty("e")
        else:
            return word
    elif level == "n":
        word = new_word()
        if len(new_word()) <= 6 and len(new_word()) >= 10:
            return difficulty("n")
        else:
            return word
    elif level == "h":
        word = new_word()
        if len(word) < 10:
            return difficulty("h")
        else:
            return word


def level():
    """asks user the difficutly level then calls the diffuculty funtion above
    to get the proper starting word"""
    mode = input("Please pick a difficulty level..[e]asy, [n]ormal, [h]ard: ")
    if mode == "e":
        return difficulty("e")
    elif mode == "n":
        return difficulty("n")
    elif mode == "h":
        return difficulty("h")
    else:
        print("Please only choose e, n, or h")
        return level()


def game_check():
    """Check to see if words match and returns winning message. And checks to
    see if player is out of guesses and ends the game"""
    if start_word == blank_word:
        print("Yay! You solved the mystery word")
        return True

    if start_guess < 1:
        print("No more turns, Game Over.\nThe mystery word was: {}."
              .format(' '.join(start_word)))
        return True


def display_message():
    """Shows player running total of guesses and letters"""
    print("="*25)
    print("You have {} guesses left".format(start_guess))
    print("Incorrect letters so far {}\n".format(incorrect_letters))


def get_letter():
    """Asks user for letter and checks to make sure it a legit single letter"""
    letter = input("Please pick a letter to try: ").lower()
    if letter in guessed_letters == True:  # This doesnt work?!?
        print("You have already guessed that letter, try another")
        return get_letter()
    elif len(letter) != 1:
        print("\nPlease input ONE letter\nTry again\n")
        return get_letter()
    elif letter.isalpha() == False:
        print("\nYou guessed a NUMBER\nTry a letter\n")
        return get_letter()
    else:
        # print(guess)
        guessed_letters.append(letter)
        return letter


def letter_check(guess):
    """Checks if guessed letter is in the start_word. If so, replaces the "_"
    in blank_word to the correct letter at proper index position. If letter not
    present, it takes away 1 guess and adds letter to incorrect_guesses list"""
    index = 0
    letter_found = False
    for letter in start_word:  # checks guessed against letter in start_word
        if guess == letter:
            blank_word[index] = guess
            letter_found = True
        index += 1
    if letter_found == True:
        print("\nGOOD GUESS!")

    if letter_found == False:
        print("\n", "Sorry, {} is not in the mystery word".format(guess))
        incorrect_letters.append(guess)
        return False
    # print(blank_word)
    return blank_word

start_word = list(level())  # turns string into list of letters
blank_word = list(len(start_word) * "_")  # turns string into list of u_scores
start_guess = 8
incorrect_letters = []
guessed_letters = []

print("Mystery Word Time.\nYour mystery word has {} letters.\n"
      .format(len(start_word)))
print(' '.join(blank_word), "\n")

# main game loop
while True:
    if game_check() == True:
        break
    display_message()
    letter = get_letter()
    if letter_check(letter) == False:
        start_guess -= 1

    print("\n", ' '.join(blank_word), "\n")
