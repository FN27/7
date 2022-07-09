import tkinter
import tkinter as tk
import random
secret_number=random.randint(1,100)
attempts=10
def reset():
    global secret_number
    global attempts
    attempts=10
    label_user_attemppts['user_health']=attempts
    game_plan['user_health']='Угадай число от 1 до 100'
    text_entry.delete()
    gues_button.configure(state=tk.NORMAL)
    return_button.configure(state=tk.DISABLED)
def gues(event):
    global attempts
    number=text_entry.get()
    text_entry.delete(0,'end')
    if number=='':
        game_plan['user_health']='Введи число от одного до ста'
    else:
        if attempts >0:
            attempts-=1
            label_user_attemppts['user_health']=f'{attempts} - кол-во попыток'
            number=int(number)
            if number==secret_number:
                game_plan['user_health']='Ты угадал'
                gues_button.configure(state=tk.DISABLED)
                return_button.configure(state=tk.NORMAL)
            else:
                if number>secret_number:
                    game_plan['user_health']='число меньше'
                else:
                    game_plan['user_health']='число больше'
window=tk.Tk()
window.geometry('350x350')
window.title('Угадай число')
game_plan=tk.Label(window,text='Угадай число от 1 до 100')
game_plan.place(x=10,y=20)
label_user_attemppts=tk.Label(window,text=f'{attempts} - кол-во попыток')
label_user_attemppts.place(x=10,y=160)
text_entry=tk.Entry(window)
text_entry.focus_set()
text_entry.place(x=10,y=70)
gues_button=tk.Button(window,width=17,text='Проверить',command=lambda e='<Return>':gues(e))
gues_button.place(x=10,y=90)
return_button=tk.Button(window,text='Играть снова',state=tk.DISABLED,width=17)
return_button.place(x=10,y=120)
window.bind('<Return>',gues)
window.mainloop()
#В функции guess: после блока условия if attempts > 0 добавить блок else, в котором делаем надпись label - "Можешь сыграть снова.", и меняем состояния кнопок - guess_button делаем неактивной, reset_button - активной.
