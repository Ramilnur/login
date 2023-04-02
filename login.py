from tkinter import *

pa = '7788d'
us = 'ramil123'

root = Tk()
root.title("Добро пожаловать в приложение PythonRu")
root.geometry('200x150')
root.resizable(False, False)

root1 = Tk()
root1.title("Добро пожаловать в приложение PythonRu")
root1.geometry('200x150')
root1.resizable(False, False)
root1.withdraw()

root2 = Tk()
root2.title("Добро пожаловать в приложение PythonRu")
root2.geometry('200x150')
root2.resizable(False, False)
root2.withdraw()

def login():
    root.withdraw()
    root1.deiconify()
    user = ent.get()
    parol = ent1.get()
    if user == us and parol == pa:
        root2.deiconify()
    else:
        print('error')

ent = Entry(root1, width=25)
ent.place(x=20, y=20)

ent1 = Entry(root1, width=25)
ent1.place(x=20, y=40)

but = Button(root1, text='Login', width=20, command=login)
but.place(x=20, y=100)

but = Button(root, text='Login', width=20, command=login)
but.place(x=20, y=100)

root.mainloop()
