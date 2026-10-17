
from models import TriviaQuestion


question1 = TriviaQuestion(
    "Q001",
    "What is the largest planet in our solar system?",
    ["Earth", "Mars", "Jupiter", "Saturn"],
    3,
    "Science",
    "Easy",
    "Jupiter is the largest planet in our solar system.",
    True
)

question2 = TriviaQuestion(
    "Q002",
    "Which programming language is named after a comedy group?",
    ["Java", "Python", "C++", "Ruby"],
    2,
    "Technology",
    "Medium",
    "Python was named after Monty Python.",
    True
)