def andmed(a, b, c, d, e, f, g, h, i):
    fail = open('andmed.txt', 'w')
    fail.write(a.strip('\n'))
    fail.write('\n')
    fail.write(b.strip('\n'))
    fail.write('\n')
    fail.write(c.strip('\n'))
    fail.write('\n')
    fail.write(d.strip('\n'))
    fail.write('\n')
    fail.write(e.strip('\n'))
    fail.write('\n')
    fail.write(f.strip('\n'))
    fail.write('\n')
    fail.write(g.strip('\n'))
    fail.write('\n')
    fail.write(h.strip('\n'))
    fail.write('\n')
    fail.write(i.strip('\n'))


def sisu(number):
    faill = open('andmed.txt')
    read = faill.readlines()
    return read[number]
    
def sisu2(number):
    faill = open('arve.txt')
    read = faill.readlines()
    return read[number]
def arveread():
    ridasid = (sum(1 for line in open('arve.txt')) - 1)
    return ridasid
    