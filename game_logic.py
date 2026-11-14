from models import Player, QuizRound
import global_functions as gf
from storage import load_questions,load_players,save_players,save_quiz_history, load_quiz_history
import quiz as q

def display_options(options, prompt):
    print()  # New line before displaying options
    for row in range(4):
        for col in range(4):
            index = col *4 + row
            if index < len(options):
                print(f"{f'{index + 1}. {options[index]}':<25}", end="") # inner f-string formats the option number and name the outer f-string formats the entire string to be left-aligned with a width of 25 characters
        print()  # New line after each row
    
    print(f"Choose a {prompt} (1 - {len(options)}): ") # Print the range of valid category choices
  
    print()# New line after displaying options

def choose_options(options, prompt):

    display_options(options, prompt) # Display the options to the user

    while True: # Start a loop to repeatedly prompt the user for a valid option choice
        try:
            choice = int(input("Enter your choice: ")) # Get the user's choice as an integer
            if 1 <= choice <= len(options): # Check if the choice is within the valid range
                return options[choice - 1] # Return the selected option (adjusting for zero-based index)
            else:
                print(f"Invalid selection. Please choose a valid {prompt}.\n") # Print an error message for invalid selection
        except ValueError:
            print("Invalid input. Please enter a number.\n") # Print an error message for non-integer input      

def choose_number_of_questions(count):
    print(f"There are {count} questions available. How many would you like to answer? (1 - {count})\n") # Prompt the user for the number of questions to answer
    choice = gf.get_valid_int("Enter your choice: ", 1, count) # Get a valid integer input from the user within the specified range
    return choice # Return the user's choice

def choose_player():
    gf.typewriter_print("\nPlease select a player or create a new one...")
    players = load_players()
    options = [] 
    for player in players:
        options.append(f"{player.name} ({player.player_id})") # Create a list of player names and IDs for selection
    options.append("New Player")
    display_options(options, "player") # Display the list of players and the option to create a new player
    choice =gf.get_valid_int("Enter your choice: ", 1, len(options)) # Get a valid integer input from the user within the specified range
    if choice == len(options): # Check if the user chose to create a new player
        return create_new_player() # Call the function to create a new player
    else: 
        return players[choice - 1] 

def create_new_player():

    new_player_name = ""
    while new_player_name == "": # Check if the entered name is empty or contains only whitespace
        new_player_name = input("\nEnter the name for the new player: ").strip() # Prompt the user for the new player's name and remove leading/trailing whitespace
        if new_player_name == "": # Check if the entered name is still empty after stripping whitespace
            print("Player name cannot be empty. Please enter a valid name.\n") # Print an error message for empty name
    players = load_players() # Load the existing players from storage
    next_id = len(players) + 1 # Generate a new player ID based on the number of existing players

    while True:
        new_player_id = f"P{next_id:03d}" # Generate a new player ID based on the number of existing players
        if any(player.player_id == new_player_id for player in players): # Check if the generated ID already exists
            next_id += 1 # Increment the ID if it already exists
        else:
            break # Exit the loop if a unique ID is found
    new_player = Player(new_player_id, new_player_name) # Create a new Player object
    players.append(new_player) # Add the new player to the list of players
    save_players(players) # Save the updated list of players to storage
    return new_player # Return the newly created player

def start_selection():
    gf.typewriter_print("Please make your quiz selections...")

    questions = load_questions() # Load the trivia questions from the JSON file
    if not questions: # Check if the list of questions is empty
         print("No questions available. Please add questions to the trivia game.")
         return

    categories = q.get_categories(questions) # Get the available categories from the loaded questions
    if not categories: # Check if the list of categories is empty
        print("No categories available. Please add questions to the trivia game.")
        return
    
    categories.insert(0, "All") # Add an "All" option to the list of categories
    selected_category = choose_options(categories, "category") # Prompt the user to select a category
    difficulties = q.get_difficulties(questions, selected_category) # Get the available difficulties from the loaded questions
    difficulties.insert(0, "All") # Add an "All" option to the list of difficulties
    selected_difficulty = choose_options(difficulties, "difficulty") # Prompt the user to select a difficulty
    filtered_questions = q.filter_questions(questions, selected_category, selected_difficulty) # Filter the questions based on the selected category and difficulty
    choose_number = choose_number_of_questions(len(filtered_questions)) # Prompt the user to select the number of questions to answer
    return filtered_questions, choose_number,selected_category, selected_difficulty # Return the filtered questions and the number of questions to answer

def start_quiz():
    player = choose_player() # Prompt the user to select or create a player
    selection =start_selection() # Start the selection process for category, difficulty, and number of questions
    if selection is None: # Check if the selection process was unsuccessful
        return # Exit the function if no selection was made
    filtered_questions, choose_number,selected_category, selected_difficulty = selection
    
    print(f"You have selected {choose_number} questions from the filtered list of {len(filtered_questions)} questions.")
    questions = q.select_random_questions(filtered_questions, choose_number) # Select a random subset of questions based on the user's choice
    gf.typewriter_print("Starting the quiz...\n")
    quiz_round = QuizRound(player, questions)

    while not quiz_round.is_finished(): # Continue the quiz until all questions have been answered
        quiz_round.show_question()
        answer = gf.get_valid_int("Enter your answer: ", 1, len(quiz_round.get_current_question().choices))-1 # Prompt the user for their answer and validate the input
        quiz_round.answer_question(answer)
        quiz_round.next_question()
    
    if player.update_high_score(quiz_round.score):
        print("New high score achieved!") # Update the player's high score if applicable
        players = load_players() # Load the existing players from storage
        for i, p in enumerate(players): # Iterate through the list of players to find the current player
            if p.player_id == player.player_id: # Check if the player IDs match
                players[i] = player # Update the player's information in the list
                save_players(players) # Save the updated list of players to storage
                break
        else:
            print("Player not found in the list. High score not saved.") # Print an error message if the player is not found in the list

    save_quiz_history(player, quiz_round.score, selected_category, selected_difficulty) # Save the quiz history entry to storage

    quiz_round.show_summary() # Show the summary of the quiz round
    
    input("\nPress Enter to return to the main menu...")
    return # return to the main menu after the quiz is finished
