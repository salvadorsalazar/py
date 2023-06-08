
from tkinter import *

root = Tk()
e = Entry(root,width=50, bg="white",fg="black")
e.pack()
# e,get()

e.insert(0,"enter your name: ")

def myClick():
    hello = "hello "+ e.get()
    myLabel = Label(root,text=hello)
    myLabel.pack()


myButton = Button(root,text="enter your name",command=myClick,bg="blue")
# myButton = Button(root,text="click me", padx=50 ,pady=50)

myButton.pack()



root.mainloop()
