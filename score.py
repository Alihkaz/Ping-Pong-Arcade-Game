#
from turtle import Turtle


class Scoreboard(Turtle):

  
  def __init__(self):
    super().__init__()
    self.hideturtle()
    self.color("white")
    self.penup()
    self.l_score=0
    self.r_score=0
    self.update_scoreboard()

    
  def update_scoreboard(self):
    self.clear()
    self.goto(-100,150)
    self.write(self.l_score,align="center",font=("Courier",45,"normal"))
    self.goto(100,150)
    self.write(self.r_score,align="center",font=("Courier",45,"normal"))


  def give_l_point(self):
    self.l_score+=1
    self.update_scoreboard()
    
  def give_r_point(self):
    self.r_score+=1
    self.update_scoreboard()
    