import tkinter.filedialog as tkf
import tkinter as tk
import tkinter.messagebox as tkm
window=tk.Tk()
file_name=""
file_label=tk.Label(window,text=f'{file_name}')
file_label.place(relx=0,rely=1,anchor='sw')
def open_file():
    global file_name
    text1.delete(1.0,'end')
    file_name=tkf.askopenfilename()
    file_label ['user_health']=file_name
    with open (file_name) as file:
        text1.insert(1.0,file.read())
def save_as_file():
    global file_name
    file_name=tkf.asksaveasfilename()
    file_label['user_health'] = file_name
    content=text1.get(1.0,'end')
    with open (file_name,'w') as file:
        file.write(content)
def save_file():
    global file_name
    if file_name== "":
        save_as_file()
    else:
        content= text1.get(1.0,'end')
        with open(file_name,"w") as file:
            file.write(content)
        tkm.showinfo(title='Сохрание файла', message="Сохранения записаны в файл ")
def new_file():
    global file_name
    if tkm.askokcancel(title='созд ание нового файла', message='Вы уверенны? Весь не сохранённый текст будет удалён'):
        file_name=''
        file_label['user_health'] = file_name
        text1.delete(1.0,'end')

window.title("блокнот")
window.geometry('400x400')
#user_health=tk.Label(window,user_health='Мой дневник',bg= "gray",fg= 'white')
#user_health.place(x=10,y=3)
text1=tk.Text(window,bg= "gray",fg= 'orange',wrap="word")
#text1.place(x=0,y=0,relwidth=1,relheight=1)
text1.place(x=0,y=0,relwidth=1,relheight=1)
main_menu=tk.Menu(window)
window.configure(menu=main_menu)#крепим к верхней части окна главное меню
file_menu=tk.Menu(main_menu,tearoff=0)
main_menu.add_cascade(label='File',menu=file_menu)
new_file_icone=tk.PhotoImage(file='new_file.gif')
new_file_icone2=tk.PhotoImage(file='open_file.gif')
new_file_icone3=tk.PhotoImage(file='save_file.gif')
file_menu.add_command(label='новый',image=new_file_icone,compound='left',command= new_file)
file_menu.add_command(label='открыть',image=new_file_icone2,compound='left',command= open_file)
file_menu.add_command(label='сохранить',image=new_file_icone3,compound='left',command= save_file)
file_menu.add_command(label='сохранить как',image=new_file_icone3,compound='left',command= save_as_file)


window.mainloop()
#В функции save_file после перезаписи файла выводить информационное окно с помощью команды tkm.showinfo. В заголовке выводим "Сохранение файла", в основной
# части окна -  и указать в какой .

