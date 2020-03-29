import turtle
import os

window = turtle.Screen()
window.title('Pong')
window.bgpic('background.png')
window.setup(width = 800,height = 600)
window.tracer(0)

# paddle a
paddle_a = turtle.Turtle()
paddle_a.shape('square')
paddle_a.penup()
paddle_a.goto(-380,0)
paddle_a.color('white')
paddle_a.shapesize(stretch_wid = 5, stretch_len = 1)

# paddle b
paddle_b = turtle.Turtle()
paddle_b.shape('square')
paddle_b.penup()
paddle_b.goto(370,0)
paddle_b.color('white')
paddle_b.shapesize(stretch_wid = 5, stretch_len = 1)

# ball
ball = turtle.Turtle()
ball.shape('circle')
ball.penup()
ball.goto(0,0)
ball.color('white')
dx = 3
dy = 3

# sounds
def play_sound():
    if os.sys.platform == 'darwin':
        os.system('afplay bounce.wav&')
    elif os.sys.platform == 'win64':
        os.play_sound('bounce.wav',os.SND_ASYNC)
    else:
        os.system('aplay bounce.wav&')

# paddle movement
# paddle up
def paddle_up_a():
    if paddle_a.ycor() < 250:
        paddle_a.sety(paddle_a.ycor()+20)

def paddle_up_b():
    if paddle_b.ycor() < 250:
        paddle_b.sety(paddle_b.ycor()+20)

# paddle down
def paddle_down_a():
    if paddle_a.ycor() > -240:
        paddle_a.sety(paddle_a.ycor()-20)

def paddle_down_b():
    if paddle_b.ycor() > -240:
        paddle_b.sety(paddle_b.ycor()-20)

# score
score_a = 0
score_b = 0
pen = turtle.Turtle()
pen.goto(0,270)
pen.hideturtle()
pen.clear()
pen.color('white')
pen.write('Player A {}  Player B {}'.format(score_a,score_b),False, align='center',font=('Courier',24))

# listen for key strokes
window.listen()
window.onkeypress(paddle_up_a, 'w')
window.onkeypress(paddle_up_b, 'Up')
window.onkeypress(paddle_down_a, 's')
window.onkeypress(paddle_down_b, 'Down')


while True:
    # check to see if ball is touching the top and bottom of screen/window
    if ball.ycor()>290 or ball.ycor() < -290:
        dy = -dy
        play_sound()
    # check to see if the ball is touching the paddles
    if ball.ycor() > paddle_a.ycor()-50 and ball.ycor() < paddle_a.ycor()+50 and ball.xcor() == paddle_a.xcor()+20:
        dx = -dx
        play_sound()
    if ball.ycor() > paddle_b.ycor()-50 and ball.ycor() < paddle_b.ycor()+50 and ball.xcor() == paddle_b.xcor()-10:
        dx = -dx
        play_sound()
    # check to see if ball is out of screen, reset its position and increase score
    if ball.xcor() > 400:
        score_a += 1
        ball.setpos(0,0)
        pen.clear()
        pen.write('Player A {}  Player B {}'.format(score_a,score_b),False, align='center',font=('Courier',24))
    if ball.xcor() < -400:
        score_b += 1
        ball.setpos(0,0)
        pen.clear()
        pen.write('Player A {}  Player B {}'.format(score_a,score_b),False, align='center',font=('Courier',24))
        # move the ball continuously
    ball.setpos(ball.xcor()+dx,ball.ycor()+dy)
    window.update()