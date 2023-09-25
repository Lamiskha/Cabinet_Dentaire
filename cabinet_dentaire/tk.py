from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import webbrowser
import os
import sys
from datetime import datetime
from datetime import date
pro = Tk()
pro.geometry('800x500+230+80')
pro.title('Cabinet Dantaire')
pro.iconbitmap('icone.ico')
title = Label(pro, text='CABINET EL ANOUAR ', fg='#9DD4C4' , bg='#707878' , font=('Arial',16,'bold',))
title.pack(fill=X)
F1 = Frame(pro, width=260, height=500 , bg='#9DD4C4')
icon = PhotoImage(file="phone.png")
B1 = Button(F1, text="Patients", bg="#707878", fg="white", font=("Arial", 12, "bold"), width=20)
B1.place(x=25 ,y=180 )
B2 = Button(F1, text="Consultation", bg="#707878", fg="white", font=("Arial", 12, "bold"), width=20)
B2.place(x=25 ,y=230 )
B3 = Button(F1, text="Payement", bg="#707878", fg="white", font=("Arial", 12, "bold"), width=20)
B3.place(x=25 ,y=280 )
B4 = Button(F1, text="Stockage Materielle", bg="#707878", fg="white", font=("Arial", 12, "bold"), width=20)
B4.place(x=25 ,y=330 )
F1.place(x=540 , y=30)
def update_time():
    current_time = datetime.now().strftime('%H:%M:%S')
    time_label.config(text=current_time)
    pro.after(1000, update_time)
time_label = Label(pro, font=("Arial", 13))
time_label.place(x='15' , y='33')

update_time()

def update_date():
    current_date = date.today().strftime('%d/%m/%Y')
    date_label.config(text=current_date)
    pro.after(86400000, update_date) 

date_label = Label(pro, font=("Arial", 13))
date_label.place(x='430' , y='33')
update_date()
photo = PhotoImage(file='C.png')
imo = Label(F1,image=photo)
imo.place(x='0' , y='0' )
photo1 = PhotoImage(file='dent.png')
imo1 = Label(pro,image=photo1)
imo1.place(x='20' , y='70' )
F2 = Frame(pro, width=498, height=100 , bg='#9DD4C4')
F2.place(x='20' , y='380')
B1 = Button(F2, text="Rendez-Vous", bg="#707878", fg="white", font=("Arial", 12, "bold"), width=40, height=1)
B1.place(x=43 ,y=30 )
pro.resizable(False,False)
pro.mainloop()
