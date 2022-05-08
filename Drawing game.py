from turtle import *
t = Turtle()
t.color('black')
t.width(5)
t.shape('classic')
t.pendown()
t.speed(0)
s=getscreen()
s.listen()
print('''  Drawing game\n\nButton list:
                                                                                            
colors:                                                                                          
from 1 to 6

shapes:
from 7 to 0

controls:
1- w = forward
2- s = backward
3- d = right(in degrees)
4- a = left(in degrees)
5- e = penup
6- r = pendown
7- f = goto x0,y0(penup and pendown your self)
8- v = show turtle
9- c = hide turtle
10- x = end fill
11- z = begin fill 
12- q = restart\n\n     >!Buttons on keyboard!<''')
# colors
def color():
    t.color('red')
s.onkey(color,'1')
def color():
    t.color('purple')
s.onkey(color,'2')
def color():
    t.color('blue')
s.onkey(color,'3')
def color():
    t.color('orange')
s.onkey(color,'4')
def color():
    t.color('white')
s.onkey(color,'5')
def color():
    t.color('black')
s.onkey(color,'6')
# shapes
def shape():
    t.shape('square')
s.onkey(shape,'7')
def shape():
    t.shape('triangle')
s.onkey(shape,'8')
def shape():
    t.shape('circle')
s.onkey(shape,'9')
def shape():
    t.shape('classic')
s.onkey(shape,'0')
# Movments
def forward():
    t.forward(5)
s.onkey(forward,'w')
def backward():
    t.backward(5)
s.onkey(backward,'s')
def right():
    t.right(5)
s.onkey(right,'d')
def left():
    t.left(5)
s.onkey(left,'a')
# pen controls
def penup():
    t.penup()
s.onkey(penup,'e')
def pendown():
    t.pendown()
s.onkey(pendown,'r')
def begin_fill():
    t.begin_fill()
s.onkey(begin_fill,'z')
def end_fill():
    t.end_fill()
s.onkey(end_fill,'x')
def hide_turtle():
    t.hideturtle()
s.onkey(hide_turtle,'c')
def show_turtle():
    t.showturtle()
s.onkey(show_turtle,'v')
def goto00():
    t.goto(0,0)
s.onkey(goto00,'f')
# restart
def restart():
    t.penup()
    t.showturtle()
    t.end_fill()
    t.goto(0,0)
    t.pendown()
    t.color('black')
    t.shape('classic')
    t.setheading(0)
    t.clear()
s.onkey(restart,'q')
