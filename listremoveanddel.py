#program to remove and del in list
#ishan hambir

#remove
l = ['Alice', 'Bob', 'Charlie', 'Bob', 'Dave']

l.remove('Alice')
print(l)

#del
l = [0, 10, 20, 30, 40, 50]

del l[0]
print(l)

del l[3]
print(l)

del l[-1]
print(l)

del l[-2]
print(l)
