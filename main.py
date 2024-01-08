#imports
from turtle import  Screen,Turtle
from paddlemove import Paddle
from ball import Ball
from score import Scoreboard
import time


#-----------------------UI Set UP-------------------------------
window=Screen()
window.setup(width=700,height=700)
window.bgcolor("black")
window.tracer(0)


ri_paddle=Paddle((230,0))
le_paddle=Paddle((-230,0))
scoreboard=Scoreboard()
ball=Ball()




#-----------------------Listening to the player And setting up the Controllers -------------------------------

window.listen()
window.onkey(ri_paddle.go_upside,"Up")
window.onkey(ri_paddle.go_downside,"Down")
window.onkey(le_paddle.go_upside,"w")
window.onkey(le_paddle.go_downside,"s")




#-----------------------Starting The Game-------------------------------


game__on=True
while game__on:
  
  #to reduce the noise , we will let the screen slepp depending on the speed of the b all
  time.sleep(ball.moving_speed)
  window.update()
  ball.move()
  
  #If the ball hits the upper or the down side let it bounce and shift the y direction
  if ball.ycor()>150 or ball.ycor()<-150:
    ball.shift_y()

  #If the ball hits right side and the right player miss , give a point to the left player 
  if (ball.distance(ri_paddle)>25 and ball.xcor()>230) :
      ball.restart()
      scoreboard.give_l_point()

  #If the ball hits left side and the left player miss , give a point to the right player   
  if (ball.distance(le_paddle)>25 and ball.xcor()<-230):
    ball.reset()
    scoreboard.give_r_point()
   

  #If the ball hits right paddle or the left paddle , let it bounce and increase the speed of the ball 
  if (ball.distance(ri_paddle)<25 and ball.xcor()>210) or (ball.distance(le_paddle)<25 and ball.xcor()<-210):
    ball.increase_speed()
    ball.shift_x()



window.exitonclick()

