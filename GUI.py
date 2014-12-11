import dataret as dr
import datainp as di
import klient_tab as kt
from pdfgen import *
from seaded import * 
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
label2.grid(column = 1, row = 5, padx=10, pady=1)

toode1 = tk.StringVar(f1)
toode1.set(tooted[0]) # default value

w2 = tk.OptionMenu(f1, toode1, *tooted)
w2.grid(column =1, row = 6, padx=10, pady=1)


######### toode 1 kogus

L1 = tk.Label(f1, text="Kogus")
L1.grid(column =2, row = 5, padx=10, pady=1)
E1 = tk.Entry(f1, bd =5)
E1.grid(column =2, row = 6, padx=10, pady=1)

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

button = tk.Button(f1, text="Loo arve", command=lambda: loopdf("2", klient.get(), toode1.get(), toode2.get()))
button.grid(column =4, row = 10, padx=10, pady=10)

######################
#    SEADED          #
######################

label4 = tk.Label(f2, text="Tooted laos:")
label4.grid(column=0, row = 4, padx=3, pady=10)

l4 = tk.Listbox(f2, height = 18, width = 63)
l4.grid(column =0, row = 5, columnspan=3, padx = 3)

ss = ttk.Scrollbar(f2, command=l4.yview)
ss.grid(column = 3, row = 5, sticky= 'ns' )
l4['yscrollcommand'] = ss.set
ttk.Sizegrip().pack()
for i in kliendid:
    l4.insert('end', i)
    
button = tk.Button(f2, text="Lisa toode", command=lambda: dr.demo())
button.grid()



######################
# klientide TAB      #
######################


L1 = tk.Label(f3, text="Meie kliendid:")
L1.grid(column=0, row = 4, padx=3, pady=10)

l = tk.Listbox(f3, height = 18, width = 63)
l.grid(column =0, row = 5, columnspan=3, padx = 3)

s = ttk.Scrollbar(f3, command=l.yview)
s.grid(column = 3, row = 5, sticky= 'ns' )
l['yscrollcommand'] = s.set
ttk.Sizegrip().pack()
for i in kliendid:
    l.insert('end', i)
    
button = tk.Button(f3, text="LISA KLIENT", command=lambda: kt.kliendiaken())
button.grid(column =2, columnspan=2, row = 6, pady=10)


######################
#    SEADED          #
######################

button = tk.Button(f4, text="Loo andmebaas", command=lambda: dr.firststart())
button.grid(column = 0, row = 2)
button = tk.Button(f4, text="DEMO", command=lambda: dr.demo())
button.grid(column = 0, row = 3)

fnimil = tk.Label(f4, text="Firmanimi:")
fnimil.grid(column = 1, row = 2)
fnimi = tk.Entry(f4, bd =5)
fnimi.insert(0, sisu(0))
fnimi.grid(column = 2, row = 2, padx=15)

tänavl = tk.Label(f4, text="Tänav, maja, korter:")
tänavl.grid(column = 1, row = 3)
tänav = tk.Entry(f4, bd =5)
tänav.insert(0, sisu(1))
tänav.grid(column = 2, row = 3, padx=15)

linnl = tk.Label(f4, text="Linn, postiindeks:")
linnl.grid(column = 1, row = 4)
linn = tk.Entry(f4, bd =5)
linn.insert(0, sisu(2))
linn.grid(column = 2, row = 4, padx=15)

maakondl = tk.Label(f4, text="Maakond:")
maakondl.grid(column = 1, row = 5)
maakond = tk.Entry(f4, bd =5)
maakond.insert(0, sisu(3))
maakond.grid(column = 2, row = 5, padx=15)

telefonl = tk.Label(f4, text="Telefon:")
telefonl.grid(column = 1, row = 6)
telefon = tk.Entry(f4, bd =5)
telefon.insert(0, sisu(4))
telefon.grid(column = 2, row = 6, padx=15)

emaill = tk.Label(f4, text="E-mail:")
emaill.grid(column = 1, row = 7)
email = tk.Entry(f4, bd =5)
email.insert(0, sisu(5))
email.grid(column = 2, row = 7, padx=15)

regl = tk.Label(f4, text="Reg nr:")
regl.grid(column = 1, row = 8)
reg = tk.Entry(f4, bd =5)
reg.insert(0, sisu(6))
reg.grid(column = 2, row = 8, padx=15)

pankl = tk.Label(f4, text="Pank:")
pankl.grid(column = 1, row = 9)
pank = tk.Entry(f4, bd =5)
pank.insert(0, sisu(7))
pank.grid(column = 2, row = 9, padx=15)

arvel = tk.Label(f4, text="Kontonumber:")
arvel.grid(column = 1, row = 10)
arve = tk.Entry(f4, bd =5)
arve.insert(0, sisu(8))
arve.grid(column = 2, row = 10, padx=15)

button = tk.Button(f4, text="Salvesta andmed", command=lambda:
                   andmed(fnimi.get(), tänav.get(), linn.get(), maakond.get(), telefon.get(), email.get(), reg.get(), pank.get(), arve.get()))
button.grid(column =2, row = 11, padx=10, pady=10)

root.mainloop()
