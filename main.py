from models import Player, QuizRound
from global_functions import typewriter_print
from storage import load_questions
from quiz import filter_questions, select_random_questions, get_categories, get_difficulties

def display_options(options, prompt):
    print()  # New line before displaying options
    for row in range(4):
        for col in range(4):
            index = col *4 + row
            if index < len(options):
                print(f"{f'{index + 1}. {options[index]}':<25}", end="") # inner f-string formats the option number and name the outer f-string formats the entire string to be left-aligned with a width of 25 characters
        print()  # New line after each row
    
    print(f"Choose a {prompt} (1 - {len(options)}): ") # Print the range of valid category choices
  
    print()#  New line after displaying options

def choose_options(options, prompt):

    display_options(options, prompt) # Display the options to the user

    while True: # Start a loop to repeatedly prompt the user for a valid option choice
        try:
            choice = int(input("Enter your choice: ")) # Get the user's choice as an integer
            if 1 <= choice <= len(options): # Check if the choice is within the valid range
                return options[choice - 1] # Return the selected option (adjusting for zero-based index)
            else:
                print(f"Invalid selection. Please choose a valid {prompt}.") # Print an error message for invalid selection
        except ValueError:
            print("Invalid input. Please enter a number.\n") # Print an error message for non-integer input
            



def choose_number_of_questions(count):
    print(f"There are {count} questions available. How many would you like to answer? (1 - {count})") # Prompt the user for the number of questions to answer
    while True:
        try:
            choice = int(input("Enter your choice: ")) # Get the user's choice as an integer
            if 1 <= choice <= count: # Check if the choice is within the valid range
                return choice # Return the selected number of questions
            else:
                print(f"Invalid selection. Please choose a number between 1 and {count}.") # Print an error message for invalid selection
        except ValueError:
            print("Invalid input. Please enter a number.") # Print an error message for non-integer input

def start_selection():
    questions = load_questions() # Load the trivia questions from the JSON file

def start_quiz():
    typewriter_print("Please make your selections...")
    questions = start_selection() # Call the start_selection function to begin the quiz


 
    #round1 = QuizRound(player, questions)
    #round1.start_round()
    #answer = int(input("Enter the number of your answer: "))
    #round1.answer_question(answer)
