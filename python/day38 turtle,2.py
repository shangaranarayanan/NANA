from turtle import *

'''forward(100)

left(120)

forward(100)

right(40)
backward(100)
backward(50)
done()'''

'''color('blue')
width(3)
forward(100)

left(120)

forward(100)


home()
print(pos())
clearscreen()
done()'''

'''color('red')
fillcolor('yellow')
begin_fill()
for i in range(4):
    forward(100)
    right(90)
end_fill()
home()
print(pos())

done()'''

# forward(200)
# clearscreen()
'''
hideturtle()
showturtle()
forward(100)
right(85)
forward(96)
clear()
forward(100) 
'''
# shape("turtle")
# forward(200)

"""forward(85)
left(30)
forward(90)
reset()
forward(50)""" 

# Square
'''
for i in range(4):
    forward(100)
    right(90)
clearscreen()
'''
# Circle
# circle(100)
#clearscreen()
'''
# star
right(74)
forward(100)
for i in range(4):
    right(144)
    forward(100)
'''
'''
# Hexagon
side=6
for i in range(6):
    forward(80)
    right(360/6)
'''

'''
# parallelogram
for i in range(2):
    forward(130)
    right(60)
    forward(50)
    right(120)
'''

'''
import turtle  
wn = turtle.Screen()
wn.bgcolor("light blue")
skk = turtle.Turtle()
skk.color("blue")

def sqrfunc(size):
    for i in range(4):
        skk.fd(size)
        skk.left(90)
        size = size + 5

sqrfunc(6)
sqrfunc(26)
sqrfunc(46)
sqrfunc(66)
sqrfunc(86)
sqrfunc(106)
sqrfunc(126)
sqrfunc(146)
'''

'''
import turtle
loadWindow = turtle.Screen()
turtle.speed(0)

for i in range(100000000000):
    turtle.circle(5*i)
    turtle.circle(-5*i)
    turtle.left(i)

turtle.exitonclick()
'''

'''
import turtle
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
    t.speed(0)
    t.pencolor(colors[x%6])
    t.width(x//100 + 1)
    t.forward(x)
    t.left(59) 
'''

'''
from turtle import *
color('red')
fillcolor('yellow')
begin_fill()
while True:
    speed(0)
    # screen.delay(5)
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
#clearscreen()
'''

'''
import turtle

screen = turtle.Screen()
screen.title("Click the Turtle!")

my_turtle = turtle.Turtle()
my_turtle.shape("turtle") 
my_turtle.color("green")
my_turtle.penup() 

def move_to_click(x, y):
    my_turtle.goto(x, y)
    print(f"Turtle moved to: ({x}, {y})")

screen.onclick(move_to_click)

screen.mainloop()
'''

'''
import turtle

screen = turtle.Screen()
screen.title("Click the Turtle!")

my_turtle = turtle.Turtle()
my_turtle.shape("turtle") 
my_turtle.color("green")
my_turtle.penup() 

def move_to_click(x, y):
    my_turtle.goto(x, y)
    print(f"Turtle moved to: ({x}, {y})")

screen.onclick(move_to_click)

screen.mainloop()
'''

