from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
for question in question_data:
    question_text = question["question"]["text"]
    correct_answer = question["correctAnswer"]
    incorrect_answers = question["incorrectAnswers"]
    all_options = incorrect_answers + [correct_answer]
    new_question = Question(question_text, correct_answer, all_options)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
