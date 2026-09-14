from time import sleep


def print_text(string):
    for char in string:
        print(char, end="", flush=True)
        sleep(0.05)
    sleep(0.5)
    print()


def show_menu():
    print()
    print_text("=== Welcome to Dani's Trivia Game!!! ===")
    print("1. Start Game")
    print("2. View High Scores")
    print("3. Manage Questions")
    print("4. Quiz History")
    print("5. About")
    print("6. Settings")
    print("7. Exit")
    print()


def start_game():
    print("start_game")


def show_high_scores():
    print("show_high_scores")


def show_manage_questions():
    print("show_manage_questions")


def show_quiz_history():
    print("show_quiz_history")


def show_about():
    print("show_about")


def show_settings():
    print("show_settings")


def exit_game():
    print_text("Thank you for playing! Goodbye!")


while True:
    show_menu()

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        start_game()
    elif choice == "2":
        show_high_scores()
    elif choice == "3":
        show_manage_questions()
    elif choice == "4":
        show_quiz_history()
    elif choice == "5":
        show_about()
    elif choice == "6":
        show_settings()
    elif choice == "7":
        exit_game()
        break
    else:
        print("Invalid selection. Please choose 1-7.")
