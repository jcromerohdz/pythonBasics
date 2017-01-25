#Strings, variables, enteros(Integers)
#Strings
print "Esto es un string!"
print 'Esto tambien es un string'
print """Esto tambien es un string"""
print "asi puedo concatenar un string"+" con el signo mas"

#Variables
s3 = "Christian"
s2 = "Como estas!"
saludo = s2 + " " +s3
print saludo
n1 = 1
print s2 + str(1)
print s3 * 2

#Integers
print 1 + 5
print 5 - 2
print 5 * 2
print 5/2.0

n = 3
n2 = 6.0
r = n / n2
nr = n**2

print "resultado: " + str(r)
print "resultado: " + str(nr)

def suma(a,b):
    return a + b

print "resultado de la funcion suma: " + str(suma(5,5))
print type(n)
print type(saludo)
print type(suma(5,5))

if 5 > 4:
    print "5 es mayor que 4"
else:
    print "5 no es mayor que el numero x"

for i in range(1,11):
    print "hola!"

#fibonacci series
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

print fib(7)
