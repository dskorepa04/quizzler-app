from tkinter import *
from tkinter import Canvas
from quiz_brain import QuizBrain
import datetime
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx= 20, pady= 20, bg = THEME_COLOR)

        self.score = Label(text= "Score: 0", fg= 'white', bg= THEME_COLOR)
        self.score.grid(column= 1, row= 0)

        self.canvas = Canvas(width= 300, height= 250, bg= 'white')
        self.question_text = self.canvas.create_text(150,125,width= 280, text= "", font= ("Arial", 20, "italic"), fill= THEME_COLOR)
        self.canvas.grid(column= 0, row= 1, columnspan= 2, pady= 50)


        # self.question = Label(text= 'text', font= ("Arial", 20, "italic"), fg= 'black', bg= 'white')
        # self.question.grid(column= 0, row= 1, columnspan= 2)

        self.true_photo = PhotoImage(file= '/Users/davidskorepa/Desktop/coding/Main/Projects/100 days of code/Day 34./quizzler-app-start/images/true.png')
        self.true = Button(image= self.true_photo, highlightthickness= 0, command= self.true_pressed)
        self.true.grid(column= 0, row= 2)

        self.false_photo = PhotoImage(file= '/Users/davidskorepa/Desktop/coding/Main/Projects/100 days of code/Day 34./quizzler-app-start/images/false.png')
        self.false = Button(image= self.false_photo, highlightthickness= 0, command= self.false_pressed)
        self.false.grid(column= 1, row= 2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg= 'white')
        if self.quiz.still_has_questions():
            self.score.config(text= f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text= q_text)
        else:
            self.canvas.itemconfig(self.question_text, text= "You reached the end of the quiz")
            self.true.config(state= 'disabled')
            self.false.config(state= 'disabled')

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right == True:
            self.canvas.config(bg= 'green')
            # self.window.after(1000, self.get_next_question())
            # self.get_next_question()
        else:
            self.canvas.config(bg = 'red')
        self.window.after(1000, self.get_next_question)

