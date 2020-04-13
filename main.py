from tkinter import *
from tasks import *
createTask("test","4-1-2020")

window = Tk()
window.title("Welcome to Repl.it")
window.geometry('350x200')

lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)

txt = Entry(window,width=10)
txt.grid(column=1, row=0)

def clicked():
    lbl.configure(text="Button was clicked !!")

btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=2, row=0)



print("hello world")


window.mainloop()