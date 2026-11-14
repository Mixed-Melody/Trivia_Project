# Trivia Question, Player and Quiz round
import global_functions as gf
import quiz

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

        if not self.question_id or self.question_id.strip() == "": # Check if the question ID is empty or contains only whitespace
            return False, "Question ID cannot be empty."

        if not self.prompt or self.prompt.strip() == "": # Check if the prompt is empty or contains only whitespace
            return False, "Prompt cannot be empty."

        if not self.choices or len(self.choices) < 2: # Check if the choices list is empty or has less than 2 choices
            return False, "At least two choices are required."

        if self.correct_answer is None: # Check if the correct answer index is None
            return False, "Correct answer cannot be None."

        if self.correct_answer < 0: # Check if the correct answer index is less than 0
            return False, "Correct answer cannot be less than 0."

        if self.correct_answer > len(self.choices) - 1: # Check if the correct answer index is greater than the number of choices
            return False, "Correct answer is more than the number of choices."

        if len(set(self.choices)) != len(self.choices): # Check if the choices list contains duplicate values
            return False, "Answer choices must be unique."

        if not self.category or self.category.strip() == "": # Check if the category is empty or contains only whitespace
            return False, "Category cannot be empty."
        
        if not self.difficulty or self.difficulty.strip() == "": # Check if the difficulty is empty or contains only whitespace
            return False, "Difficulty cannot be empty."
        
        if self.difficulty.strip().lower() not in ["easy", "medium", "hard"]: # Check if the difficulty is not one of the allowed values (case-insensitive)
            return False, "Difficulty must be 'Easy', 'Medium', or 'Hard'."

        return True, None


# Player class
class Player:
    def __init__(self, player_id, name, high_score=0):
        self.player_id = player_id
        self.name = name
        self.high_score = high_score


    def __str__(self):
        return (
            f"Player ID: {self.player_id}\n"
            f"Name: {self.name}\n"
            f"High Score: {self.high_score}\n"
        )

    def update_high_score(self, score):
        if score > self.high_score:
            self.high_score = score
            return True  # Return True to indicate that the high score was updated
        return False  # Return False to indicate that the high score was not updated

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
        self.missed_questions = []  # List to store missed questions

    def __str__(self):
        return (
            f"Player: {self.player.name}\n"
            f"Questions: {len(self.questions)}\n"
            f"Current Index: {self.current_index}\n"
            f"Score: {self.score}\n"
        )

    def get_current_question(self):
        return self.questions[self.current_index]

    def show_current_question(self):
        gf.typewriter_print(
            f"Question {self.current_index + 1}\n"
            f"{self.get_current_question().prompt}\n"
        )

    def show_choices(self):
        gf.typewriter_print(f"Choices: ")
        c = 1
        for each in self.get_current_question().choices:
            print(f"{c}. {each}")
            c += 1

    def answer_question(self, answer):
        if self.get_current_question().correct_answer == answer:
            print("\nCorrect!\n")
            self.score += 1
        else:
            self.missed_questions.append(self.get_current_question())
            print("\nIncorrect!\n")

    def show_question(self):
        self.show_current_question()
        self.show_choices()

    def show_summary(self):
        gf.typewriter_print("=== Quiz Summary ===")
        gf.typewriter_print(f"Player: {self.player.name}")
        gf.typewriter_print(f"Score: {self.score}/{len(self.questions)}")
        gf.typewriter_print(f"Percentage: {self.score / len(self.questions) * 100:.2f}%")
        # show breakdown of all missed questions with their correct answers and the player's answer
        if self.missed_questions:
            gf.typewriter_print("=== Missed Questions ===")
            for q in self.missed_questions:
                gf.typewriter_print(f"Category: {q.category:<10} | Difficulty: {q.difficulty:<6} | Correct Answer: {q.choices[q.correct_answer]:<15}")
        else:
            gf.typewriter_print("No missed questions. Great job!")

        # show breakdown of score by category
        gf.typewriter_print("=== Category Breakdown ===")
        for category in set(q.category for q in self.questions):
            category_questions = [
                q for q in self.questions
                if q.category == category
            ]

            category_score = sum(
                1 for q in category_questions
                if q not in self.missed_questions
            )
            gf.typewriter_print(
                f"Category: {category:<15} | "
                f"Score: {category_score}/{len(category_questions)} | "
                f"Percentage: {category_score / len(category_questions) * 100:.2f}%"
                )
        

    def next_question(self):
        if self.current_index < len(self.questions):
            self.current_index += 1
            return True
        else:
            self.show_summary()
            return False

    def is_finished(self):
        return self.current_index >= len(self.questions) # returns true if the current index is greater than or equal to the number of questions

 
