from models import Player, QuizRound
from global_functions import typewriter_print
import temp_questions as tq

def start_quiz():
    typewriter_print("Starting the quiz...")
    player_name = input("Enter your name: ")
    print()#space
    player_id = "P001" # temp
    player = Player(player_id, player_name)
    questions = [tq.question1, tq.question2]
    round1 = QuizRound(player, questions)
    round1.start_round()
    answer = int(input("Enter the number of your answer: "))
    round1.answer_question(answer)
