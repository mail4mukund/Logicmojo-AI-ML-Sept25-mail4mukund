name=input('Enter your name')
match name:
    case 'Mukund':
        print('Welcome :' + name)
    case 'Kumar':
        print('Welcome :' + name)
    case 'Sri':
       print('Welcome :' + name)

print('Even Number Print:')
counter=1
for counter in range(1,50):
    if(counter%2==0):
        print(counter)

print('Used while method for the same!')
counter=100
while counter in range(1,50):
    if(counter%2==0):
        print(counter)
    counter+=1
else:
    print('Not running any while condition')

