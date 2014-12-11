def andmed(a, b, c, d, e, f, g, h, i):
    fail = open('andmed.txt', 'w')
    fail.write(a)
    fail.write('\n')
    fail.write(b)
    fail.write('\n')
    fail.write(c)
    fail.write('\n')
    fail.write(d)
    fail.write('\n')
    fail.write(e)
    fail.write('\n')
    fail.write(f)
    fail.write('\n')
    fail.write(g)
    fail.write('\n')
    fail.write(h)
    fail.write('\n')
    fail.write(i)


def sisu(number):
    faill = open('andmed.txt')
    read = faill.readlines()
    return read[number]
