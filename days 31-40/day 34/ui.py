from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ('Arial', 20, 'italic')


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.score = 0

        self.window = Tk()
        self.window.title('Quizler')
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.score_label = Label(text=f'Score: {self.score}', bg=THEME_COLOR, padx=20, pady=20, fg='white')
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(150, 125, text='', font=FONT, width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

        true_image = PhotoImage(file='images/true.png')
        self.true_button = Button(image=true_image, padx=20, pady=20, highlightthickness=0, command=self.is_it_true)
        self.true_button.grid(column=0, row=2)

        false_image = PhotoImage(file='images/false.png')
        self.false_button = Button(image=false_image, padx=20, pady=20, highlightthickness=0, command=self.is_it_false)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text='You have reached the end of quiz')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def is_it_true(self):
        self.after_checking_answer(self.quiz.check_answer('True'))

    def is_it_false(self):
        self.after_checking_answer(self.quiz.check_answer('False'))

    def after_checking_answer(self, result: bool):
        if result:
            self.canvas.config(bg='green')
            self.score += 1
            self.score_label.config(text=f'Score: {self.score}')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)


