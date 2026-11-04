import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ").lower().strip()
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    # Added spaces for better readability in the terminal
    print("You chose " + player + ", computer chose " + computer + ".")
    
    if player == computer:
        return "It's a tie!"
 
    elif player == "rock": 
        if computer == "scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rock! You lose." # Fixed the logic/text here
  
    elif player == "paper": 
        if computer == "rock":
            return "Paper covers rock! You win!"
        else:
            return "Scissors cuts paper! You lose." # Fixed the text here
  
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts paper! You win!"
        else:
            return "Rock smashes scissors! You lose." # Fixed the text here

    else:
        return "Invalid input! Please type rock, paper, or scissors."

# Run the game
choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
