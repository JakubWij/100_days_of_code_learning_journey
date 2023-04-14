from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:
    # quiz_brain attribute passed to this class is another class, by adding ":" we can specify what's
    # the type of object we pass so we make less mistakes, then we can assign it to self.quiz and use later in code
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        # buttons layouts
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(column=0, row=1, columnspan=2, padx=50, pady=50)
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="SAMPLE",
            font=FONT,
            fill=THEME_COLOR,
            width=280
        )

        self.score_label = Label(text="Score:0", bg=THEME_COLOR, fg="white", font=("Arial", 16, "bold"))
        self.score_label.grid(column=1, row=0)

        yes_image = PhotoImage(file="images/true.png")
        self.yes_button = Button(image=yes_image, command=self.answered_yes, bg=THEME_COLOR, highlightthickness=0)
        self.yes_button.grid(column=0, row=2)
        no_image = PhotoImage(file="images/false.png")
        self.no_button = Button(image=no_image, command=self.answered_no, bg=THEME_COLOR, highlightthickness=0)
        self.no_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.yes_button.config(state="disabled")
            self.no_button.config(state="disabled")

    def answered_yes(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def answered_no(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        if not is_right:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
