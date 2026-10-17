# menu loop and game flow
from global_functions import typewriter_print
from main import start_quiz


def show_menu():
    print()
    typewriter_print("=== Main Menu ===")
    print("1. Start Game")
    print("2. View High Scores")
    print("3. Manage Questions")
    print("4. Quiz History")
    print("5. Settings")
    print("6. About")
    print("7. Exit")
    print()


def start_game():
    print("start_game")
    start_quiz()


def show_high_scores():
    print("show_high_scores")
    show_menu()


def show_manage_questions():
    print("show_manage_questions")
    show_menu()
    

def show_quiz_history():
    print("show_quiz_history")
    show_menu()
    

def show_about():
    print("show_about")
    show_menu()
    

def show_settings():
    print("show_settings")
    show_menu()
    

def exit_game():
    typewriter_print("Thank you for playing! Goodbye!", 0.05, 0.1)


typewriter_print("=== Welcome to Dani's Trivia Game!!! ===")
show_menu()

while True:    

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        start_game()
        break
    elif choice == "2":
        show_high_scores()
    elif choice == "3":
        show_manage_questions()
    elif choice == "4":
        show_quiz_history()
    elif choice == "5":
        show_settings()
    elif choice == "6":
        show_about()
    elif choice == "7":
        exit_game()
        break
    else:
        print("Invalid selection. Please choose 1-7.")
