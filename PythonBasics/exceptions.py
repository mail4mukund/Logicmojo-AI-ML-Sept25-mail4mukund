
a=int(input('Enter your total marks:\t'))
b=int(input('Enter number of subjects:\t'))

perc=a/b
print('Value of\n {}/{} = {}'.format(a,b,perc))

for x in range(1,20,1):
    if(x>10):
        break
    print(f"Value from the loop of rang function:{x}")
