import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors), or 'q' to quit: ").lower()
        if user_choice in ['rock', 'paper', 'scissors', 'q']:
            return user_choice
        else:
            print("Invalid choice. Please try again.")

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'draw'
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'scissors' and computer_choice == 'paper') or
        (user_choice == 'paper' and computer_choice == 'rock')
    ):
        return 'user'
    else:
        return 'computer'

def play_game():
    user_score = 0
    computer_score = 0
    draw_count = 0

    print("Let's play Rock, Paper, Scissors!")

    while True:
        user_choice = get_user_choice()
        if user_choice == 'q':
            break

        computer_choice = get_computer_choice()

        print(f"\nYou chose: {user_choice}")
        print(f"The computer chose: {computer_choice}\n")

        winner = determine_winner(user_choice, computer_choice)

        if winner == 'draw':
            print("It's a draw!")
            draw_count += 1
        elif winner == 'user':
            print("You win!")
            user_score += 1
        else:
            print("You lose!")
            computer_score += 1

        print(f"\nScore: You - {user_score}  Computer - {computer_score}  Draws - {draw_count}\n")

    print("\nThanks for playing!")

play_game()
