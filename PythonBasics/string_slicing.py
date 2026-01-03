str='sliceit'
# print(str[:2]) #sl -- default start is 0
# print(str[-1]) #t -- -1 is last index
# print(str[0]) #s -- 0 is first index
# print(str[-5:-2]) #ice
#print(str[-5:-2:1]) #ice -- Above and this are same, since direction is positive
#print(str[-5:-2:0]) #will not work since zero is not allowed
# print(str[:-2]) #slice
# print(str[-2:-1]) #i
#print(str[-2:2]) # No output since START=-2 is 'i' but direction is positive(L to R)
#print(str[-2:2:-1]) #iec since we are going in reverse direction (R to L)

#print(str[-1:0:-1]) #tiecil
#print(str[:0:-1]) #tiecil - Since Direction is R to L so default START=-1
print(str[-1::-1]) #tiecils - Since END is not given so it will take till last index L to R  END=length of array/ count, R to L=
print(str[0::1])

