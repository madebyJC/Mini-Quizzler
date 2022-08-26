import data
from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Mini Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.right_img = PhotoImage(file="images/true.png")
        self.wrong_img = PhotoImage(file="images/false.png")

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.text_canvas = self.canvas.create_text(150, 125,
                                                   text="example",
                                                   fill=THEME_COLOR,
                                                   width=280,
                                                   font=("Arial", 20, "italic"))
        self.canvas.grid(column=1, row=2, columnspan=2, pady=50)

        self.score_label = Label(text=f"Score: 0", fg="white", bg=THEME_COLOR, highlightthickness=0)
        self.score_label.grid(column=2, row=1)

        self.right_button = Button(image=self.right_img, highlightthickness=0, command=self.true_pressed)
        self.wrong_button = Button(image=self.wrong_img, highlightthickness=0, command=self.false_pressed)
        self.right_button.grid(column=1, row=3)
        self.wrong_button.grid(column=2, row=3)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text_canvas, text=q_text)
        else:
            self.canvas.itemconfig(self.text_canvas, text=f"You have reached the end of the quiz. "
                                                          f"Your final score is {self.quiz.score}!")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
