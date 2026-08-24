import turtle

screen = turtle.Screen()
screen.title("Colorful Turtle Graphics Project")
screen.bgcolor("skyblue")

t = turtle.Turtle()
t.speed(5)   
t.width(2)


def rectangle(color, width, height):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()


def triangle(color, size):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    t.end_fill()


def circle(color, radius):
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()




t.penup()
t.goto(-400, -250)
t.pendown()
rectangle("green", 800, 150)


t.penup()
t.goto(-100, -100)
t.pendown()
rectangle("lavender", 200, 150)

t.penup()
t.goto(-120, 80)
t.pendown()
triangle("saddlebrown", 240)

t.penup()
t.goto(-20, -100)
t.pendown()
rectangle("cyan", 40, 90)

for x in [-80, 40]:
    t.penup()
    t.goto(x, -20)
    t.pendown()
    rectangle("lightblue", 40, 40)


t.penup()
t.goto(-280, -100)
t.pendown()
rectangle("brown", 40, 120)

t.penup()
t.goto(-300, 20)
t.pendown()
circle("darkgreen", 40)

t.penup()
t.goto(-250, 10)
t.pendown()
circle("green", 45)

t.penup()
t.goto(-330, 10)
t.pendown()
circle("forestgreen", 30)



def flower(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

    t.color("green")
    t.setheading(90)
    t.forward(40)

    t.penup()
    t.goto(x, y + 40)
    t.pendown()

    colors = ["red", "pink", "purple", "orange", "magenta"]

    for c in colors:
        t.fillcolor(c)
        t.begin_fill()
        t.circle(8)
        t.end_fill()
        t.left(72)

    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(10)
    t.end_fill()


flower(120, -50)
flower(180, -70)
flower(240, -60)


 


for x in range(-150, 351, 30):
    t.penup()
    t.goto(x, -100)
    t.pendown()
    rectangle("burlywood", 10, 60)

t.penup()
t.goto(-350, -60)
t.pendown()
rectangle("burlywood", 700, 8)

t.penup()
t.goto(-350, -30)
t.pendown()
rectangle("burlywood", 700, 8)


t.hideturtle()
turtle.done()
