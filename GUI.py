import dataret as dr
import datainp as di
import klient_tab as kt
from pdfgen import *

import tkinter as tk
import tkinter.ttk as ttk


root = tk.Tk()
# use width x height + x_offset + y_offset (no spaces!)
root.geometry("%dx%d+%d+%d" % (450, 450, 100, 50))
root.title('MinuLadu ver 0.1')

nb = ttk.Notebook(root)
nb.pack(fill='both', padx = 7, pady = 7, expand='yes')

# create a child frame for each page
f1 = tk.Frame()
f2 = tk.Frame()
f3 = tk.Frame()
f4 = tk.Frame()

# create the pages
nb.add(f1, text='Arved')
nb.add(f2, text='Ladu')
nb.add(f3, text='Kliendid')
nb.add(f4, text='Seaded')

# put a button widget on child frame f1 on page1
#btn1 = tk.Button(f1, text='Lisa uus')
#btn1.pack(side='left', anchor='nw', padx=3, pady=5)
#########

####################
# Arve lisamine    #
####################

##### listid

kliendid = dr.outkliendid()
tooted = dr.outtooted()

#### kliendi valimine
label1 = tk.Label(f1, text="Kliendi nimi:")
label1.grid(column = 0, row = 4, padx=3, pady=5)

klient = tk.StringVar(f1)
klient.set(kliendid[0]) # default value

w = tk.OptionMenu(f1, klient, *kliendid)
w.grid(column = 1, row = 4, padx=3, pady=5, )



###### toode 1
label2 = tk.Label(f1, text="Toode")
label2.grid(column = 1, row = 5, padx=10, pady=10)

toode1 = tk.StringVar(f1)
toode1.set(tooted[0]) # default value

w2 = tk.OptionMenu(f1, toode1, *tooted)
w2.grid(column =1, row = 6, padx=10, pady=10)


######### toode 1 kogus

L1 = tk.Label(f1, text="Kogus")
L1.grid(column =2, row = 5, padx=10, pady=10)
E1 = tk.Entry(f1, bd =5)
E1.grid(column =2, row = 6, padx=10, pady=10)

########### toode 2

label3 = tk.Label(f1, text="Toode")
label3.grid(column = 1, row = 7, padx=10, pady=10)

toode2 = tk.StringVar(f1)
toode2.set(tooted[0]) # default value

w3 = tk.OptionMenu(f1, toode2, *tooted)
w3.grid(column =1, row = 8, padx=10, pady=10)


######### toode 2 kogus

L2 = tk.Label(f1, text="Kogus")
L2.grid(column =2, row = 7, padx=10, pady=10)
E2 = tk.Entry(f1, bd =5)
E2.grid(column =2, row = 8, padx=10, pady=10)

##### loo arve nupp
def ok():
    print("value is", klient.get())

button = tk.Button(f1, text="Loo arve", command=lambda: loopdf("2", klient.get(), toode1.get(), toode2.get()))
button.grid(column =4, row = 10, padx=10, pady=10)


######################
# klientide TAB      #
######################
button = tk.Button(f3, text="LISA KLIENT", command=lambda: kt.kliendiaken())
button.pack()

L1 = tk.Label(f3, text="Meie kliendid:")
L1.pack()

l = tk.Listbox(f3, height=5)
l.pack()
s = ttk.Scrollbar(f3, command=l.yview)
s.pack()
l['yscrollcommand'] = s.set
ttk.Sizegrip().pack()
for i in kliendid:
    l.insert('end', i)



######################
#    SEADED          #
######################

button = tk.Button(f4, text="Loo andmebaas", command=lambda: dr.firststart())
button.pack()
button = tk.Button(f4, text="DEMO", command=lambda: dr.demo())
button.pack()



root.mainloop()
