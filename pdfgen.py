from reportlab.pdfgen import canvas


def loopdf(arvenumber, kliendinimi, toode1, toode2):
    c = canvas.Canvas("arve" + arvenumber + ".pdf")
    c.drawString(100,750,"FIRMANIMI")
    c.drawString(100,675,'Arve nr:')
    c.drawString(100,660,'Kuupäev:')
    
    c.drawString(100,625,'Maksja:')


    c.line(100,600,550,600)
    c.drawString(100,575,'Toode')
    c.drawString(275,575,'Kogus')
    c.drawString(350,575,'Hind')
    c.drawString(425,575,'Summa')
    c.drawString(100,550,toode1)
    c.drawString(275,550,'1 tk')
    c.drawString(350,550,'4€/kg')
    c.drawString(425,550,'4€')
    c.drawString(100,530,toode2)
    c.drawString(275,530,'1 tk')
    c.drawString(350,530,'4€/kg')
    c.drawString(425,530,'4€')

    c.drawString(350,430,'KOKKU:')
    c.drawString(425,430,'8€')

    c.drawString(100,330,'Krista Teearu')
    c.drawString(100,315,'Juhataja')

    c.line(100,300,550,300)

    c.drawString(100,275,'FIRMANIMI')
    c.drawString(100,255,'Sipelga tn 8-61')
    c.drawString(100,235,'Tallinn 34758')
    c.drawString(100,215,'Harjumaa')
    
    c.drawString(275,275,'Telefon: 538205')
    c.drawString(275,255,'E-mail: jama@jama.ee')
    c.drawString(275,235,'Reg nr: 73578358')
    
    c.drawString(450,275,'SEB')
    c.drawString(450,255,'40385760774')
    

    c.save()
    
