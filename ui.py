import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quizzler App")
        self.window.config(padx=30, pady=30, bg=THEME_COLOR)

        self.score_label = tk.Label(
            self.window, text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 16)
        )
        self.score_label.grid(row=0, column=1, padx=20, pady=10)

        self.canvas = tk.Canvas(self.window, width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        self.Option_A = tk.Button(self.window, text="A", width=20, height=2, highlightthickness=0, bg="#e0e0e0", command=lambda: self.check_answer(self.Option_A))
        self.Option_A.grid(row=2, column=0, padx=10, pady=10)

        self.Option_B = tk.Button(self.window, text="B", width=20, height=2, highlightthickness=0, bg="#e0e0e0", command=lambda: self.check_answer(self.Option_B))
        self.Option_B.grid(row=2, column=1, padx=10, pady=10)

        self.Option_C = tk.Button(self.window, text="C", width=20, height=2, highlightthickness=0, bg="#e0e0e0", command=lambda: self.check_answer(self.Option_C))
        self.Option_C.grid(row=3, column=0, padx=10, pady=10)

        self.Option_D = tk.Button(self.window, text="D", width=20, height=2, highlightthickness=0, bg="#e0e0e0", command=lambda: self.check_answer(self.Option_D))
        self.Option_D.grid(row=3, column=1, padx=10, pady=10)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text, options = self.quiz.next_question()
            q_number = self.quiz.question_number
            self.canvas.itemconfig(self.question_text, text=f"Q{q_number}. {q_text}")
            self.Option_A.config(text=options[0], bg="#e0e0e0")
            self.Option_B.config(text=options[1], bg="#e0e0e0")
            self.Option_C.config(text=options[2], bg="#e0e0e0")
            self.Option_D.config(text=options[3], bg="#e0e0e0")
        else:
            self.canvas.itemconfig(self.question_text, text="You've completed the quiz!")
            self.Option_A.config(text="")
            self.Option_B.config(text="")
            self.Option_C.config(text="")
            self.Option_D.config(text="")

    def check_answer(self, selected_button):
        correct_answer = self.quiz.current_question.answer
        selected_text = selected_button.cget("text")

        if self.quiz.check_answer(selected_text):
            selected_button.config(bg="green")
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            selected_button.config(bg="red")
            for button in [self.Option_A, self.Option_B, self.Option_C, self.Option_D]:
                if button.cget("text") == correct_answer:
                    button.config(bg="green")

        self.window.after(1000, self.get_next_question)


