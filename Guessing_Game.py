# Guessing Game
Winning_Number = 76
guess = 1
Guess_Number = input("Enter a guess number between 0 to 100: ")
Guess_Number = int(Guess_Number)
Game_over = False

while not Game_over:
    if Guess_Number == Winning_Number:
        print(f"you win: and your guessed this number in {guess}")
        Game_over = True
    else:
        if Guess_Number < Winning_Number:
            print("you guessed too low ")
        else:
            print("you guessed too high ")
            
        guess += 1
        Guess_Number = int(input("Guessed again: "))