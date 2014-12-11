import dataret as dr
import datainp as di
import klient_tab as kt
from pdfgen import *
from seaded import *

import tkinter as tk
import tkinter.ttk as ttk


root = tk.Tk()
###
root.geometry("%dx%d+%d+%d" % (450, 450, 100, 50))
root.title('MinuLadu ver 0.1')

nb = ttk.Notebook(root)
nb.pack(fill='both', padx = 7, pady = 7, expand='yes')

# Loo tabid

f1 = tk.Frame()
f2 = tk.Frame()
f3 = tk.Frame()
f4 = tk.Frame()

# Loo lehed

nb.add(f1, text='Arved')
nb.add(f2, text='Ladu')
nb.add(f3, text='Kliendid')
nb.add(f4, text='Seaded')


####################
# Arve lisamine    #
####################

##### listid

kliendid = dr.outkliendid()
tooted = dr.outtooted()

#### kliendi valimine
label1 = tk.Label(f1, text="Kliendi nimi:")
label1.grid(column = 0, row = 4, pady=5, sticky='w')

klient = tk.StringVar(f1)
klient.set(kliendid[0]) # default value

w = tk.OptionMenu(f1, klient, *kliendid)
w.grid(column = 1, row = 4,  pady = 5)


#### Kuupäev

kuupl = tk.Label(f1, text="Kuupäev:")
kuupl.grid(column =0, row = 5,  pady=1, sticky='w')
kuup = tk.Entry(f1, bd =5)
kuup.grid(column =1, row = 5,  pady=1)


tekst = tk.Label(f1, text="Toodete arvele lisamine:")
tekst.grid(column =0, row = 6, pady=20, sticky='w')

###### toode 1
label2 = tk.Label(f1, text="Toode:")
label2.grid(column = 0, row = 7, pady=1, sticky='w')

toode1 = tk.StringVar(f1)
toode1.set(tooted[0]) # default value

w2 = tk.OptionMenu(f1, toode1, *tooted)
w2.grid(column =1, row = 7, pady=1)


######### toode 1 kogus

L1 = tk.Label(f1, text="Kogus:")
L1.grid(column =0, row = 8, pady=1, sticky='w')
E1 = tk.Entry(f1, bd =5)
E1.grid(column =1, row = 8, pady=1)

######### arve number

f = open('arvenumber.txt')
arvenumber = f.read()
f.close()

##### loo arve nupp
def ok():
    print("value is", klient.get())
    
button = tk.Button(f1, text="Lisa toode", command=lambda: lisatoode(arvenumber, toode1.get(), E1.get()))
button.grid(column =2, row = 8, padx=10, pady=10)

button = tk.Button(f1, text="Loo arve", command=lambda: loopdf(kuup.get(), klient.get()))
button.grid(column =2, row = 10, padx=10, pady=50, sticky ='e')

button = tk.Button(f1, text="Hetkeseis", command=lambda: kt.hetkeseis())
button.grid(column =2, row = 9, padx=10, pady=10)

######################
#    Tooted laos     #
######################

label4 = tk.Label(f2, text="Tooted laos:")
label4.grid(column=0, row = 4, padx=3, pady=10)

l4 = tk.Listbox(f2, height = 18, width = 63)
l4.grid(column =0, row = 5, columnspan=3, padx = 3)

ss = ttk.Scrollbar(f2, command=l4.yview)
ss.grid(column = 3, row = 5, sticky= 'ns' )
l4['yscrollcommand'] = ss.set
ttk.Sizegrip().pack()
for i in tooted:
    l4.insert('end', i)
    
button = tk.Button(f2, text="LISA TOODE", command=lambda: kt.tooteaken())
button.grid(row = 6, column= 2, pady = 10, sticky = 'e')


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
