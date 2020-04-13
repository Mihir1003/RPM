from tkinter import *
from tasks import *
import json

f=open("tasks.json","w")
f.write("")
f.close()
window = Tk()
window.title("Welcome to Repl.it")
window.geometry('350x200')

lbl = Label(window, text="Empty")
lbl.grid(column=0, row=1)

txt = Entry(window,width=10)
txt.grid(column=1, row=0)

def clicked():
    createTask(txt.get())
    f = open("tasks.json", "r")
    if f.read():
        f.seek(0)
        tasks = [value["title"] for value in list(json.loads(f.read()).values())]
    else:
        tasks = ""
    f.close()
    lbl.configure(text=tasks)

btn = Button(window, text="add", command=clicked)
btn.grid(column=2, row=0)



print("hello world")


window.mainloop()