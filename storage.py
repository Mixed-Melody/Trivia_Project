# JSON load/save functions
import json # Import the json module for reading and writing JSON files
from models import TriviaQuestion, Player # Import the TriviaQuestion class from the models module

DATA_FILE = "data/trivia.json" # Define a constant for the path to the JSON file where trivia questions are stored
PLAYER_FILE = "data/players.json" # Define a constant for the path to the JSON file where player data is stored
HISTORY_FILE = "data/quiz_history.json" # Define a constant for the path to the JSON file where quiz history is stored

def load_questions():

    try:
        with open(DATA_FILE, "r") as file: # Open the JSON file in read mode
            data = json.load(file) # Load the JSON data from the file
            questions = [] # Initialize an empty list to store TriviaQuestion objects

        for item in data["questions"]: # Iterate over each item in the loaded JSON data
            question = TriviaQuestion(
                item["id"], # Set the question ID
                item["prompt"], # Set the question prompt
                item["choices"], # Set the question choices
                item["correct_index"], # Set the question correct answer index
                item["category"], # Set the question category
                item["difficulty"], # Set the question difficulty
                item["explanation"], # Set the question explanation
                item["active"] # Set the question active status
            )
            questions.append(question) # Add the TriviaQuestion object to the list
        return questions # Return the list of TriviaQuestion objects

    except (OSError, json.JSONDecodeError) as error: # catch FileNotFoundError and JSONDecodeError to handle file reading issues
        print(f"\nError reading trivia file: {error}") # Print an error message
        return [] # Return an empty list if the JSON file is not found
    
def save_questions(questions):
    data = {"questions":[]} # Initialize a dictionary to store question data

    for question in questions: # Iterate over each TriviaQuestion object in the list
        data["questions"].append({
            "id": question.question_id, # Add the question ID to the dictionary
            "prompt": question.prompt, # Add the question prompt to the dictionary
            "choices": question.choices, # Add the question choices to the dictionary
            "correct_index": question.correct_answer, # Add the question correct answer index to the dictionary
            "category": question.category, # Add the question category to the dictionary
            "difficulty": question.difficulty, # Add the question difficulty to the dictionary
            "explanation": question.explanation, # Add the question explanation to the dictionary
            "active": question.active # Add the question active status to the dictionary
        })
    try:
        with open(DATA_FILE, "w") as file: # Open the JSON file in write mode
            json.dump(data, file, indent=4) # Write the updated trivia questions to the JSON file with indentation for readability
            return True # Return True to indicate that saving the trivia questions was successful
    except (OSError, TypeError) as error: # Catching OSError and TypeError to handle file writing issues
        print(f"\nError saving trivia data: {error}") # Print an error message if there is an issue writing to the file
        return False # Return False to indicate that saving the trivia questions failed

def load_players():
    try:
        with open(PLAYER_FILE, "r") as file: # Open the JSON file in read mode
            data = json.load(file) # Load the JSON data from the file
            players = [] # Initialize an empty list to store Player objects

        for item in data["players"]: # Iterate over each item in the loaded JSON data
            player = Player(
                item["id"], # Set the player ID
                item["name"], # Set the player name
                item.get("high_score", 0) # Set the player high score, defaulting to 0 if not present
            )
            players.append(player) # Add the Player object to the list
        return players # Return the list of Player objects

    except (OSError, json.JSONDecodeError) as error: # Catch errors related to file not found, JSON decoding, or OS errors
        print(f"\nError reading players file: {error}")
        return [] # Return an empty list if there is an error reading the file


def save_players(players):
    data = {"players": []} # Initialize a dictionary to store player data

    for player in players: # Iterate over each Player object in the list
        data["players"].append({
            "id": player.player_id, # Add the player ID to the dictionary
            "name": player.name, # Add the player name to the dictionary
            "high_score": player.high_score # Add the player high score to the dictionary
        })
    try:
        with open(PLAYER_FILE, "w") as file: # Open the JSON file in write mode
            json.dump(data, file, indent=4) # Write the player data to the JSON file with indentation for readability
            return True # Return True to indicate that saving the player data was successful

    except (OSError, TypeError) as error: # Catch OSError to handle file writing issues
        print(f"\nError saving player data: {error}") # Print an error message if there is an issue writing to the file
        return False # Return False to indicate that saving the player data failed

def update_high_score(player, score):
    if score > player.high_score: # Check if the new score is higher than the player's current high score
        player.high_score = score # Update the player's high score
        players = load_players() # Load the existing players from storage
        for i, p in enumerate(players): # Iterate through the list of players to find the current player
            if p.player_id == player.player_id: # Check if the player IDs match
                players[i] = player # Update the player's information in the list
                break
        save_players(players) # Save the updated list of players to storage

def reset_high_scores(players):
    for player in players: # Iterate over each Player object in the list
        player.reset_high_score() # Reset the player's high score to 0
    if save_players(players):
        return True # Return True to indicate that resetting high scores was successful
    else:
        return False # Return False to indicate that resetting high scores failed
    

def load_quiz_history():
    try:
        with open(HISTORY_FILE, "r") as file: # Open the JSON file in read mode
            data = json.load(file) # Load the JSON data from the file
            return data.get("history", []) # Return the quiz history, defaulting to an empty list if not present
    except FileNotFoundError: # Catch FileNotFoundError to handle the case where the file does not exist
        print("\nQuiz history file not found. Returning empty history.") # Print a message indicating that the file was not found
        return [] # Return an empty list if the file is not found
    except (OSError, json.JSONDecodeError) as error: #  Catch OSError and JSONDecodeError to handle file reading issues
        print(f"\nError reading quiz history file: {error}")
        return None # Return None if there is an error reading the file

def save_quiz_history(player, score, category, difficulty):
    history = load_quiz_history() # Load the existing quiz history from storage

    if history is None: # Check if the loaded history is None, indicating an error occurred and stop trying to save.
        print("\nError: Quiz history is None.")
        return

    next_id = len(history) + 1 # Generate a new quiz ID based on the number of existing history entries
    quiz_id = f"Q{next_id:03d}" # Generate a new quiz ID in the format "Q###"


    history_entry = {
        "Quiz ID": quiz_id, # Store the Quiz ID
        "player_id": player.player_id, # Store the player ID
        "score": score, # Store the quiz score
        "category": category, # Store the quiz category
        "difficulty": difficulty # Store the quiz difficulty
    }

    history.append(history_entry) # Add the new history entry to the list

    try:
        with open(HISTORY_FILE, "w") as file: # Open the JSON file in write mode
            json.dump({"history": history}, file, indent=4) # Write the updated quiz history to the JSON file with indentation for readability
            return True # Return True to indicate that saving the quiz history was successful

    except (OSError) as error: # Catch OSError and TypeError to handle file writing issues
        print(f"\nError saving quiz history: {error}") # Print an error message if there is an issue writing to the file
        return False # Return False to indicate that saving the quiz history failed