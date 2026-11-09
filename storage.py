# JSON load/save functions
import json # Import the json module for reading and writing JSON files
from models import TriviaQuestion # Import the TriviaQuestion class from the models module

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
