# Trivia Question, Player and Quiz round
from global_functions import typewriter_print

# Trivia question class
class TriviaQuestion:
    def __init__(self, question_id, prompt, choices, correct_answer, category, difficulty, explanation, active):
        self.question_id = question_id
        self.prompt = prompt
        self.choices = choices
        self.correct_answer = correct_answer
        self.category = category
        self.difficulty = difficulty
        self.explanation = explanation
        self.active = active

    def __str__(self):
        return (
            f"Question ID: {self.question_id}\n"
            f"Prompt: {self.prompt}\n"
            f"Choices: {self.choices}\n"
            f"Correct Answer: {self.correct_answer}\n"
            f"Category: {self.category}\n"
            f"Difficulty: {self.difficulty}\n"
            f"Explanation: {self.explanation}\n"
            f"Active: {self.active}\n"
        )
    
    def is_valid(self):

        if not self.question_id or self.question_id.strip() == "":
            return False, "Question ID cannot be empty."

        if not self.prompt or self.prompt.strip() == "":
            return False, "Prompt cannot be empty."

        if not self.choices or len(self.choices) < 2:
            return False, "At least two choices are required."

        if self.correct_answer is None:
            return False, "Correct answer cannot be None."

        if self.correct_answer < 1:
            return False, "Correct answer cannot be less than 1."

        if self.correct_answer > len(self.choices):
            return False, "Correct answer is more than the number of choices."

        if not self.category or self.category.strip() == "":
            return False, "Category cannot be empty."
        
        if not self.difficulty or self.difficulty.strip() == "":
            return False, "Difficulty cannot be empty."
        
        if self.difficulty.strip().lower() not in ["easy", "medium", "hard"]:
            return False, "Difficulty must be 'Easy', 'Medium', or 'Hard'."

        return True, None


# Player class
class Player:
    def __init__(self, player_id, name,):
        self.player_id = player_id
        self.name = name
        self.high_score = 0


    def __str__(self):
        return (
            f"Player ID: {self.player_id}\n"
            f"Name: {self.name}\n"
            f"High Score: {self.high_score}\n"
        )

    def update_high_score(self, score):
        if score > self.high_score:
            self.high_score = score

    def change_name(self, new_name):
        self.name = new_name

    def reset_high_score(self):
        self.high_score = 0


# Quiz round class
class QuizRound:
    def __init__(self, player, questions):
        self.player = player
        self.questions = questions
        self.current_index = 0
        self.score = 0

    def __str__(self):
        return (
            f"Player: {self.player.name}\n"
            f"Questions: {len(self.questions)}\n"
            f"Current Index: {self.current_index}\n"
            f"Score: {self.score}\n"
        )

    def show_current_question(self):
        typewriter_print(
            f"Question 1\n"
            f"{self.questions[self.current_index].prompt}\n"
        )

    def show_choices(self):
        typewriter_print(f"Choices: ")
        c = 1
        for each in self.questions[self.current_index].choices:
            print(f"{c}. {each}")
            c += 1

    def answer_question(self, answer):
        if self.questions[self.current_index].correct_answer == answer:
            print("Correct!")
        else:
            print("Incorrect!")

    def update_score(self, score):
        print(f"update_score called with score: {score}")

    def start_round(self):
        print("start_round called")
        self.show_current_question()
        self.show_choices()

    def is_finished(self):
        print("is_finished called") 
