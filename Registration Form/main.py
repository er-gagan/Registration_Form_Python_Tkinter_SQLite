from tkinter import *
from SQLiteDB import *
from tkinter.messagebox import *

root = Tk()
root.geometry("1100x650")
root.resizable(0,0)

photo = PhotoImage(file = "./logo.png")
root.iconphoto(False,photo)

root.title("Registration Form")

fname = StringVar()
mname = StringVar()
lname = StringVar()
phone1 = StringVar()
phone2 = StringVar()
pin = StringVar()
current_address = StringVar()
check_address = StringVar()
permanent_address = StringVar()
city = StringVar()
state = StringVar()
gender = StringVar()
area_of_intrest1 = StringVar()
area_of_intrest2 = StringVar()
area_of_intrest3 = StringVar()
area_of_intrest4 = StringVar()
area_of_intrest5 = StringVar()
area_of_intrest6 = StringVar()
area_of_intrest7 = StringVar()
area_of_intrest8 = StringVar()
age = StringVar()
email = StringVar()

gender.set(1)

def Submit():
    Area_Of_Intrest = ""
    aoi1=area_of_intrest1.get()
    aoi2=area_of_intrest2.get()
    aoi3=area_of_intrest3.get()
    aoi4=area_of_intrest4.get()
    aoi5=area_of_intrest5.get()
    aoi6=area_of_intrest6.get()
    aoi7=area_of_intrest7.get()
    aoi8=area_of_intrest8.get()
    if aoi1!="":
        Area_Of_Intrest += aoi1
    if aoi2!="":
        Area_Of_Intrest +=" " + aoi2
    if aoi3!="":
        Area_Of_Intrest +=" " + aoi3
    if aoi4!="":
        Area_Of_Intrest +=" " + aoi4
    if aoi5!="":
        Area_Of_Intrest +=" " + aoi5
    if aoi6!="":
        Area_Of_Intrest +=" " + aoi6
    if aoi7!="":
        Area_Of_Intrest +=" " + aoi7
    if aoi8!="":
        Area_Of_Intrest +=" " + aoi8
    if Area_Of_Intrest[0] == " ":
        Area_Of_Intrest = Area_Of_Intrest[1::]
        
    Fname = fname.get()
    Mname = mname.get()
    Lname = lname.get()
    Phone1 = phone1.get()
    Phone2 = phone2.get()
    Pin = pin.get()
    Current_address = current_address.get()
    Permanent_address = permanent_address.get()
    City = city.get()
    State = state.get()
    Gender = gender.get()
    Age = age.get()
    Email = email.get()
    Suggession = textarea.get('1.0',END)
    SendDB(Fname,Mname,Lname,Phone1,Phone2,Pin,Current_address,Permanent_address,City,State,Gender,Area_Of_Intrest,Age,Email,Suggession)
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
    

Label(root,text="Student Registration Form",font=("CalibriBlack",25)).place(x=360,y=10)

Label(root,text="First Name:",font=("CalibriBlack",15)).place(x=20,y=70)
e1 = Entry(root,textvariable=fname,font=("CalibriBlack",15))
e1.focus()
e1.place(x=130,y=72)

Label(root,text="Middle Name:",font=("CalibriBlack",15)).place(x=370,y=70)
Entry(root,textvariable=mname,font=("CalibriBlack",15)).place(x=500,y=72)

Label(root,text="Last Name:",font=("CalibriBlack",15)).place(x=740,y=70)
Entry(root,textvariable=lname,font=("CalibriBlack",15)).place(x=850,y=72)

Label(root,text="Phone1:",font=("CalibriBlack",15)).place(x=20,y=110)
Entry(root,textvariable=phone1,font=("CalibriBlack",15)).place(x=130,y=112)

Label(root,text="Phone2:",font=("CalibriBlack",15)).place(x=370,y=110)
Entry(root,textvariable=phone2,font=("CalibriBlack",15)).place(x=500,y=112)

Label(root,text="ZIP/PIN:",font=("CalibriBlack",15)).place(x=740,y=110)
Entry(root,textvariable=pin,font=("CalibriBlack",15)).place(x=850,y=112)

Label(root,text="Current Address:",font=("CalibriBlack",15)).place(x=20,y=150)
e2 = Entry(root,textvariable=current_address,font=("CalibriBlack",15),width=75)
e2.place(x=230,y=150)

