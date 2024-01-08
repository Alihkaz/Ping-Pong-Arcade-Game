#
from turtle import Turtle 

class Paddle(Turtle) :
   def __init__(self,position):
      super().__init__()
      self.shape("square")
      self.color("white")
      self.shapesize(5,stretch_len=1)
      self.penup()
      self.goto(position)

  

   def go_upside(self):
       new_y=self.ycor()+22
       self.goto(self.xcor(),new_y)

   def go_downside(self):
       new_y=self.ycor()-22
       self.goto(self.xcor(),new_y)
        
  
