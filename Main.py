from tkinter import *
import time 

root = Tk()
root.title("Timer")
root.geometry("400x600")
root.config(bg="#000")
root.resizable(False,False)

heading = Label(root,text="Timer",font="arial 30 bold",bg="#000",fg="#ea3548")
heading.pack(pady=10)
 
#clock
Label(root,font=("arial",15,"bold"),text="current time:",bg='#000').place(x=65,y=70)
def timer():
    global times
    times=int(hours.get())*3600+int(minutes.get())*60+int(seconds.get())
    while times> -1:
        
        min,sec=(times//60,times%60)
        hrs = 0
        if min>60:
            hrs,min=(min//60,min%60)
       
        seconds.set(sec)
        minutes.set(min)
        hours.set(hrs)

        root.update()
        time.sleep(1)

        if times==0:

            seconds.set("00")
            hours.set("00")
            minutes.set("00")
           
        times -= 1

def brush():
    hours.set("00")
    minutes.set("02")
    seconds.set("00")

def face():
    hours.set("00")
    minutes.set("15")
    seconds.set("00")

def eggs():
    hours.set("00")
    minutes.set("10")
    seconds.set("00")

def clock():
    clock_time = time.strftime("%H:%M:%S %p")
    current_time.config(text=clock_time)
    current_time.after(1000,clock)


current_time=Label(root,font="arial 15 bold",text="",fg="#000",bg="#fff")
current_time.place(x=190,y=70)
clock()

#timer
hours = StringVar()
Entry(root,textvariable=hours,width=2,font="arial 50",bg="#000",fg="#fff",bd=0).place(x=30,y=155)
hours.set("00")

minutes = StringVar()
Entry(root,textvariable=minutes,width=2,font="arial 50",bg="#000",fg="#fff",bd=0).place(x=150,y=155)
minutes.set("00")

seconds = StringVar()
Entry(root,textvariable=seconds,width=2,font="arial 50",bg="#000",fg="#fff",bd=0).place(x=270,y=155)
seconds.set("00")

Label(root,text="Hours",font="arial 12",bg="#000",fg="#fff").place(x=45,y=225)
Label(root,text="Minutes",font="arial 12",bg="#000",fg="#fff").place(x=160,y=225)
Label(root,text="Seconds",font="arial 12",bg="#000",fg="#fff").place(x=275,y=225)

button = Button(root,text="Start", fg="#ea3548",bg="#fff",bd=0,width=20,height=2,font="arial 10 bold",command=timer)

image1 = PhotoImage(file="brush.png")
button1 = Button(root,image=image1,bg="#000",bd=0,command=brush)
button1.place(x=7,y=300)

image2 = PhotoImage(file="face.png")
button2 = Button(root,image=image2,bg="#000",bd=0,command=face)
button2.place(x=137,y=300)

image3 = PhotoImage(file="eggs.png")
button3 = Button(root,image=image3,bg="#000",bd=0,command=eggs)
button3.place(x=267,y=300)


button.pack(padx=5,pady=40,side=BOTTOM)

root.mainloop()
