# Write a program to Play Stone-Paper-Scissors GAME with the Computer.

# The game should allow the user to choose between stone, paper, or scissors.
# The computer should randomly choose between stone, paper, or scissors.

import random # Import the random library to generate random choices.

def main(): # Main function to play the game.
    print("Welcome to the Stone-Paper-Scissors Game !")

    # Define the choices dictionary.
    choices = ["stone", "paper", "scissors"]

    # Ask user for input and convert it to an integer.
    user_choice = input("Enter your choice(stone, paper, or scissors): ").lower()
    
    # Computer Choices the randomly.
    computer_choice = random.choice(choices)
    print(f"Computer Chooses: {computer_choice}")


    # Compare user's choice with computer's choice.
    if user_choice == computer_choice:
        print("It's a tie!")

        # Check all winning conditions for the user.
    elif (user_choice == "stone" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "stone") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        
         print("You Win!") # User wins, if any of these conditions are true.
        # If not tie or user win, then computer wins.

    else:
         print("You Lose!")
         # Game Ends Here when you not want to play

# If you want to play again Write yes to continue game again.
if __name__ == "__main__":
    while True:
        main()
        play_again = input("Do you want to play again(Yes/No) :").strip().lower() # When we use .strip() method used for any types of spacebars or newlines ignoring. 
        
        if play_again != "yes": # OR: We can write this line same and flexible as if play_again.startswith("y"):
            print("Thanks for Playing")
            break

    
        
        