
from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root,text="button clicked")
    myLabel.pack()


myButton = Button(root,text="click me",command=myClick,bg="black")
# myButton = Button(root,text="click me", padx=50 ,pady=50)

myButton.pack()



root.mainloop()
