def play_hangman_game():
    welcome_hangman_game_message()
    secret_word, num = loading_secret_word()

    right_letters = ["_" for letter in secret_word]
    print(right_letters)

    hanged = False
    hit = False
    fails = 0

    while(not hanged and not hit):
        attempt = str(input("Enter a letter -> "))
        attempt = attempt.strip().upper()

        if(attempt in secret_word):
            correct_hit_mark(attempt, right_letters, secret_word)
        else:
            fails += 1

        hanged = fails == 6
        hit = "_" not in right_letters

        print(right_letters)

def welcome_hangman_game_message():
    print("*"*28)
    print("Welcome to the hangman game")
    print("*"*28)

def loading_secret_word():
    with open("words.txt") as file:
        words = file.readlines()
    from random import randint
    num = randint(0, len(words))
    secret_word = words[num].strip().upper()
    return(secret_word, num)

def correct_hit_mark(attempt, right_letters, secret_word):
    cont = 0
    for letter in secret_word:
        if(attempt == letter):
            print("The letter {0} was found in position {1}\n".format(attempt, cont))
            right_letters[cont] = attempt
        cont += 1

if(__name__ == "__main__"):
    play_hangman_game()