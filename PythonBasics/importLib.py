import random

a=random.randint(1,50);
# print(a)
colors=[]
colors.append('red')
colors.append('blue')
colors.append('black')
colors.append('green')
colors.append('gray')
colors.append('brown')
inputColor = input ('Enter your color choice: \n')
if inputColor in colors:
    print('Yeh I found your colors: '+ inputColor)
elif a%2==0:
    print('Random guess is even number'+ str(a))
else:
    print('No luck with computer choice or color choice? \n' + inputColor +"\n" + str(a))


for a1 in colors:
    print(a1);

#create a list of 1 to 50 as arry
numbers=[];
for k in range(1,20,1):
    numbers.append(k)

print('Sum of upto 20 all numbers: \n'+ str(int(sum(numbers))))


