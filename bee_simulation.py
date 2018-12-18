import turtle
import random

startx = 0
starty = 0
# number of bees mus be > 1
num_of_bees = 1

beeShape = "BEE/BeeImg.gif"
# empty list to store bees agent
bees = []

environment = turtle.Screen()
environment.setup(800, 800, startx, starty)
environment.bgcolor("black")
environment.title("Bee Simulation Environment")
#environment.addshape(beeShape)
environment.register_shape(beeShape)
#environment.tracer(0)


for _ in range(num_of_bees):
    bees.append(turtle.Turtle())

for bee in bees:
    bee.color("yellow")
    bee.shape("circle")
    bee.shapesize(1, 2, 1)


while True:
    #environment.update()

    for bee in bees:
        bee.forward(1)
        #angle = random.randint(-180, 180)
        #bee.left(angle)
        #bee.heading()
         

#environment.mainloop()
environment.exitonclick()