from tkinter import *
root=Tk()
root.geometry('500x500')

val=StringVar()

def sub():
    print(val.get())

c1 = Checkbutton(root,text="One",variable=val,onvalue="One")
c1.deselect()
c1.place(x=20,y=20)

Checkbutton(root,text="Two").place(x=20,y=50)
Checkbutton(root,text="Three").place(x=20,y=80)
Checkbutton(root,text="Four").place(x=20,y=110)

Button(root,text="Submit",command=sub).place(x=20,y=150)

root.mainloop()