matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print("Matrix is:")
print("[",end="")
for row in matrix:
    for k in row:
        print(k,end=", ")
    print()
print("]",end="")


print(matrix.pop(-1)[0])
print(matrix.pop(1)[0])
