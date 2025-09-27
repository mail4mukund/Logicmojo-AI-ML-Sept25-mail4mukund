import random

def sum(a, b):
	return a + b


inpt1= input('Enter your first value\n')
inpt2= input('Enter your 2nd value\n')

print('Sum of both Number:'+ str(sum(int(inpt1),int(inpt2))))


rand1=random.randint(1,6)
rand2=random.randint(1,6)

print('Sum of both Random Number:'+ str(sum(int(rand1),int(rand2))))
