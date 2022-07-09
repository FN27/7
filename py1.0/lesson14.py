import turtle
t=turtle.Turtle()
t.speed(10)
t.shape('turtle')
def scuear():
    for s in range(4):
        t.forward(100)
        t.left(90)
def move(x,y):
    t.up()
    t.goto(x,y)
    t.down()
def pentagon():
    for s in range(5):
        t.forward(100)
        t.left(72)
def polegon(sides, long):
    for s in range(sides):
        t.forward(long)
        t.left(360/sides)
def uzor():
    for s in range(60):
        polegon(5,50)
        t.left(6)
def circle():
    for s in range(60):
        t.forward(10)
        t.left(6)
def spiral():
    for s in range(160):
        t.forward(s/10)
        t.left(15)
def star():
    for s in range(5):
        t.forward(100)
        t.left(144)
def olimpick(x,y,color):
    t.color(color)
    t.width(10)
    move(x,y)
    circle()
def olimpick_logo():
    olimpick(-120,60,'blue')
    olimpick(0,60,'black')
    olimpick(120,60,'red')
    olimpick(-60,0,'yellow')
    olimpick(60,0,'green')
def rainbow():
    f=16
    for s in range(8):
        g=10-1.5
    t.up()
    t.goto(-10,60)
    t.down()
    t.setheading(90)
    t.width(15)
    t.color('red')
    for s in range(f):
        t.forward(10)
        t.right(6)
    t.up()
    t.goto(4, 60)
    t.down()
    t.setheading(90)
    t.width(15)
    t.color('orange')
    for s in range(f):
        t.forward(g)
        t.right(6)
    t.up()
    t.goto(18, 60)
    t.down()
    t.setheading(90)
    t.width(15)
    t.color('yellow')
    for s in range(f):
        t.forward(g-1.4)
        t.right(6)
    t.up()
    t.goto(18+14, 60)
    t.down()
    t.setheading(90)
    t.width(15)
    t.color('green')
    for s in range(f):
        t.forward(7.2-1.4)
        t.right(6)
    t.up()
    t.goto(18 + 14 + 14, 60)
    t.down()
    t.setheading(90)
    t.width(15)
    t.color('blue')
    for s in range(f):
        t.forward(7.2 - 1.4 - 1.4)
        t.right(6)
    t.up()
    t.goto(18 + 14 + 14+14, 60)
    t.down()
    t.setheading(90)
    t.width(15)
    t.color('cyan')
    for s in range(f):
        t.forward(7.2 - 1.4 - 1.4-1.4)
        t.right(6)
    t.up()
    t.goto(18 + 14 + 14 + 14+14, 60)
    t.down()
    t.setheading(90)
    t.width(15)
    t.color('purple')
    for s in range(f):
        t.forward(7.2 - 1.4 - 1.4 - 1.4-1.4)
        t.right(6)
    t.up()
    t.goto(18 + 14 + 14 + 14 + 14+14, 60)
    t.down()
    t.setheading(90)
    t.width(15)
    t.color('white')
    for s in range(f):
        t.forward(7.2 - 1.4 - 1.4 - 1.4 - 1.4-1.4)
        t.right(6)
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
def red():
    t.color('red')
t.screen.onkeypress(rainbow,'s')
t.screen.onkeypress(red,'r')
t.screen.onkeypress(up,'Up')
t.screen.onkeypress(up_or_down,'space')
t.screen.onkeypress(down,'Down')
t.screen.onkeypress(left,'Left')
t.screen.onkeypress(right,'Right')
t.screen.listen()


#Сделать функцию отрисовки радуги. (Подсказка: дуга - это половина круга, т.е. произведение угла поворота на количество повторов должно быть равно 180. Чтобы следующая дуга была меньше предыдущей - уменьшаем длину линии)
#tkinter-подготовится
#for s in range(24):
#    polegon(10,50)
#    t.left(15)
#polegon(8,100)
t.screen.mainloop()
#Сделать улучшенную функцию многоугольника, чтобы она принимала количество сторон и длину стороны
#Написать функции смены цвета линии и присвоить их клавишам букв - например, клавиша "b" меняет цвет на голубой ("blue"), клавиша "y" - на желтый ("yellow"), "g" - на зеленый("green").
#Сделать функцию отрисовки радуги. (Подсказка: дуга - это половина круга, т.е. произведение угла поворота на количество повторов должно быть равно 180. Чтобы следующая дуга была меньше предыдущей - уменьшаем длину линии)
