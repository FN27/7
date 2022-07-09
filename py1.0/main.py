import tkinter as tk
import tkinter.messagebox as mbox
import random
window=tk.Tk()
score=0
folse=0
time_left=30
colors=['red','blue','green','pink','black','yellow','orange','purple','brown','white']
def new_word():
    color_label['fg']=random.choice(colors)
    color_label['user_health']=random.choice(colors)
def timer():
    global time_left
    if time_left>0:
        time_left-=1
        label_time['user_health']=f'Осталось {time_left} секунд'
        label_time.after(1000,timer)
    else:
        mbox.showinfo('Время вышло','Игра окончена')
        text.delete(0, 'end')
        if score > folse:
            mbox.showinfo('Хороший результат', 'Молодец!')
        else:
            mbox.showinfo('Неважный результат', 'Постарайся в следуйщий раз')
def check(event):
    global folse
    global score
    if time_left>0:
        user_color=text.get()
        word_color=color_label['fg']
        if user_color==word_color:
            print('да')
            score+=1
            label_score['user_health']=f'правельных ответов: {score}'
        else:
            print('нет')
            folse+=1
            label_false['user_health']=f'Ошибок: {folse}'
            print(text)
        text.delete(0,'end')
        new_word()
window.geometry('350x250')
window.title('цвет')
instruction=tk.Label(window,text='введи цвет слова, а не слово! Жми Enter, чтобы играть ',font=('Helvetica', 10))
instruction.place(x=10,y=10)
label_score=tk.Label(window,text=f'правельных ответов: {score}')
label_score.place(x=10,y=200)
label_time=tk.Label(window,text=f'Осталось {time_left} секунд')
label_time.place(x=10,y=50)
label_false=tk.Label(window,text=f'Ошибок{folse}')
label_false.place(x=160,y=200)
color_label=tk.Label(window,text='color', font=('Helvetica', 60))
color_label.place(x=10,y=80)
text=tk.Entry(window,font=('Helvetica', 10))
text.place(x=10,y=180)
text.focus_set()
new_word()
window.bind('<Return>',check)
timer()
window.mainloop()
#В функции timer: после блока условия if time_left > 0 добавить блок else, в котором выводить всплывающее окно из библиотеки tkinter.messagebox - "Конец игры", "Время вышло".
#В функции check: после блока условия if time_left > 0 добавить блок else, в котором делаем проверку - если правильных ответов больше неправильных - сделать всплывающее окно - "Хороший результат", "Ты молодец". Иначе -
# "Неважный результат", "В следующий раз получится лучше".
