lenth=float(input('enter length :\n'))
widht=float(input('enter width :\n'))
area=lenth*widht
print('area of the shape is : '+str(area))

if area>100:
    print("Area is more than hundred")
elif area>50:
    print("it is more than fifty") 
else:
    print('Ah it is less than Fifty')