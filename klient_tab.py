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

def tooteaken():
    toplevel = Toplevel()
    toplevel.title('Lisa toode')
    toplevel.geometry("%dx%d+%d+%d" % (250, 200, 100, 50))
    
    L1 = Label(toplevel, text="Toote nimi")
    L1.pack()
    E1 = Entry(toplevel, bd =2)
    E1.pack()

    L1 = Label(toplevel, text="Toote number")
    L1.pack()
    E2 = Entry(toplevel, bd =2)
    E2.pack()

    L1 = Label(toplevel, text="Toote hind")
    L1.pack()
    E3 = Entry(toplevel, bd =2)
    E3.pack()
    button = Button(toplevel, text="Lisa toode", command=lambda: dr.sisestatoode(E1.get(), E2.get(), E3.get()))
    button.pack()

    toplevel.focus_set()    
 
     

    
def hetkeseis():
    toplevel = Toplevel()
    toplevel.title('Hetkel arvel')
    toplevel.geometry("%dx%d+%d+%d" % (250, 300, 100, 50))
    
    a = Listbox(toplevel, height = 18, width = 63)
    a.grid(column =0, row = 5, columnspan=3, padx = 3)
    
    f = open('arve.txt')
    sisu = f.readlines()
    f.close()
    
    sisu = sisu[1::2]
    for i in sisu:
        a.insert('end', i)
    

    toplevel.focus_set()    
     