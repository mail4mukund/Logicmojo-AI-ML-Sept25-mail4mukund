import cmath

lst=[3,2,4,1,5,2]
for i in lst:
    print(i)
print('Conversion of List in SET\n We see duplicate value is removed in Set')
st=set(lst)
for i in st:
    print(i)

j=10
eq = 9 + 2j
print('Value of equation'+str(eq))

k=complex(3+9)
print('Value of complex data type: '+ str(cmath.cos(0)))

dtype=cmath.cos(90)
print(type(dtype))
print('Value of cos 90 is: '+ str(dtype))
