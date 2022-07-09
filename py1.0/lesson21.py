import tkinter as tk
import  random
import time
colors=['black','red','white','pink','blue','yellow','green']
stop=False
def moove_circle():
    global stop
    d = random.randint(1, 100)
    x = random.randint(0, 500 - d)
    y = random.randint(0, 500 - d)
    color=random.choice(colors)
    circle=canvas.create_oval(x,y,x+d,y+d,fill=color)
    dx=1
    dy=2
    while True:
        coords = canvas.coords(circle)
        left=coords[0]
        top=coords[1]
        right=coords[2]
        buttom=coords[3]
        if left<=0 or right>=500:
            dx=-dx
        if top<=0 or buttom>=500:
            dy=-dy
        canvas.move(circle,dx,dy)
        time.sleep(0.01)
        if stop:
            stop=False
            break
        window.update()
def stop_draw():
    global stop
    stop=True
def unlimit_scuear():
    global  stop
    while True:
        draw_scueare()
        window.update()
        time.sleep(1)
        if stop:
            stop=False
            break
def draw_circle():
    d=random.randint(1,100)
    x=random.randint(0,500-d)
    y=random.randint(0,500-d)
    color=random.choice(colors)
    canvas.create_oval(x,y,x+d,y+d,fill=color)
def draw_scueare():
    d=random.randint(1,100)
    x=random.randint(0,500-d)
    y=random.randint(0,500-d)
    color=random.choice(colors)
    canvas.create_rectangle(x,y,x+d,y+d,fill=color)
def draw_oval():
    d=random.randint(1,100)
    d2=random.randint(1,100)
    x=random.randint(0,500-d)
    y=random.randint(0,500-d2)
    color=random.choice(colors)
    canvas.create_oval(x,y,x+d,y+d2,fill=color)
def unlimit_circle():
    global  stop
    while True:
        draw_circle()
        window.update()
        time.sleep(1)
        if stop:
            stop=False
            break
window=tk.Tk()
window.title('Программа')
window.geometry('650x500')
stop_butt=tk.Button(width=17,text='Пауза',command=stop_draw)
stop_butt.place(x=510,y=140)
button_moove_circle=tk.Button(window,width=17,text='Рисорвать движущейся круг',command=moove_circle)
button_moove_circle.place(x=510,y=200)
button_draw=tk.Button(window,width=17,text='Рисорвать круг',command=draw_circle)
button_draw.place(x=510,y=20)
button_draw_rect=tk.Button(window,width=17,text='Рисорвать квадрат',command=draw_scueare)
button_draw_rect.place(x=510,y=50)
button_draw_oval=tk.Button(window,width=17,text='Рисорвать овал',command=draw_oval)
button_draw_oval.place(x=510,y=80)
button_draw_oval_ever=tk.Button(window,width=17,text='Бесконечно рисорвать овал',command=unlimit_circle)
button_draw_scirkle_ever=tk.Button(window,width=17,text='Бесконечно рисорвать квадрат',command=unlimit_scuear)
button_draw_scirkle_ever.place(x=510,y=170)
button_draw_oval_ever.place(x=510,y=110)
canvas=tk.Canvas(window,width=500,height=500,bg='white')
canvas.place(x=0,y=0)
window.mainloop()
#Сделать функцию бесконечных квадратов, тоже с остановкой.
