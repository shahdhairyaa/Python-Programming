import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissor): ").lower()
        if user_choice in ['rock', 'paper', 'scissor']:
            return user_choice
        else:
            print("Invalid choice. Please enter rock, paper, or scissor.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissor'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissor') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissor' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    print("Welcome to Rock-Paper-Scissor Game!")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print("You chose:", user_choice)
        print("Computer chose:", computer_choice)

        print(determine_winner(user_choice, computer_choice))

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    main()