size = int(input("Enter the height of the rhombus: "))
row = 1
while (size >= row):
    for col in range(0, (size - row)):
        print(" ",end=" ")
    for ast in range(0, ((row * 2) - 1)):
        print("*",end=" ")
    print("\n")
    row = row + 1

row = size - 1
while (row>=0):
    for col in range(0, (size - row)):
        print(" ", end=" ")
    for ast in range(0, ((row * 2) - 1)):
        print("*", end=" ")
    print("\n")
    row = row - 1

