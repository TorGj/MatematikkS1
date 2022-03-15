from numpy import *
from random import *

'''Programmet nedenfor simulerer 100 terningkast og regner ut den relative frekvensen for seksere i de 100 kastene.
Kjør programmet noen ganger og se hva du får. Legg merke til at den relative frekvensen for seksere vil variere 
noe fra en simulering til en annen.'''

N = 100             # antall kast
terningkast = [ ]   # tom liste for antall øyne

for element in range(N):  # løkke som utfører terningkastene
  terningkast.append(randint(1,7))

terningkast = array(terningkast)  # gjør om lista til en array
n = sum(terningkast == 6)         # bestemmer antall seksere
rel_frekv = n/N                   # regner ut relativ frekvens

print("Antall kast:", N)
print("Antall seksere:", n)
print("Relativ frekvens:", rel_frekv)