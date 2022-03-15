from pylab import *

utfallsrom = ["rød", "blå", "gul", "grå"] # utfallsrommet
sannsynligheter = [1/3, 1/3, 1/6, 1/6]    # sannsynlighetene for utfallene
lykkehjul = choice(utfallsrom, p = sannsynligheter) # simulerer lykkehjulet

print("Lykkehjulet stoppet på", lykkehjul)