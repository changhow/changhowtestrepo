import turtle
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("bouncing ball simulator")
wn.tracer(0.01)

balls = []

for _ in range(1):
    balls.append(turtle.Turtle())

colors = ["red", "blue", "yellow", "green", "white", "purple"]
shapes = ["circle", "triangle", "square"]

for ball in balls:
#    ball = turtle.Turtle()
    ball.shape(random.choice(shapes))
    ball.color(random.choice(colors))
    ball.penup()
    ball.speed(0)
    x = random.randint(-290, 290)
    y = random.randint(200, 400)
    ball.goto(x, y)
    ball.dy = 0
    ball.dx = random.randint(-3, 3)
    ball.da = random.randint(-5, 5)

gravity = 0.1
drag = 0.1

while True:
    wn.update()

    for ball in balls:
        ball.rt(ball.da)
        ball.dy -= gravity
        ball.dx -= drag
        ball.sety(ball.ycor() + ball.dy)
        ball.setx(ball.xcor() + ball.dx)

        if ball.xcor() > 300:
            ball.setx(300)
            ball.dx *= -1
            ball.da *= -1

        if ball.xcor() < -300:
            ball.setx(-300)
            ball.dx *= -1
            ball.da *= -1

        if ball.ycor() < -300:
            ball.color(random.choice(colors))
            ball.sety(-301)
            ball.dy *= -1
        



wn.mainloop()