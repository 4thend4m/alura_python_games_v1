from guessing_game import play_guessing_game
from hangman_game import play_hangman_game

print("*"*33)
print("Choose the game you want to play")
print("*"*33)
print("1 | Guessing Game \n2 | Hangman Game")
game = int(input("\nPut the number according to the game you want to play-> "))

if (game == 1):
    print("\n\n\n\n")
    play_guessing_game()
elif (game == 2):
    print("\n\n\n\n")
    play_hangman_game()