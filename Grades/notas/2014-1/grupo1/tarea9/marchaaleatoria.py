import sys
import math
import random

R = float(sys.argv[1])

A = 0.0
B = 0.0
C = 0.0

x = 0.0
y = 0.0
z = 0.0

r = 0.0
thetha1 = 0.0
thetha2 = 0.0

Npasos = 0.0

lstx = []
lsty = []
lstz = []
lstNpasos = []
lstr = []

def rifadeangulos():
    radian = (random.random())*(2*math.pi)
    return radian

while (r<R):
    thetha1 = rifadeangulos()
    thetha2 = rifadeangulos()

    A = (math.sin(thetha1))*(math.cos(thetha2))
    B = (math.sin(thetha1))*(math.sin(thetha2))
    C = math.cos(thetha1)
    
    x += A
    y += B
    z += C
    Npasos += 1
    r = (math.sqrt((math.pow(x, 2))+(math.pow(y, 2))+(math.pow(z, 2))))

    lstx.append(x)
    lsty.append(y)
    lstz.append(z)
    lstNpasos.append(Npasos)
    lstr.append(r)

archivoxyzNpasosr = open('marcha-aleatoria.dat', 'w')

for i in range (len(lstx)):
    archivoxyzNpasosr.write(str(lstx[i])+"   "+str(lsty[i])+"   "+str(lstz[i])+"   "+str(lstNpasos[i])+"   "+str(lstr[i])+"\n")

archivoxyzNpasosr.close()






    


