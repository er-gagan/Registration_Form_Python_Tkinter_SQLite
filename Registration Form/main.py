from tkinter import *
from SQLiteDB import *
from tkinter.messagebox import *

root = Tk()
root.geometry("1100x500")
root.resizable(0,0)

photo = PhotoImage(file = "./logo.png")
root.iconphoto(False,photo)

root.title("Registration Form")

fname = StringVar()
phone1 = StringVar()
gender = StringVar()
age = StringVar()
pin = StringVar()
current_address = StringVar()
check_address = StringVar()
permanent_address = StringVar()
city = StringVar()
state = StringVar()
area_of_intrest1 = StringVar()
area_of_intrest2 = StringVar()
area_of_intrest3 = StringVar()
area_of_intrest4 = StringVar()

gender.set(1)

def Submit():    
    Fname = fname.get()
    Phone1 = phone1.get()
    Gender = gender.get()
    Age = age.get()
    Pin = pin.get()
    Current_address = current_address.get()
    Permanent_address = permanent_address.get()
    City = city.get()
    State = state.get()
    
    Area_Of_Intrest = ""
    aoi1=area_of_intrest1.get()
    aoi2=area_of_intrest2.get()
    aoi3=area_of_intrest3.get()
    aoi4=area_of_intrest4.get()
    if aoi1!="":
        Area_Of_Intrest += aoi1
    if aoi2!="":
        Area_Of_Intrest +=" " + aoi2
    if aoi3!="":
        Area_Of_Intrest +=" " + aoi3
    if aoi4!="":
        Area_Of_Intrest +=" " + aoi4
    if Area_Of_Intrest[0:1:] == " ":
        Area_Of_Intrest = Area_Of_Intrest[1::]
    
    Suggession = textarea.get('0.0',END)
    
    Suggession_length = len(Suggession)
    if Fname[0:1:] == " " or Fname[0::] == "":
        showerror("Entry is Empty","Please Fill First Name Entry Box")
    elif Phone1[0:1:] == " " or Phone1[0::] == "":
        showerror("Entry is Empty","Please Fill Phone Entry Box")
        e4.focus()
    elif Pin[0:1:] == " " or Pin[0::] == "":
        showerror("Entry is Empty","Please Fill Zip/Pin Entry Box")
        e6.focus()
    elif Current_address[0:1:] == " " or Current_address[0::] == "":
        showerror("Entry is Empty","Please Fill Current Address Entry Box")
        e2.focus()
    elif Permanent_address[0:1:] == " " or Permanent_address[0::] == "":
        showerror("Entry is Empty","Please Fill Permanent Address Entry Box")
        e3.focus()
    elif City[0:1:] == " " or City[0::] == "":
        showerror("Entry is Empty","Please Fill City Name Entry Box")
        e9.focus()
    elif Area_Of_Intrest[0:1:] == " " or Area_Of_Intrest[0::] == "":
        showerror("Checkbox is Empty","Please Fill At Least One Checkbox")
    elif Suggession_length < 5 or Suggession[0:1:] == " " or Suggession[-2:-1:] == " ":
        showerror("Suggession Box is Empty","Please Fill Atleast 6 Chatacter In Suggession Box")
        textarea.focus()
    elif State == "Please Select State":
        showerror("State Error","Please Select State")
    else:
        SendDB(Fname,Phone1,Gender,Age,Pin,Current_address,Permanent_address,City,State,Area_Of_Intrest,Suggession)
        showinfo("Record Stored","Student Record Has Successfully Stored")
    
def ChkAdrs():
    check_value = check_address.get()
    if check_value == "Yes":
        permanent_address.set(current_address.get())
        e2.config(state="readonly")
        e3.config(state="readonly")
    else:
        permanent_address.set("")
        e2.config(state="normal")
        e3.config(state="normal")
        
def Clear():
    fname.set("")
    phone1.set("")
    pin.set("")
    current_address.set("")
    permanent_address.set("")
    city.set("")
    age.set("5")
    r1.select()
    chk.deselect()
    c1.deselect()
    c5.deselect()
    c7.deselect()
    c8.deselect()
    e1.focus()
    e2.config(state="normal")
    e3.config(state="normal")
    state.set("Please Select State")
    textarea.delete('0.0',END)
    
def Show_Record():
    Toproot = Toplevel()
    Toproot.geometry('1008x415')
    Toproot.resizable(0,0)
    photo = PhotoImage(file = "./logo.png")
    Toproot.iconphoto(False,photo)
    try:
        tt1 = Text(Toproot,font=("ArialBlack",15),width=89,height=17,bd=10,padx=4)
        tt1.place(x=0,y=0)
        record_data = Show_Data()
        data_length = len(record_data)
        for i in range(0,data_length):
            tt1.insert(END,record_data[i])
        tt1.config(state='disabled')
    except sqlite3.OperationalError:
        Toproot.destroy()
        showerror("Database Error","Database not exist")

