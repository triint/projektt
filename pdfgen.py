from reportlab.pdfgen import canvas


def loopdf(arvenumber, kliendinimi, toode1, toode2):
    c = canvas.Canvas("arve" + arvenumber + ".pdf")
    c.drawString(100,750,"Lugupeetud " + kliendinimi)
    c.drawString(100,650,toode1)
    c.drawString(100,550,toode2)
    c.save()
    