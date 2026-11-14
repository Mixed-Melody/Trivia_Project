# JSON load/save functions
import json # Import the json module for reading and writing JSON files
from models import TriviaQuestion, Player # Import the TriviaQuestion class from the models module

DATA_FILE = "data/trivia.json" # Define the path to the JSON file where trivia questions are stored

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

    except FileNotFoundError:
        print("Trivia file not found. Starting with an empty question bank.")
        return [] # Return an empty list if the JSON file is not found
    except json.JSONDecodeError:
        print("Trivia JSON file is corrupted. Unable to load questions.")
        return [] # Return an empty list if there is an error decoding the JSON file

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

    with open(DATA_FILE, "w") as file: # Open the JSON file in write mode
        json.dump(data, file, indent=4) # Write the updated trivia questions to the JSON file with indentation for readability
    
def load_players():
    try:
        with open("data/players.json", "r") as file: # Open the JSON file in read mode
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

    except FileNotFoundError:
        print("Players file not found. Starting with an empty player list.")
        return [] # Return an empty list if the JSON file is not found
    except json.JSONDecodeError:
        print("Players JSON file is corrupted. Unable to load players.")
        return [] # Return an empty list if there is an error decoding the JSON file

def save_players(players):
    data = {"players": []} # Initialize a dictionary to store player data

    for player in players: # Iterate over each Player object in the list
        data["players"].append({
            "id": player.player_id, # Add the player ID to the dictionary
            "name": player.name, # Add the player name to the dictionary
            "high_score": player.high_score # Add the player high score to the dictionary
        })

    with open("data/players.json", "w") as file: # Open the JSON file in write mode
        json.dump(data, file, indent=4) # Write the player data to the JSON file with indentation for readability

def reset_high_scores(players):
    for player in players: # Iterate over each Player object in the list
        player.reset_high_score() # Reset the player's high score to 0
    save_players(players) # Save the updated list of players to storage

def load_quiz_history():
    try:
        with open("data/quiz_history.json", "r") as file: # Open the JSON file in read mode
            data = json.load(file) # Load the JSON data from the file
            return data.get("history", []) # Return the quiz history, defaulting to an empty list if not present
    except FileNotFoundError:
        print("Quiz history file not found. Starting with an empty history.")
        return [] # Return an empty list if the JSON file is not found
    except json.JSONDecodeError:
        print("Quiz history JSON file is corrupted. Unable to load history.")
        return [] # Return an empty list if there is an error decoding the JSON file

def save_quiz_history(quiz_id, player, score, category, difficulty):
    history_entry = {
        "Quiz ID": quiz_id, # Store the Quiz ID
        "player_id": player.player_id, # Store the player ID
        "score": score, # Store the quiz score
        "category": category, # Store the quiz category
        "difficulty": difficulty # Store the quiz difficulty
    }

    history = load_quiz_history() # Load the existing quiz history from storage
    history.append(history_entry) # Add the new history entry to the list

    try:
        with open("data/quiz_history.json", "w") as file: # Open the JSON file in write mode
            json.dump({"history": history}, file, indent=4) # Write the updated quiz history to the JSON file with indentation for readability
    except IOError:
        print("Error saving quiz history. Unable to write to file.") # Print an error message if there is an issue writing to the file