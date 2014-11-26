import dataret as dr
import datainp as di
import klient_tab as kt

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

klient = tk.StringVar(f1)
klient.set(kliendid[0]) # default value

w = tk.OptionMenu(f1, klient, *kliendid)
w.pack(padx=3, pady=5)



###### toode 1

toode1 = tk.StringVar(f1)
toode1.set(tooted[0]) # default value

w2 = tk.OptionMenu(f1, toode1, *tooted)
w2.pack(padx=3, pady=5)


######### toode 1 kogus

L1 = tk.Label(f1, text="Kogus")
L1.pack()
E1 = tk.Entry(f1, bd =5)
E1.pack()

######### toode 2

toode2 = tk.StringVar(f1)
toode2.set(tooted[0]) # default value

w3 = tk.OptionMenu(f1, toode2, *tooted)
w3.pack(padx=3, pady=5)

######### toode 1 kogus

L2 = tk.Label(f1, text="Kogus")
L2.pack()
E2 = tk.Entry(f1, bd =5)
E2.pack()


##### loo arve nupp
def ok():
    print("value is", klient.get())

button = tk.Button(f1, text="Loo arve", command=ok)
button.pack()


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
