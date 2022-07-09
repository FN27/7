import tkinter
window=tkinter.Tk()
def get_num1():
    num1=text_num1.get()
    num1=(int(num1))
    return num1
def get_num2():
    num2=text_num2.get()
    num2=(int(num2))
    return num2
def set_answere(a):
    text_answer.delete(0,'end')
    text_answer.insert(0,a)
    
def add():
    num1=get_num1()
    num2=get_num2()
    res=num1+num2
    set_answere(res)

def sub():    
    num1=get_num1()
    num2=get_num2()
    res=num1-num2
    set_answere(res)

def x():    
    num1=get_num1()
    num2=get_num2()
    res=num1 * num2
    set_answere(res)

def y():
    num2=get_num2()
    num1=get_num1()
    res=num1 / num2
    set_answere(res)
    


window.title("Мой калькулятор")
window.geometry('300x300')
window.configure(bg='grey')
text1=tkinter.Label(window,text='Введите второе число',bg="yellow")
text1.place(x=95,y=20)
text2=tkinter.Label(window,text='Введите второе число',bg='yellow')
text2.place(x=95,y=61)
text3=tkinter.Label(window,text='Ответ',bg="yellow")
text3.place(x=95,y=200)
button_add=tkinter.Button(window,text="+",command=add,width=7,height=2)
button_add.place(x=95,y=110)
button_m=tkinter.Button(window,text="-",command=sub,width=7,height=2)
button_m.place(x=160,y=110)
button_x=tkinter.Button(window,text='*',command=x,width=7,height=2)
button_x.place(x=95,y=154)
button_y=tkinter.Button(window,text=':',command=y,width=7,height=2)
button_y.place(x=160,y=154)

text_num1=tkinter.Entry(window,width=20)
text_num1.place(x=95,y=40)
text_num2=tkinter.Entry(window,width=20)
text_num2.place(x=95, y=81)
text_answer=tkinter.Entry(window, width=20)
text_answer.place(x=95, y=221)
window.mainloop()


##Написать функцию, принимающую три числа и возвращающую самое маленькое из них.
##Написать функцию для расчета площади круга - функция принимает значение радиуса
##r и вычисляет площадь по формуле S=π* r*r, где S - площадь круга, π = 3.14, r -
##радиус круга. Вычисленное значение функция возвращает в место своего вызова





