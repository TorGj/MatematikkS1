from numpy import *
from random import *

bolle = ['Blå']*2 + ['Rød']*3
#print(bolle)

Ant_trekk = 10

trekk=[]
utfall_br = 0

for i in range(Ant_trekk):
    trekk.append(choice(bolle))
    trekk.append(choice(bolle))
    utfall_br = utfall_br + int((trekk[2*i] == 'Blå') and (trekk[2*i+1] == 'Rød'))
    #print((trekk[2*i] == 'Blå') and (trekk[2*i+1] == 'Rød'))

print(trekk)
print('Relativ frekvens for "først Blå så Rød" er:', utfall_br/Ant_trekk)
