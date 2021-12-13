import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
WHITE = "#FFFFFF"
GREEN = "#00E000"
RED = "#E00000"
FONT = "Arial"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        # Labels
        self.score_label = tk.Label(text="Score: 0", bg=THEME_COLOR, fg=WHITE)
        self.score_label.grid(row=0, column=1)

        # Canvas
        self.canvas = tk.Canvas(width=300, height=250,
                                highlightthickness=0, bg=WHITE)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Placeholder Text",
            font=(FONT, 20, 'italic'),
            fill=THEME_COLOR
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Buttons
        true_img = tk.PhotoImage(file="images/true.png")
        self.true_button = tk.Button(image=true_img, highlightthickness=0,
                                     command=self.answer_true)
        self.true_button.grid(row=2, column=0)

        false_img = tk.PhotoImage(file="images/false.png")
        self.false_button = tk.Button(image=false_img, highlightthickness=0,
                                      command=self.answer_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg=WHITE)
        self.score_label.config(text=f"Score: {self.quiz.score}")

        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,
                                   text="You've reached the end of the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def answer_true(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def answer_false(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg=GREEN)
        else:
            self.canvas.config(bg=RED)

        self.window.after(1000, self.get_next_question)