Label(root,text="Student Registration Form",font=("CalibriBlack",25)).place(x=360,y=10)

Label(root,text="Name:",font=("CalibriBlack",15)).place(x=20,y=70)
e1 = Entry(root,textvariable=fname,font=("CalibriBlack",15),bd=2,width=40)
e1.focus()
e1.place(x=130,y=72)

Label(root,text="Phone:",font=("CalibriBlack",15)).place(x=620,y=70)
e4 = Entry(root,bd=2,textvariable=phone1,font=("CalibriBlack",15),width=30)
e4.place(x=700,y=70)

Label(root,text="Gender:",font=("CalibriBlack",15)).place(x=20,y=110)
r1 = Radiobutton(root,text="Male",variable=gender,value="Male",font=("CalibriBlack",15))
r1.select()
r1.place(x=120,y=110)
Radiobutton(root,text="Female",variable=gender,value="Female",font=("CalibriBlack",15)).place(x=210,y=110)
Radiobutton(root,text="Other",variable=gender,value="Others",font=("CalibriBlack",15)).place(x=320,y=110)

Label(root,text="Age:",font=("CalibriBlack",15)).place(x=450,y=110)
e10 = Spinbox(root,font=("CalibriBlack",15),from_=5, to=100,state="readonly",width=10,textvariable=age)
e10.place(x=520,y=112)

Label(root,text="ZIP/PIN:",font=("CalibriBlack",15)).place(x=720,y=110)
e6 = Entry(root,bd=2,textvariable=pin,font=("CalibriBlack",15))
e6.place(x=820,y=112)

Label(root,text="Current Address:",font=("CalibriBlack",15)).place(x=20,y=150)
e2 = Entry(root,bd=2,textvariable=current_address,font=("CalibriBlack",15),width=75)
e2.place(x=230,y=150)

chk = Checkbutton(root,text="If your current address is same as permanent address then check it else not",variable=check_address,onvalue="Yes",offvalue="No",command=ChkAdrs,font=("CalibriBlack",14))
chk.deselect()
chk.place(x=20,y=185)

Label(root,text="Permanent Address:",font=("CalibriBlack",15)).place(x=20,y=230)
e3 = Entry(root,bd=2,textvariable=permanent_address,font=("CalibriBlack",15),width=75)
e3.place(x=230,y=230)

Label(root,text="City:",font=("CalibriBlack",15)).place(x=20,y=270)
e9 = Entry(root,bd=2,textvariable=city,font=("CalibriBlack",15),width=30)
e9.place(x=130,y=270)

Label(root,text="State:",font=("CalibriBlack",15)).place(x=500,y=270)
state_list=["Uttar Pradesh","Uttrakhand","Maharastra","Jammu & Kashmir"]
state.set("Please Select State")
o1=OptionMenu(root,state,*state_list)
o1.config(font=("CalibriBlack",15),width=30)
o1['menu'].configure(font=("CalibriBlack",15))
o1.place(x=600,y=268)


Label(root,text="Area of Intrest:",font=("CalibriBlack",15)).place(x=20,y=310)
c1 = Checkbutton(root,variable=area_of_intrest1,onvalue="Programming",offvalue="",text="Programming",font=("CalibriBlack",15))
c1.deselect()
c1.place(x=200,y=310)
c5 = Checkbutton(root,variable=area_of_intrest2,onvalue="Studying",offvalue="",text="Studying",font=("CalibriBlack",15))
c5.deselect()
c5.place(x=400,y=310)
c7 = Checkbutton(root,variable=area_of_intrest3,onvalue="Dancing",offvalue="",text="Dancing",font=("CalibriBlack",15))
c7.deselect()
c7.place(x=600,y=310)
c8 = Checkbutton(root,variable=area_of_intrest4,onvalue="Travelling",offvalue="",text="Travelling",font=("CalibriBlack",15))
c8.deselect()
c8.place(x=800,y=310)

Label(root,text="Any Suggession:",font=("CalibriBlack",13)).place(x=20,y=350)
textarea = Text(root,font=("CalibriBlack",15),bd=5,height=3)
textarea.place(x=20,y=380)

Button(root,text="Submit",font=("CalibriBlack",20),bd=8,command=Submit).place(x=940,y=360)
Button(root,text="Clear",font=("CalibriBlack",13),bd=5,command=Clear).place(x=915,y=440)
Button(root,text="Show Record",font=("CalibriBlack",12),bd=5,command=Show_Record).place(x=980,y=440)

def on_closing():
    if askokcancel("Quit", "Do you want to quit?"):
        DbClose()
        root.destroy()
        
root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()