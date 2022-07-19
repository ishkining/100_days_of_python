class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    # TODO: 1: asking the questions
    def next_question(self):
        current_question = self.question_list[self.question_number]
        return input(f'Q.{self.question_number + 1}: {current_question.text} ')

    # TODO 2: checking if the answer was correct
    def is_answer_correct(self):
        answer = self.next_question()
        if self.question_list[self.question_number].answer.lower() == answer.lower():
            print('You are right!')
            self.score += 1
        else:
            print('You are wrong!')
        self.question_number += 1
        print(f'The current score is {self.score}/{self.question_number}')

    # TODO 3: checking if we're the end of the quiz
    def still_has_questions(self):
        return self.question_number < len(self.question_list)







