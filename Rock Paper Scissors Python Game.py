import random

choice = 0
play_again = ""

# START GAME
print("Winning rules of the game ROCK PAPER SCISSORS are:\n",
    "Rock vs Paper => Paper wins \n",
    "Rock vs Scissors => Rock wins \n",
    "Paper vs Scissors => Scissor wins \n")

# SUB-PROBLEM 1: USER (input and conditional choices)
choice = int(input("Enter your choice (1, 2, or 3): "))

while play_again != "N" and play_again != "n":
    #1 looping until user enter invalid input
    if choice == 1 or choice == 2 or choice == 3:
    #2 initialize choice_name variable for user's choice
        if choice == 1:
            choice_name = "Rock"
        elif choice == 2:
            choice_name = "Paper"
        else:
            choice_name = "Scissors"
            
    #3 print user choice
    print("User choice is \n",
        choice_name, "\n",
        "Now it's Computer's turn \n")
    
# SUB-PROBLEM 2: COMPUTER (random choice and conditional choices)

    #1 Computer chooses randomly any number 1 to 3 using randint method
    comp_choice = random.randint(1, 3)
    
    #2 looping until comp_choice is equal to choice
    
#3 initialize value of comp_choice_name variable corresponding to the choice value
    if comp_choice == 1:
        comp_choice_name = "Rock"
    elif comp_choice == 2:
        comp_choice_name = "Paper"
    else:
        comp_choice_name = "Scissors"
    print("Computer choice is \n",
    comp_choice_name, "\n")
    print(choice_name, "vs", comp_choice_name)
    
# SUB-PROBLEM 3: PLAY (Conditional play of game)
#1 check for draw
    if choice == comp_choice:
        print("Draw")
    #2 check condition for winning
    elif (choice == 1 and comp_choice ==3) or (choice == 2 and comp_choice == 1) or (choice == 3 and comp_choice == 2):
        print("You win!")
    #3 Printing either user or computer wins or draw
    else:
        print("Computer wins!")
        
    # SUB-PROBLEM 4: PLAY AGAIN (User input choice to play again)
    play_again = input("Do you want to play again? (Y/N): ")
    #1 if user input n or N then condition is True
    if play_again != "N" and play_again != "n":
        choice = int(input("Enter your choice (1, 2, or 3): "))
    print("Thanks for playing")
