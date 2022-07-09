import turtle
t=turtle.Turtle()
t.speed(10)
t.shape('turtle')
def yellow():
    t.color('yellow')
def blue():
    t.color('blue')
def green():
    t.color('green')
def up():
    t.setheading(90)
    t.forward(10)
def down():
    t.setheading(-90)
    t.forward(10)
def left():
    t.setheading(180)
    t.forward(10)
def right():
    t.setheading(0)
    t.forward(10)
def up_or_down():
    if t.isdown():
        t.up()
    else:
        t.down()
t.screen.onkeypress(green,'g')
t.screen.onkeypress(yellow,'y')
t.screen.onkeypress(blue,'b')
t.screen.onkeypress(up,'Up')
t.screen.onkeypress(up_or_down,'space')
t.screen.onkeypress(down,'Down')
t.screen.onkeypress(left,'Left')
t.screen.onkeypress(right,'Right')
t.screen.listen()
t.screen.mainloop()


