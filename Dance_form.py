from tkinter import *
#  ---- function to set users details in another txt  file ------
def values():
    f= open('user_details.txt', 'a')
    f.write(f"\n name = {name__.get()}")
    f.write(f"\n phone number = {str(phone__.get())}")
    f.write(f"\n email id = {email__.get()}" )
    f.write(f"\n Gender = {gender__.get()}")
    f.write(f"\n Age = {age__.get()}" )
    f.write(f"\n Address = {Address__.get()}" )
    f.write(f"\n Dance type = {Dance_type__.get()}")
    f.write("\n-----Next user details------")
    # print(name__.get())
    # print(phone__.get())
    # print(email__.get())
    # print(gender__.get())
    # print(age__.get())
    # print(Address__.get())
    # print(Dance_type__.get())


root = Tk()
root.geometry("900x600")
root.title("Dance Form")

photo =PhotoImage(file="Screenshot (17).png")

hading = Label(root , text="Fill this dance form" , font=('' , 20 , 'bold'), fg='blue')
hading.place(x=0 , y=0 , relwidth=1 )
box = Frame(root , border=5  )
box.place(x=180 , y=60,height=700 ,width=500)
back_immage = Label(box ,image=photo)
back_immage.pack()
# --------input variable------------
name__= StringVar()
phone__ = IntVar()
email__= StringVar()
gender__ = StringVar()
gender__.set("female")
age__= StringVar()
Address__= StringVar()
Dance_type__= StringVar()

# -----------label names------------
name = Label(box , text="Name" ,font=("" , 15 , 'bold'  ) , bg='white').place(x=50,y=10)
phone = Label(box , text="Number" ,font=("" , 15 , 'bold' ), bg='white').place(x=50,y=60)
email_id = Label(box , text="Email ID" ,font=("" , 15 , 'bold' ), bg='white').place(x=50,y=120)

gender = Label(box , text="Gender" ,font=("" , 15 , 'bold' ), bg='white').place(x=50,y=180)
age = Label(box , text="Age" ,font=("" , 15 , 'bold' ), bg='white').place(x=50,y=240)
Address = Label(box , text="Address" ,font=("" , 15 , 'bold' ), bg='white').place(x=50,y=280)
Dance_type = Label(box , text="Dance type" ,font=("" , 15 , 'bold' ), bg='white').place(x=50,y=330)

# -----Entery box details -------------
name_ = Entry(box  ,font=("" , 15 , 'bold'  ) ,textvariable=name__, border =4 , bg='white').place(x=180,y=10)
phone_ = Entry(box  ,font=("" , 15 , 'bold'  ) ,textvariable=phone__, border =4 , bg='white').place(x=180,y=60)
email_ = Entry(box  ,font=("" , 15 , 'bold'  ) ,textvariable=email__, border =4 , bg='white').place(x=180,y=120)

# -----Radio buttons--------
radio = Radiobutton(box , text="Male" ,variable=gender__, value="Male",font=("" ,15,'bold' ),bg='white').place(x=180,y=180)
radio = Radiobutton(box , text="Female" , variable=gender__, value="Female",font=("" ,15,'bold' ),bg='white').place(x=250,y=180)

# gender_ = Entry(box  ,font=("" , 15 , 'bold'  ) ,textvariable=gender__, border =4 , bg='white').place(x=180,y=180)
age_ = Entry(box  ,font=("" , 15 , 'bold'  ) ,textvariable=age__, border =4 , bg='white').place(x=180,y=240)
address_ = Entry(box  ,font=("" , 15 , 'bold'  ) ,textvariable=Address__, border =4 , bg='white').place(x=180,y=280)
dance_type_ = Entry(box  ,font=("" , 15 , 'bold'  ) ,textvariable=Dance_type__, border =4 , bg='white').place(x=180,y=330)
# ---------submit buttom ---------
submit = Button(box , text="submit" ,font=("" , 20 , 'bold') ,command=values,bg='#7b1616',fg='#2d8619',border=4).place(x=150,y=380)

root.mainloop()