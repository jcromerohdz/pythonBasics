#Espresiones-Condicionales if, else if (elif)

True
False

print(True==True)

print "Christian" == "christian"

list_a = [1,2,3]
list_b = [1,2,3]
list_c = [11,2,3]

print list_a == list_b
print list_a == list_c

for i in list_a:
    print i
    if (i**2)%3 == 0:
        print "El numero es 9"
        print i

for i in list_a:
    if i == 2:
        print "Si eres 2"
    elif i == 1:
        print("algo diferente")
    else:
        print i

list_d = ["Christian", "coco", "comida", 1234, "otro", 2323]
for i in list_d:
    if isinstance(i, int):
        print str(i) + " Es un numero entero"
    else:
        print i + " Es un string"
    

print isinstance(list_d, list)
