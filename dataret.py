import sqlite3


#loo andmebaas
def firststart():
    db = sqlite3.connect('test.db')
    #kustutab eelmised tabelid
    db.execute('drop table if exists kliendid')
    db.execute('drop table if exists tooted')
    
    db.execute('create table kliendid (t1 text, i1 int, t2 text)')
    db.execute('create table tooted (t1 text, i1 int, i2 int)')
    
    db.commit()
    sisestaklient('Kliendi nimi', 1, 'nimi@mail.ee')
    sisestatoode('toote nimi', 1, 2)
    

#sisestan kliendi andmeid
def sisestaklient(nimi, kliendinumber, email):
    db = sqlite3.connect('test.db')
    db.execute('insert into kliendid (t1, i1, t2) values(?, ?, ?)', (nimi, kliendinumber, email))
    db.commit()
    #kliendid = outkliendid()
    
#sisestan tooted
def sisestatoode(nimi, tootenumber, hind):
    db = sqlite3.connect('test.db')
    db.execute('insert into tooted (t1, i1, i2) values(?, ?, ?)', (nimi, tootenumber, hind))
    db.commit()    
      
   
#firststart()
def demo():    
    sisestaklient('Kliendi nimi', 1, 'nimi@mail.ee')
    sisestatoode('toote nimi', 1, 2)
  



#väljastan nimekirjad

def outkliendid():
    db = sqlite3.connect('test.db')
    db.row_factory = lambda cursor, row: row[0]
    cursor = db.execute('select t1 from kliendid order by t1')
    kliendid = []
    for row in cursor:
        kliendid = kliendid + [row]
    return(kliendid)

def outtooted():
    db = sqlite3.connect('test.db')
    db.row_factory = lambda cursor, row: row[0]
    cursor = db.execute('select t1 from tooted order by t1')
    tooted = []
    for row in cursor:
        tooted = tooted + [row]
    return(tooted)
    
def hindid(id):
    db = sqlite3.connect('test.db')
    db.row_factory = lambda cursor, row: row[0]
    cursor = db.execute('select i2 from tooted order by t1')
    hinnad = []
    for row in cursor:
        hinnad = hinnad + [row]
    
    return(hinnad[id])


    

