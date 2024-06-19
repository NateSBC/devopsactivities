# Make a rock paper scissors app that I can play against the computer. 
# The program should keep track of the number of rounds played, the number of rounds
# won by the user, and the number of rounds won by the computer. 
# After each round, the program should display the results 
# and ask the user if they want to play another round. 
# You should use functions, loops, conditionals, random number generation to achieve this.

import random


def play_round():
    choices = ("Rock", "Paper", "Scissors")
    computer_choice = random.choice(choices)
    player_choice = input(f"Please enter your choice {choices}: ")
    print(f"You chose {player_choice} and the computer chose {computer_choice}.")
    
    if player_choice == computer_choice:
            print("Draw")
    elif player_choice == "Rock" and computer_choice == "Scissors":
            print("Player Wins!")
        
    elif player_choice == "Rock" and computer_choice == "Paper":
            print("Player Loses!")
        
    elif player_choice == "Paper" and computer_choice == "Rock":
            print("Player Wins!")
        
    elif player_choice == "Paper" and computer_choice == "Scissors":
            print("Player Loses!")
        
    elif player_choice == "Scissors" and computer_choice == "Paper":
            print("Player Wins!")
        
    elif player_choice == "Scissors" and computer_choice == "Rock":
            print("Player Loses!")
        
    else:
            print("Invalid choice. Please enter again.")
            return play_round()
    
        



num_of_rounds = -1
computer_wins = 0
user_wins = 0

while play_again == "y":
        num_of_rounds += 1
        result = play_round()
                if 
    

    print(f"Number of Rounds = {num_of_rounds}\nUser Wins = {user_wins}\nComputer Wins = {computer_wins}")
    
    play_again = input("Do you want to play again? (y/n): ")

    
    play_round()

