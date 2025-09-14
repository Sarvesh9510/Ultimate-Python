# Write a python program capable of playing this game with the user.
'''
1 = for snake
2 = for water
3 = for gun
'''
import random # This line allows the random library to pick random choices for the computer's move.

def main(): # Main function to play the game.
    print("Welcome to the Snake, Water, Gun Game !") # Greeting the player.

       # Dictionary to map numbers to choices for easy understanding.
    choices = {1: 'Snake', 2: 'Water', 3: 'Gun'}


       # Ask user for input and convert it to an integer.
   
    user_choice = int(input("Enter your choice (1 for Snake, 2 for Water, 3 for Gun): "))

       # Computer randomly selects a number between 1, 2, or 3.

    computer_choice = random.randint(1, 3)
    print(f"Computer Chooses: {choices[computer_choice]}") # Displaying the computer's choice.


       # Check for Tie first: both choices are the same.
    if user_choice == computer_choice:
       print("It's a Tie!") # Both picked same, it's a tie.

       # Check all winning condition for the user.
    elif (user_choice == 1 and computer_choice == 2) or \
         (user_choice == 2 and computer_choice == 3) or \
         (user_choice == 3 and computer_choice == 1):

       print("You Win!") # User wins, if any of these conditions are true.

              # If not tie or user win, then computer wins.
    else:
       print("Computer Wins, You Lose !") # Computer wins, if all conditions are not met.
              # End the game.

              # Asking user if they want to play again.
       # Infinite loop to keep the game running until user decides to stop.
while True:
   main() # Call the main() function to play the game.
   play_again = input("Do you want to play again? (yes/no): ").lower() # Convert user input to lower case to make it case insensitive.

       # If user types "Yes", call the main() function again to play another round.
   if play_again != "yes":
          print("Thank you for Playing again!")
          break

       