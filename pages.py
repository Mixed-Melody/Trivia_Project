from storage import load_players, load_quiz_history, save_players
import global_functions as gf

def display_quiz_history():
    gf.typewriter_print("=== Quiz History ===")
    history = load_quiz_history() # Load the quiz history from storage
    if history: # Check if the history is not empty
        for entry in history: # Iterate through each entry in the quiz history
            print(f"Quiz ID: {entry['Quiz ID']:<10} | Player ID: {entry['player_id']:<10} | Score: {entry['score']:<5} | Category: {entry['category']:<15} | Difficulty: {entry['difficulty']:<10}") # Display the quiz history entry in a formatted manner
    else:
        print("No quiz history available yet.")
    input("\nPress Enter to return to the main menu...") # Prompt the user to press Enter to return to the main menu
    return  # Return to the main menu

def display_high_scores():
    gf.typewriter_print("=== High Scores ===")
    players = load_players() # Load the list of players from storage
    if not players: # Check if the list of players is empty
        print("No players found. Please add players to view high scores.")
        return
    else:
        for player in players: # print each player's name, ID, and high score in a formatted manner
            print(f"{player.name:<20} ({player.player_id:<10}) - High Score: {player.high_score:<10}") # Display each player's name, ID, and high score
            
    print("""
    1. Return to Main Menu
    2. Reset High Scores
    """)

    choice = gf.get_valid_int("Enter your choice: ", 1, 2)# Prompt the user for their choice to return to the main menu or reset high scores
    if choice == 1:
        return  # Return to the main menu
    elif choice == 2:
        reset_choice = gf.get_valid_int(
        "\nAre you sure you want to reset all high scores? (1. Yes, 2. No): ".strip(), 1, 2
        ) # Prompt the user for confirmation to reset high scores
        if reset_choice == 1:
            from storage import reset_high_scores
            reset_high_scores(players) # Call the function to reset all players' high scores
            print("\nAll high scores have been reset.")
        else:
            print("\nHigh scores were not reset.")
        return  # Return to the main menu


def display_manage_questions():
    gf.typewriter_print("=== Manage Questions ===")
    # Implement the logic to manage questions here
    print("Question management feature is under development.")

def display_settings():
    gf.typewriter_print("=== Settings ===")
    print("""
    1. Set Typewriter Speed. (0.01 to 0.5, lower is faster)
    2. Set Typewriter Wait Time. (0.0 to 2.0 seconds).
    3. Set Typewriter on/off.
    4. Return to Main Menu.
    """)

    choice = gf.get_valid_int("Enter your choice: ".strip(), 1, 4) # Prompt the user for their choice in settings
    if choice == 1:
        new_speed = gf.get_valid_float("Enter new typewriter speed (seconds per character): ".strip(), 0.01, 0.5) # Prompt the user for a new typewriter speed
        gf.set_typewriter_delay(new_speed) # Set the new typewriter speed
        print(f"Typewriter speed set to {new_speed} seconds per character.")
    elif choice == 2:
        new_wait_time = gf.get_valid_float("Enter new typewriter wait time (seconds after printing): ".strip(), 0.0, 2.0) # Prompt the user for a new typewriter wait time
        gf.set_typewriter_wait(new_wait_time) # Set the new typewriter wait time
        print(f"Typewriter wait time set to {new_wait_time} seconds after printing.")
    elif choice == 3:
        new_state = gf.get_valid_int("Enter 1 to turn typewriter ON or 2 to turn it OFF: ".strip(), 1, 2) # Prompt the user to turn the typewriter effect on or off
        if new_state == 1:
            gf.set_typewriter_effect(True) # Turn the typewriter effect on
            print("Typewriter effect is now ON.")
        else:
            gf.set_typewriter_effect(False) # Turn the typewriter effect off
            print("Typewriter effect is now OFF.")
    elif choice == 4:
        return  # Return to the main menu


def display_about():
    gf.typewriter_print("=== About ===")
    print("""
    Version 1.0
    Developed by Daniel Hacker
    This is a fun trivia game where you can test your knowledge across various categories and difficulties.
    """)
    input("Press Enter to return to the main menu...")
    return  # Return to the main menu