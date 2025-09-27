def findSumForNumbers(*parms):
    total=0;
    for a in parms:
        print(f'Value added in total is :{a}')
        total+=a;
    return total

val=findSumForNumbers(1,4,6,2)
print(f'Sum of given number is = {val}')

def SumNumbers(a, b, c, d):
    print(f'Value received in function parameters are a={a}, b={b}, c={c}, d={d}')
    return a+b+c+d;

SumNumbers(1,2,4,5)

SumNumbers(d=1,c=2,b=4,a=5)


def SumNumericValue(a, b,/, c, d):
    print(f'Value received in function parameters are a={a}, b={b}, c={c}, d={d}')
    return a+b+c+d;



calc = SumNumericValue(10, 20, 30, 40)
print(calc)


#create a method for decorators:
def createDecorator(func):
    def myInner():
        return func().upper()
    return myInner

@createDecorator
def myFunction():
    return "my name is mukund kumar"

print(myFunction())