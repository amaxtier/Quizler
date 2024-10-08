from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
  def __init__(self, quiz_brain: QuizBrain):
    self.quiz = quiz_brain
    self.window = Tk()
    self.window.title("Quizzler")
    self.window.config(bg=THEME_COLOR)

    # images
    true_image = PhotoImage(file="quizzler_app_start/images/true.png")
    false_image = PhotoImage(file="quizzler_app_start/images/false.png")
    #  Buttons
    self.true_button = Button(image=true_image, highlightthickness=0, bg=THEME_COLOR,
    relief="flat", command =self.true_pressed)
    self.true_button.grid(row=2, column=0, pady=20)

    self.false_button = Button(image=false_image, highlightthickness=0, bg=THEME_COLOR, 
    relief="flat", command=self.false_pressed)
    self.false_button.grid(row=2, column=1, pady=20)
    # label
    self.label = Label(
      font=("Arial", 20,"italic"), 
      text=f"Score: {self.quiz.score}", 
      bg=THEME_COLOR,fg="white"
    )
    self.label.grid(row=0, column=1, pady=20)
    # canvas
    self.canvas = Canvas(width=300, height=250) 
    self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
    self.canvas_text = self.canvas.create_text(
      150, 
      125, 
      text="", 
      fill=THEME_COLOR, 
      width=280
    )

    self.get_next_question()
    
    
    self.window.mainloop()

  def get_next_question(self):
    self.canvas.config(bg="white")
    if self.quiz.still_has_questions():
      q_text = self.quiz.next_question()
      self.label.config(text=f"Score: {self.quiz.score}")
      self.canvas.itemconfig(self.canvas_text, text=q_text)
      self.true_button.config(state="active")
      self.false_button.config(state="active")
    else:
      self.canvas.itemconfig(self.canvas_text, text="You've reached the end of the quiz.")
      self.true_button.config(state="disabled")
      self.false_button.config(state="disabled")

  def true_pressed(self):
    self.give_feedback(self.quiz.check_answer("True"))

  def false_pressed(self):
    self.give_feedback(self.quiz.check_answer("False"))

  def give_feedback(self, is_right: bool):
    if is_right:
      self.canvas.config(bg="green")
      self.true_button.config(state="disabled")
      self.false_button.config(state="disabled")
    else:
      self.canvas.config(bg="red")
      self.true_button.config(state="disabled")
      self.false_button.config(state="disabled")
      
    self.window.after(1000, self.get_next_question)
