from tkinter import *
root = Tk()
root.geometry("1100x700")
root.resizable(0,0)

photo = PhotoImage(file = "./logo.png")
root.iconphoto(False,photo)

root.title("Registration Form")

Label(root,text="Student Registration Form",font=("CalibriBlack",25)).place(x=360,y=0)

Label(root,text="First Name:",font=("CalibriBlack",15)).place(x=20,y=70)
Entry(root,font=("CalibriBlack",15)).place(x=130,y=72)

Label(root,text="Middle Name:",font=("CalibriBlack",15)).place(x=370,y=70)
Entry(root,font=("CalibriBlack",15)).place(x=500,y=72)

Label(root,text="Last Name:",font=("CalibriBlack",15)).place(x=740,y=70)
Entry(root,font=("CalibriBlack",15)).place(x=850,y=72)

Label(root,text="Phone1:",font=("CalibriBlack",15)).place(x=20,y=110)
Entry(root,font=("CalibriBlack",15)).place(x=130,y=112)

Label(root,text="Phone2:",font=("CalibriBlack",15)).place(x=370,y=110)
Entry(root,font=("CalibriBlack",15)).place(x=500,y=112)

Label(root,text="ZIP/PIN:",font=("CalibriBlack",15)).place(x=740,y=110)
Entry(root,font=("CalibriBlack",15)).place(x=850,y=112)

Label(root,text="Address:",font=("CalibriBlack",15)).place(x=20,y=150)
Label(root,text="Permanent Address:",font=("CalibriBlack",15)).place(x=20,y=190)
Label(root,text="Name:",font=("CalibriBlack",15)).place(x=20,y=230)
Label(root,text="Name:",font=("CalibriBlack",15)).place(x=20,y=270)

# image1= PhotoImage(file="./back.png")
# label_for_image= Label(root, image=image1)
# label_for_image.place(x=-2, y=-1)


root.mainloop()