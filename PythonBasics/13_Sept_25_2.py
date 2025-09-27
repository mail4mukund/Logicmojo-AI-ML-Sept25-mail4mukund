import datetime
a=11.0
b=23
print(type(a))

setV={a,'mukund', 23, 'Chautham'}
print(type(setV))

setV=[a,'mukund', 23, 'Chautham']
print(type(setV))

setV={a,b,'mukund', 23, 'Chautham'}
print(type(setV))

a, b= input('Enter multiple value').split()
print(a)
print(b)
print(type(a))

a1, b1= map(int,input('Enter multiple value').split())
print(a1)
print(b1)
print(type(a1))

print('Map method call with list of values')
def func11(k):
    print('Value is:'+str(k))
    return int(k)  


aaa=map(func11,[1,2,3])
print(type(aaa))

#s=[d[x] for x in l]