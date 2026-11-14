# menu loop and game flow
import global_functions as gf
import pages
import game_logic as gl

first_load = True  # Flag to indicate if it's the first time loading the menu

def show_menu():
    gf.typewriter_print("\n=== Main Menu ===")
    print("""
    1. Start Game
    2. View High Scores
    3. Manage Questions
    4. Quiz History
    5. Settings
    6. About
    7. Exit
    """)

def start_game():
    print("Starting game...")
    print() # Space for better readability
    gl.start_quiz() # Call the function to start the quiz

def exit_game():
    gf.typewriter_print("Thank you for playing! Goodbye!")

if first_load: # print a message the first time the menu is loaded
    gf.typewriter_print("=== Welcome to Dani's Trivia Game!!! ===")
    first_load = False  # Set the flag to False after the first load


show_menu()

while True:    
    try:
        choice = gf.get_valid_int("Enter your choice (1-7): ".strip(), 1, 7) # Prompt the user for their menu choice and validate the input
        print()# Space for better readability

    except ValueError:
        print("Invalid input. Please enter integer between 1 and 7.") # Print an error message for non-integer input
        continue

    if choice == 1:
        start_game() # Call the function to start the quiz
    elif choice == 2:
        pages.display_high_scores()
    elif choice == 3:
        pages.display_manage_questions()
    elif choice == 4:
        pages.display_quiz_history()
    elif choice == 5:
        pages.display_settings()
    elif choice == 6:
        pages.display_about()
    elif choice == 7:
        exit_game()
        break

    show_menu() # Show the menu again after handling the user's choice
