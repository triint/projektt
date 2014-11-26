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
    sisestaklient('Jaak', 1, 'jaak@mail.ee')
    sisestaklient('Mari', 2, 'mari@mail.ee')
    sisestaklient('Jüri', 3, 'jyri@mail.ee')
    sisestatoode('apelsiin', 1, 2)
    sisestatoode('mandariin', 2, 3)
    sisestatoode('banaan', 3, 5)



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


    
#cursor = db.execute('select * from tooted order by t1')
#for row in cursor:
#    print(row)
	
