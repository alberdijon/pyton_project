def exercise14():
    items = []
    for i in range(100, 401):
        s = str(i)
        if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0):
            items.append(s)
    print( ",".join(items))

def exercise21():
    my_list = []
    if my_list == []:
        print("The list is empty")
    elif my_list != []:
        print("The list is not empty")

def exercise20():
    final_list = []
    duplicate = [1,1,2,2,3,4,5,5,6,7,8,8,9,0,0,]
    for x in duplicate:
        if x not in final_list:
            final_list.append(x)
    print(final_list)

def exercise19():
    list1 = []
    num = int(input("Enter number of elements in list: "))
    for i in range(1, num + 1):
        numbs = int(input("Enter elements: "))
        list1.append(numbs)

    print("Smallest element is:", min(list1))

exercise19()

