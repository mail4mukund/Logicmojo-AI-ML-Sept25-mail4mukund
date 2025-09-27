import keyword

x=y=z=input('Enter value for assignment:')
print(x)
print(y)
print(z)

print('Check if all Values are on same memory location:', x is y is z)

li=input('Enter multiple value :').split(' ')

print('Print vlaue that you input in list')
for l in li:
 print(l)

print('Print all keyword that present in current version of Python')
lst=keyword.kwlist #Provides the list of all Keyword


print(type(lst))

myTuple=tuple(lst)
print(type(myTuple))
for l in myTuple:
  print(l)