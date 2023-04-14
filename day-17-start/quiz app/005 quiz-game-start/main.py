from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# https://opentdb.com/api_config.php
question_bank = []
counter = 0
for question in question_data:
    question_bank.append(Question(question["question"], question["correct_answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():# if quiz still has questions remaining:
    quiz.new_question()

print("You have completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")