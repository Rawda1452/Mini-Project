import turtle

# Create window
wind = turtle.Screen()
wind.title("Pong Game") 
wind.bgcolor("black")
wind.setup(width=800, height=600)

# Paddle 1
paddel1 = turtle.Turtle()
paddel1.speed(0)
paddel1.shape("square")
paddel1.color("red")
paddel1.shapesize(stretch_wid=6, stretch_len=1)
paddel1.penup()
paddel1.goto(-350, 0)

# Paddle 2
paddel2 = turtle.Turtle()
paddel2.speed(0)
paddel2.shape("square")
paddel2.color("green")
paddel2.shapesize(stretch_wid=6, stretch_len=1)
paddel2.penup()
paddel2.goto(350, 0)

#The Ball
ball=turtle.Turtle()
ball.speed(0)
#shape and color
ball.shape("circle")  
ball.color("white") 
#not to draw lines when move
ball.penup()  
#set the ball in centre
ball.goto(400, 0)
#ball moves by 2 every time
ball.dx=2
ball.dy=-2


# score text
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.goto(x=0, y=260)
score.write("Player1: 0 Player2: 0", align="center",
            font=("Courier", 14, "normal"))
score.hideturtle()  # we hide the object because we only want to see the text
p1_score, p2_score = 0, 0  # variables to hold player 1 & player 2 scores


# Paddle1 up and down 
def paddel1_up():
    y = paddel1.ycor() # get y coordinate of the paddle1
    y += 20  # set the y to increase by 20 
    paddel1.sety(y) # set the y of paddle1 to the new y coordinate 

def paddel1_down():
    y = paddel1.ycor() 
    y -= 20    # set the y to  decrease by 20 
    paddel1.sety(y)

# Paddle2 up and down 
def paddel2_up():
    y = paddel2.ycor() # get y coordinate of the paddle1
    y += 20  # set the y to increase by 20 
    paddel2.sety(y) # set the y of paddle1 to the new y coordinate 

def paddel2_down():
    y = paddel2.ycor() 
    y -= 20    # set the y to  decrease by 20 
    paddel2.sety(y)


# Keyboard
wind.listen() # tell the window to expect input 
wind.onkeypress(paddel1_up, "w") # by pressing w , function paddel1_up is invoked 
wind.onkeypress(paddel1_down, "s")

# Main loop 
while True:
     wind.update() # updates the screen everytime the loop run 
     ball.setx(ball.xcor()+ball.dx)  
     ball.sety(ball.ycor()+ball.dy)
     #the ball cant move out of the screen
     if ball.ycor()>290:
         ball.sety(290)
         #and reverse the direction
         ball.dy*=-1
         #same
     if ball.ycor()<-290:
         ball.sety(-290)
         ball.dy*=-1
         #same in right and left sides
     if ball.xcor()>390:
         ball.goto(0,0)
         ball.dx*=-1
         score.clear()
         p1_score += 1
         score.write(f"Player1: {p1_score} Player2: {p2_score}", align="center",
                    font=("Courier", 14, "normal"))


     if ball.xcor()<-390:
         ball.goto(0,0)
         ball.dx*=-1
         score.clear()
         p2_score += 1
         score.write(f"Player1: {p1_score} Player2: {p2_score}", align="center",
                    font=("Courier", 14, "normal"))

          #ball rebound
   #ball between top and bottom of paddle
     if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<paddel2()+50 and ball.ycor()>paddel2()-50):
         ball.setx(350)
    #reverse direction
         ball.dx*=-1
    #same
     if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<paddel1()+40 and ball.ycor()>paddel1()-40):
         ball.setx(-350)
    #reverse direction
         ball.dx*=-1
#paddel2 computer player
     if paddel2.ycor() < ball.ycor() and abs(paddel2.ycor() - ball.ycor()) > 10:
         paddel2_up()
     if paddel2.ycor() > ball.ycor() and abs(paddel2.ycor() - ball.ycor()) > 10:
         paddel2_down()