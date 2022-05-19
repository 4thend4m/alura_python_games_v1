def play_guessing_game():
    welcome_guessing_game_message()

    secret_number = loading_secret_number()
    
    attempts, missed_score, level, total_score = guessing_game_level_selector()
    
    total_score = guessing_game_player(attempts, missed_score, secret_number, total_score)
    
    final_guessing_game_message(secret_number, total_score)
    
    
    
    
    
    
    
    
def welcome_guessing_game_message():
    print("*"*28)
    print("Welcome to the guessing game")
    print("*"*28)

def level_and_score():
    level = 0
    total_score = 1000
    
    return(level, total_score)

def loading_secret_number():
    from random import randint
    secret_number = randint(0, 100)

    return(secret_number)

def guessing_game_level_selector():
    level = 0
    total_score = 1000

    while(level < 1 or level > 4):
        print("1 | Easy: 20 attempts \n2 | Medium: 10 attempts\n3 | Hard: 5 attempts\n4 | Impossible: 3 attempts")
        level = int(input("\nPut the number according to the level you want -> "))

        if(level == 1):
            attempts = 20
            missed_score = 50
        elif(level == 2):
            attempts = 10
            missed_score = 100
        elif(level == 3):
            attempts = 5
            missed_score = 200
        elif(level == 4):
            attempts = 3
            missed_score = 333.3
        else:
            print("\n\nError, enter a valid number [1 | 2 | 3 | 4]\n\n")
            continue
        
        return(attempts, missed_score, level, total_score)
        
def guessing_game_player(attempts, missed_score, secret_number, total_score):
    for c in range(1, attempts+1):

        number = int(input("Enter a number [{0}] -> ".format(attempts)))
        attempts -= 1

        if (number < 0 or number > 100):
            print("Error, enter a number between 0 and 100")
            attempts += 1
            continue

        if (number == secret_number):
            print("You got correct, congratulations")
            break
        else:
            if (number < secret_number):
                print("This number is lower than the secret number")
            elif (number > secret_number):
                print("This number is greater than the secret number")
            total_score -= missed_score
            
    return(total_score)
    
def final_guessing_game_message(secret_number, total_score):
    print("\nThe secret number was: {}".format(secret_number))
    print("You did {} points".format(round(total_score)))
    

if(__name__ == "__main__"):
    play_guessing_game()