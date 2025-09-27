#numberOflines = int(input('Enter number of lines: '))
'''spacePrinter=''
for a in range(10):
    spacePrinter += ' '
#spacePrinter.extend(spacePrinter*numberOflines)

print(spacePrinter+'*',sep='')
spacePrinter[0]=''
spacePrinter[1]=''
print(spacePrinter+'*',sep='')'''

name="Mukund"
print(name[0])
name+=' Kumar'
print(name)
t='Mr.'
n='Mukund'
s='Kumar' 
name=f"Hi {t} {n} {s}"
print(name)

name= name.replace('Kumar','Prasad')
print(name)
spacePrinter=''
for a in range(10):
    spacePrinter += ' '
spacePrinter= ''.join(spacePrinter)
print(spacePrinter+'*')

#Remove one character
print(spacePrinter[:-1]+'*')

print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.swapcase())
print(name.title())
print(name.strip())
print(name.lstrip())
print(name.find('m'))
print(name.casefold('m'))






