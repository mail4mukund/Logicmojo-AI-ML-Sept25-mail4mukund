mytuple = ("apple", "banana", "cherry")
mytuple = ("apple")
print(mytuple);

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])


#Unpacking of tuples
fruits = ("apple", "banana", "cherry")

(g1, yellow, red) = fruits

print(g1)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)


fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)