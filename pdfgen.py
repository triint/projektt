from reportlab.pdfgen import canvas


def loopdf(arvenumber, kliendinimi, toode1, toode2):
    c = canvas.Canvas("arve" + arvenumber + ".pdf")
    c.drawString(75,750,"FIRMANIMI")
    c.drawString(75,675,'Arve nr:')
    c.drawString(75,660,'Kuupäev:')
    
    c.drawString(75,625,'Maksja:')


    
    c.drawString(75,575,'Toode')
    c.drawString(250,575,'Kogus')
    c.drawString(325,575,'Hind')
    c.drawString(400,575,'Summa')
    
    c.line(65,568,525,568)
    
    c.drawString(75,550,toode1)
    c.drawString(250,550,'1 tk')
    c.drawString(325,550,'4€/kg')
    c.drawString(405,550,'4€')
    c.drawString(75,530,toode2)
    c.drawString(250,530,'1 tk')
    c.drawString(325,530,'4€/kg')
    c.drawString(405,530,'4€')

    c.drawString(325,430,'Summa KM-ta:')
    c.drawString(405,430,'8€')
    c.drawString(325,410,'Käibemaks:')
    c.drawString(405,410,'8€')
    c.drawString(325,390,'SUMMA:')
    c.drawString(405,390,'8€')


    c.line(65,130,525,130)

    c.drawString(75,105,'FIRMANIMI')
    c.drawString(75,90,'Sipelga tn 8-61')
    c.drawString(75,75,'Tallinn 34758')
    c.drawString(75,60,'Harjumaa')
    
    c.drawString(240,105,'Telefon: 538205')
    c.drawString(240,90,'E-mail: jama@jama.ee')
    c.drawString(240,75,'Reg nr: 73578358')
    
    c.drawString(425,105,'SEB')
    c.drawString(425,90,'40385760774')
    

    c.save()
    
