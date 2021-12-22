import turtle as t
import random

def get_length_of_line():
    length = input('Enter line length from following: [long, medium, short] -->')

    if length == 'long':
        line_length = 250
    elif length == 'medium':
        line_length = 200
    else:
        line_length = 100
    return line_length

def get_width_of_line():
    width = input("Enter the width from the following: [superthick,thick,thin] --->")
    if width == 'superthick':
        line_width = 40
    elif width == 'thick':
        line_width = 25
    else:
        line_width = 10
    return line_width

def inside_window():
    left_limit = (-t.window_width()/2)+100
    right_limit = (t.window_width()/2)-100
    top_limit = (t.window_height()/2)-100
    bottom_limit = (-t.window_height()/2)+100
    (x,y) = t.pos()
    inside = left_limit <x<right_limit and bottom_limit <y<top_limit
    return inside

def move_turtle(line_length):
    pen_colors = ['red','green','orange','yellow','blue','purple']
    t.pencolor(random.choice(pen_colors))
    if inside_window():
        angle = random.randint(0,180)
        t.right(angle)
        t.forward(line_length)
    else:
        t.backward(line_length)

line_width = get_width_of_line()
line_length = get_length_of_line()

t.shape('turtle')
t.fillcolor('green')
t.bgcolor('black')
t.speed('fastest')
t.pensize(line_width)

while True:
    move_turtle(line_length)
