from reportlab.pdfgen import canvas
import sqlite3
import os
from seaded import *
from dataret import *

def lisatoode(arvenumber, toode, kogus):
    f = open('arve.txt', 'a')
    if os.path.isfile('arve.txt') and os.path.getsize('arve.txt') > 0:
        f.write('{} \n'.format(toode))
        f.write('{} \n'.format(kogus))
    else:
        f.write('{} \n'.format(arvenumber))
        f.write('{} \n'.format(toode))
        f.write('{} \n'.format(kogus))
    f.close()
        
def loopdf(kuupaev, kliendinimi):
    f = open('arvenumber.txt')
    arvenr = int(f.read())
    f.close()
    c = canvas.Canvas("arve" + str(arvenr) + ".pdf")
    c.drawString(75,750,sisu(0).strip('\n'))
    c.drawString(75,675,'Arve nr: ' + str(arvenr))
    c.drawString(75,660,'Kuupäev: ' + kuupaev)
    
    c.drawString(75,625,'Maksja: ' + kliendinimi)


    
    c.drawString(75,575,'Toode')
    c.drawString(250,575,'Kogus')
    c.drawString(325,575,'Hind')
    c.drawString(400,575,'Summa')
    
    c.line(65,568,525,568)
    
    i = 1
    summa = 0
    tooted = outtooted()
    while i < arveread():

        a = 550 - ((i-1) * 10)
        hind = hindid(tooted.index(sisu2(i).strip(' \n')))
        kogus = int(sisu2(i+1).strip('\n'))
        
        c.drawString(75,a,sisu2(i).strip('\n'))
        c.drawString(250,a,sisu2(i+1).strip('\n') + ' tk')
        c.drawString(325,a,str(hind) + ' €/tk')
        c.drawString(405,a, str(hind * kogus) + ' €')
        i += 2
        summa += hind * kogus

    
    kaive = summa * 0.2
    kokku = summa * 1.2
    c.drawString(325,430,'Summa KM-ta:')
    c.drawString(405,430,str(summa) + ' €' )
    c.drawString(325,410,'Käibemaks:')
    c.drawString(405,410,str(kaive) + ' €')
    c.drawString(325,390,'SUMMA:')
    c.drawString(405,390,str(kokku) + ' €' )


    c.line(65,130,525,130)

    c.drawString(75,105,sisu(0).strip('\n'))
    c.drawString(75,90,sisu(1).strip('\n'))
    c.drawString(75,75,sisu(2).strip('\n'))
    c.drawString(75,60,sisu(3).strip('\n'))
    
    c.drawString(240,105,'Telefon: ' + sisu(4).strip('\n'))
    c.drawString(240,90,'E-mail: ' + sisu(5).strip('\n'))
    c.drawString(240,75,'Reg nr: ' + sisu(6).strip('\n'))
    
    c.drawString(425,105,sisu(7).strip('\n'))
    c.drawString(425,90,sisu(8).strip('\n'))
    

    c.save()
    
    f = open('arvenumber.txt')
    arvenr = int(f.read())
    f.close()
    f = open('arvenumber.txt', 'w')
    arvenr += 1
    f.write(str(arvenr))
    f.close()
    os.remove('arve.txt')
    
