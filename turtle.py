import turtle, random
from turtle import *

t = turtle.Turtle()
t.speed(0)

def int_to_hexcode(x):
    a = str(hex(x))
    a = a[2:]
    while len(a) < 2:
        a = "O" + a
    return "#" + a*3

def meteor(trailLength):
    width = 1
    t.color("black")
    for i in range(0,255,trailLength):
        t.width(width)
        t.color(int_to_hexcode(i))
        t.forward(1)
        width += 0.2 
    t.right(random.randint(-50,50))

def swirl():
    colors = ['indigo']
    for i in range(700):
        color(colors[i % len(colors)])
        width(i / 80)
        forward(i/100)
        right(1)


    
def draw_star(color,width):
    t.color(color)
    t.width(width)
    t.forward(1)

def set_scene(x):
    t.color(x)
    t.width(9999)
    t.forward(1)
    t.width(1)
    
def position():
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw_galaxy():
    set_scene("black")
    swirl()
    for a in range(3):
        position()
        meteor(3)
    for i in range(0,255):
        position()
        color = int_to_hexcode(i)
        draw_star(color,random.randint(1,3))
    
draw_galaxy()
