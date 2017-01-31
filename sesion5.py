#Functions
l = ["Christian", 21, "telefono", 10.10]

print l

int_el = [12.3, 1, 34, 34234, 99, 4.5]
int_el.sort()
print int_el
int_el.sort(reverse=True)
print int_el

suma_el = sum(int_el)
print suma_el
avg_number = sum(int_el)/len(int_el)
print avg_number

items = ["Telefono", "Computadora", 3.1416, 23, "Christian", "bolsa", 2234]
str_items = []
num_items = []

for i in items:
    if isinstance(i, float) or isinstance(i, int):
        num_items.append(i)
    elif isinstance(i, str):
        str_items.append(i)
    else:
        pass

print str_items
print num_items

def analizar_lista(lista):
    str_list_items = []
    num_list_items = []
    for i in lista:
        if isinstance(i, float) or isinstance(i, int):
            num_list_items.append(i)
        elif isinstance(i, str):
            str_list_items.append(i)
        else:
            pass
    return str_list_items, num_list_items

print analizar_lista(items)

#print sum(items)


def my_sum(num_list):
    total = 0
    for i in num_list:
        if isinstance(i, float) or isinstance(i, int):
            total += i
    return total

print my_sum(items)
