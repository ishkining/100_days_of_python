from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

questions_list = [Question(item["text"], item["answer"]) for item in question_data]

quiz = QuizBrain(questions_list)

while quiz.still_has_questions():
    quiz.is_answer_correct()

print('Game is over!')
