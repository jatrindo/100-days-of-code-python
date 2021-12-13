import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
WHITE = "#FFFFFF"
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
        self.true_button = tk.Button(image=true_img, highlightthickness=0)
        self.true_button.grid(row=2, column=0)

        false_img = tk.PhotoImage(file="images/false.png")
        self.false_button = tk.Button(image=false_img, highlightthickness=0)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)
