#Loops (for, while)

#for loop
bolsa = [10, 4 ,2 ,333, 444, 24324, 55454]
print len(bolsa) # 7 items/elementos

for i in bolsa:
    print i

c = 0 # counter/contador
for i in bolsa:
    c = c + 1
    print c

bolsa = ["aguacates", "carne", "frijoles"]

for i in bolsa:
    if i == "carne":
        print "Ya se armo la carne asada"
    else:
        print  "No se armo!"


#while loop
i= 10
while i < 11:
    print "hello"
    print i
    i+=1

i = 0
while i < 100:
    print i
    i+=1
