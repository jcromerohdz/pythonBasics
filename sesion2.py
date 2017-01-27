#Listas, Diccionarios, Tuplas

#Listas en python
abc = "Algo aqui!"
print abc[0]

# Create a list in python/ crear un lista en python
l=[]
l = ["Algo aqui", "Otra cosa aqui", 123]
print l

# Add an elemnt to a list / agragar un elemento a lista
l.append("otro elemento")
print l

# Delete the last item in the list/ Borrar el ultimo elemento de la Lista
l.pop()
print l

# See the len of a list/Ver la longitud de la lista
print len(l)

# Index an element in a list/Indexar la lista comienza en 0
print l[0]
print l[2]

#Sort an unorder list/ Ordenar una lista
l2 = [8,9,30,4,1,40,6,20,33]
l2.sort()
print l2

# Asign a variable to a list element / Asignar a una variable a un elemento de la lista
nombres = ["Christian", "Juan", "Carlos"]
carlos = nombres[2]
print carlos

# Delete an element in a list/Borrar un elemento de la lista
nombres = ["Christian", "Juan", "Carlos"]
nombres.pop(1)
print nombres

#Dictionaries in python/

d = {"nombre":"Christian",
     "edad":"??",
     "direccion":"Zamora # 11 col marron"}

print d["nombre"]
d["nombre"] = "Jose"
print d

d.update({"telefonos":["6642547436", "6646763067"]})
print d
print d["telefonos"][0]
print type(d['telefonos'][0])
print "telefono 1: " + d['telefonos'][0]
print d["telefonos"][1]

#Another way to update a dictionaries
d["emails"]={"email_1":"jcromerohdz@gmail.com",
             "email_2":"crhdragon@gmail.com"}
print d
print d["emails"]["email_2"]

#Tuples
t = ()
t = ("abc", "abc")
print type(t)
t = (("hola", "hola2"), "Hello")
print t
print t[0][1]
