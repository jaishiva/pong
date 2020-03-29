import turtle

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
dx = 2
dy = 2
# paddle movement
# paddle up
def paddle_up_a():
    if paddle_a.ycor() < 250:
        paddle_a.sety(paddle_a.ycor()+10)

def paddle_up_b():
    paddle_b.sety(paddle_b.ycor()+10)

# paddle down
def paddle_down_a():
    paddle_a.sety(paddle_a.ycor()-10)

def paddle_down_b():
    paddle_b.sety(paddle_b.ycor()-10)

# listen for key strokes
window.listen()
window.onkeypress(paddle_up_a, 'w')
window.onkeypress(paddle_up_b, 'Up')
window.onkeypress(paddle_down_a, 's')
window.onkeypress(paddle_down_b, 'Down')


while True:
    ball.setpos(ball.xcor()+dx,ball.ycor()+dy)
    if ball.ycor()>290 or ball.ycor() < -290:
        dy = -dy
    if ball.xcor() > 390 or ball.xcor() < -390:
        dx = -dx
    window.update()