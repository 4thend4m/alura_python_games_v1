def play_hangman_game():
    welcome_hangman_game_message()

    secret_word, num = loading_secret_word()

    command = hangman_game_level_selector()

    hit = hangman_game_player(secret_word, command)

    final_hangman_game_message(secret_word, hit)








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

def hangman_game_level_selector():
    level = 0

    while(level < 1 or level > 3):
        print("1 | Easy: 6 attempts \n2 | Medium: 3 attempts\n3 | Hard: 2 attempts")
        level = int(input("\nPut the number according to the level you want -> "))

        if level == 1:
            command = 1
        elif level == 2:
            command = 2
        elif level == 3:
            command = 3
            
        else:
            print("\n\nError, enter a valid number [1 | 2 | 3]\n\n")
            continue
    
    return(command)

def hangman_game_player(secret_word, command):
        hanged = False
        hit = False
        fails = 0
        letters_already_tried = []

        right_letters = ["_" for letter in secret_word]
        print(right_letters)

        while(not hanged and not hit):
            hangman_draws(fails)
            print(f"Letters already tried \n{letters_already_tried}\n")

            attempt = str(input(f"Enter a letter [{6 - fails}]-> "))
            attempt = attempt.strip().upper()
            letters_already_tried.append(attempt)

            if(attempt in secret_word):
                cont = 0
                for letter in secret_word:
                    if(attempt == letter):
                        right_letters[cont] = attempt
                    cont += 1
            else:
                fails += command

            hanged = fails == 6
            hit = "_" not in right_letters

            print(right_letters)

        return(hit)

def hangman_draws(fails):
    print("  _______     ")
    print(" |/      |    ")

    if(fails == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(fails == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(fails == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(fails == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(fails == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (fails == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def final_hangman_game_message(secret_word, hit):
    print(f"\nThe word was {secret_word}")

    if(hit):
        print("Congratulations, you won")
        print("""
           ___________      
          '._==_==_=_.'     
          .-\\:      /-.    
         | (|:.     |) |    
          '-|:.     |-'     
            \\::.    /      
             '::. .'        
               ) (          
             _.' '._        
            '-------'          
        """, end="")
    
    else:
        print("Sorry, you lose")
        print("""        
        _______________         
       /               \       
      /                 \      
    //                   \/\   
    \|   XXXX     XXXX   | /   
     |   XXXX     XXXX   |/    
     |   XXX       XXX   |     
     |                   |     
     \__      XXX      __/     
       |\     XXX     /|       
       | |           | |       
       | I I I I I I I |       
       |  I I I I I I  |       
       \_             _/       
         \_         _/         
           \_______/ 
        """, end="")

if(__name__ == "__main__"):
    play_hangman_game()