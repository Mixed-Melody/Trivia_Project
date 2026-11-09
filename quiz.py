# Filters questions and returns a list of questions that match the specified category and difficulty
import random

def filter_questions(questions, category, difficulty):
    filtered_questions = []

    # Filter questions based on category and difficulty
    for question in questions:
        if not question.active: # skip inactive questions
            continue  # Continue the loop not break it
        # Check if the question matches the specified category and difficulty and add it to the filtered list
        if (category == "All" or question.category == category) and (difficulty == "All" or question.difficulty == difficulty):
            filtered_questions.append(question)
    return filtered_questions # Return the list of filtered questions

def select_random_questions(questions, count):
    # Check if the count is valid (greater than 0 and less than or equal to the number of available questions)
    if count < 1 or count > len(questions):
        raise ValueError(f"Count must be between 1 and {len(questions)}. Provided count: {count}") # Trigger a ValueError if the count is invalid
    return random.sample(questions, count) # return a unique random sample of questions from the filtered list

def get_categories(questions):
    categories = set() # Create an empty set to store unique categories
    for question in questions: # Iterate over each question in the list
        if question.active: # Check if the question is active
            categories.add(question.category) # Add the category of the active question to the set
    return sorted(categories) # Return a new sorted list of unique categories from the set

def get_difficulties(questions, category):
    difficulties = set() # Create an empty set to store unique difficulties
    filtered_questions = filter_questions(questions, category, "All") # Filter questions based on the specified category
    for question in filtered_questions: # Iterate over each question in the list
            difficulties.add(question.difficulty) # Add the difficulty of the active question to the set
    return sorted(difficulties) # Return a new sorted list of unique difficulties from the set