chk = Checkbutton(root,text="If your current address is same as permanent address then check it else not",variable=check_address,onvalue="Yes",offvalue="No",command=ChkAdrs,font=("CalibriBlack",14))
chk.deselect()
chk.place(x=20,y=185)

Label(root,text="Permanent Address:",font=("CalibriBlack",15)).place(x=20,y=230)
e3 = Entry(root,textvariable=permanent_address,font=("CalibriBlack",15),width=75)
e3.place(x=230,y=230)

Label(root,text="City:",font=("CalibriBlack",15)).place(x=20,y=270)
Entry(root,textvariable=city,font=("CalibriBlack",15),width=30).place(x=130,y=270)

Label(root,text="State:",font=("CalibriBlack",15)).place(x=500,y=270)
state_list=["Uttar Pradesh","Uttrakhand","Maharastra","Jammu & Kashmir"]
state.set(state_list[0])
o1=OptionMenu(root,state,*state_list)
o1.config(font=("CalibriBlack",15),width=30)
o1['menu'].configure(font=("CalibriBlack",15))
o1.place(x=600,y=268)

Label(root,text="Gender:",font=("CalibriBlack",15)).place(x=20,y=310)
Radiobutton(root,text="Male",variable=gender,value="Male",font=("CalibriBlack",15)).place(x=150,y=310)
Radiobutton(root,text="Female",variable=gender,value="Female",font=("CalibriBlack",15)).place(x=250,y=310)
Radiobutton(root,text="Other",variable=gender,value="Others",font=("CalibriBlack",15)).place(x=350,y=310)

Label(root,text="Area of Intrest:",font=("CalibriBlack",15)).place(x=20,y=350)
c1 = Checkbutton(root,variable=area_of_intrest1,onvalue="Programming",offvalue="",text="Programming",font=("CalibriBlack",15))
c1.deselect()
c1.place(x=200,y=350)
c2 = Checkbutton(root,variable=area_of_intrest2,onvalue="Cricket",offvalue="",text="Cricket",font=("CalibriBlack",15))
c2.deselect()
c2.place(x=400,y=350)
c3 = Checkbutton(root,variable=area_of_intrest3,onvalue="Tennnis",offvalue="",text="Tennnis",font=("CalibriBlack",15))
c3.deselect()
c3.place(x=600,y=350)
c4 = Checkbutton(root,variable=area_of_intrest4,onvalue="Carrom",offvalue="",text="Carrom",font=("CalibriBlack",15))
c4.deselect()
c4.place(x=800,y=350)
c5 = Checkbutton(root,variable=area_of_intrest5,onvalue="Studying",offvalue="",text="Studying",font=("CalibriBlack",15))
c5.deselect()
c5.place(x=200,y=390)
c6 = Checkbutton(root,variable=area_of_intrest6,onvalue="Reading",offvalue="",text="Reading",font=("CalibriBlack",15))
c6.deselect()
c6.place(x=400,y=390)
c7 = Checkbutton(root,variable=area_of_intrest7,onvalue="Dancing",offvalue="",text="Dancing",font=("CalibriBlack",15))
c7.deselect()
c7.place(x=600,y=390)
c8 = Checkbutton(root,variable=area_of_intrest8,onvalue="Travelling",offvalue="",text="Travelling",font=("CalibriBlack",15))
c8.deselect()
c8.place(x=800,y=390)

Label(root,text="Age:",font=("CalibriBlack",15)).place(x=20,y=435)
Entry(root,textvariable=age,font=("CalibriBlack",15)).place(x=100,y=435)

Label(root,text="Email:",font=("CalibriBlack",15)).place(x=400,y=435)
Entry(root,textvariable=email,font=("CalibriBlack",15),width=45).place(x=500,y=435)

Label(root,text="Any Suggession:",font=("CalibriBlack",13)).place(x=20,y=475)
textarea = Text(root,font=("CalibriBlack",15),bd=5,height=5)
textarea.place(x=20,y=500)

Button(root,text="Submit",font=("CalibriBlack",20),bd=8,command=Submit).place(x=940,y=500)
Button(root,text="Clear",font=("CalibriBlack",16),bd=5,width=9).place(x=940,y=575)
root.mainloop()