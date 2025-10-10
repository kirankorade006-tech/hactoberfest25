import random

def get_user_choice():
    choice = input("Choose rock, paper, or scissors: ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Try again.")
        choice = input("Choose rock, paper, or scissors: ").lower()
    return choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play():
    print("🎮 Welcome to Rock-Paper-Scissors!")
    user = get_user_choice()
    computer = get_computer_choice()
    print(f"Computer chose: {computer}")
    print(determine_winner(user, computer))

if __name__ == "__main__":
    play()
