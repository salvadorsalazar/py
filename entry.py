
from tkinter import *

root = Tk()
e = Entry(root,width=50, bg="white",fg="black")
e.pack()

def myClick():
    myLabel = Label(root,text="button clicked")
    myLabel.pack()


myButton = Button(root,text="click me",command=myClick,bg="blue")
# myButton = Button(root,text="click me", padx=50 ,pady=50)

myButton.pack()



root.mainloop()
