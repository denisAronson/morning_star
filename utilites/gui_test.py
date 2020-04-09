#импортируем модуль для создания GUI
from tkinter import *

#создаем окно, задаем его размер и заголовок
window = Tk()
window.geometry('800x500')
window.title("Мое перове GUI на питоне")

#функционал кнопки
def clicked():
    lbl.configure(text='Зачем нажал')

#добавляем текст, задем локацию
lbl = Label(window, text="Hello", font=("Verdana", 30))
lbl.grid(column=0, row=0)

#пользовательский ввод
txt = Entry(window,width=10)  
txt.grid(column=1, row=0) 

#добавляем кнопку (Button виджет), задаем локацию, цвет фона и переднего плана(текст)
btn = Button(window, text="Кнопка", bg='black', fg='silver', command=clicked)
btn.grid(column=2, row=0)

window.mainloop()