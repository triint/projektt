from tkinter import *
import dataret as dr

def kliendiaken():
    toplevel = Toplevel()
    toplevel.title('Lisa klient')
    toplevel.geometry("%dx%d+%d+%d" % (250, 200, 100, 50))
    
    L1 = Label(toplevel, text="Kliendi nimi")
    L1.pack()
    E1 = Entry(toplevel, bd =2)
    E1.pack()

    L1 = Label(toplevel, text="Kliendi number")
    L1.pack()
    E2 = Entry(toplevel, bd =2)
    E2.pack()

    L1 = Label(toplevel, text="Kliendi email")
    L1.pack()
    E3 = Entry(toplevel, bd =2)
    E3.pack()
    button = Button(toplevel, text="Lisa klient", command=lambda: dr.sisestaklient(E1.get(), E2.get(), E3.get()))
    button.pack()

    toplevel.focus_set()
    
