from tkinter import *

root = Tk()

data = StringVar()

def Submit():
    Data = data.get()
    if Data[0:1:] == " " or Data[0::] == "":
        print("Empty")
    else:
        print("Not Empty")
Entry(root,textvariable=data).place(x=10,y=10)

Button(root,text="Submit",command=Submit).place(x=20,y=50)

root.mainloop()