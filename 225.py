from pylab import *

N = 10000           # antall kast
roed_terning = [ ]  # tom liste for antall øyne på rød terning
blaa_terning = [ ]  # tom liste for antall øyne på blå terning

for kast in range(N): # løkke for kast med de to terningene
    roed_terning.append(randint(1,7))
    blaa_terning.append(randint(1,7))

roed_terning = array(roed_terning) # gjør om listene til arrayer
blaa_terning = array(blaa_terning)

terninger_sum = roed_terning + blaa_terning # finner summen av antall øyne
n = sum(terninger_sum == 9) # teller opp antall ganger summen blir ni
rel_frekv = n/N             # finner relativ frekvens for sum ni

print("Relativ frekvens for sum ni:", round(rel_frekv, 3))