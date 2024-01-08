#
from turtle import Turtle
class Ball(Turtle): #inheriting from the turtle class 

  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.color("white")
    self.shapesize(1.2, 1.2)
    self.penup()
    self.x_move = 10
    self.y_move = 10
    self.moving_speed=0.3


  
  def move(self):
    new_x = self.xcor() + self.x_move
    new_y = self.ycor() + self.y_move
    self.goto(new_x, new_y)

  def shift_y(self):
    self.y_move *= -1
    self.moving_speed*=0.9
    
  def shift_x(self):
    self.x_move *= -1
    self.moving_speed*=0.9



  def restart(self):
    self.goto(0,0)
    self.moving_speed=0.2
    self.shift_x()

  def increase_speed(self):
    self.speed("fast")

