str ='mukund'
for a in str:
    print(a)

for a in 'Kumar':
    print(a)

print(str[1])

if('mukund' in 'mukund Kumar'):
    print('name found here in string')
else:
    print('Name not found')

print('******************Not in practice**********************')

if('mukund' not in 'mukunsd Kumar'):
    print('name not found here in string')
else:
    print('Name found')


#prnValue="My name is %a and my age is %b" %('mukund', 40)
#print(prnValue)