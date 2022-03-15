g = 0 # definerer en variabel for antall gunstige utfall
for t1 in range(1,7): # går gjennom alle de mulige utfallene
  for t2 in range(1,7):
    for t3 in range (1,7):
      if t1 + t2 + t3 == 9: # for sum lik 9, øker vi g med 1
        g = g + 1
print("Det er", g, "gunstige utfall.")