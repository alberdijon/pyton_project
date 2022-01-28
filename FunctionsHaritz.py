def print_calendar():
   import datetime
   import calendar
   year = datetime.datetime.now()
   print(calendar.calendar(year.year))


def delete_event(events):

    del events[:]
    print(events)


def show_events(events):
      print (events)
def addevents (events):


    print("You have chosen to add an event.")
    event_num = int(input("How many events you want to add?"))
    i = 0
    while i < event_num:
        event = input("Enter the event you have and specify thr date.")
        events.append(event)
        i += 1

def pyramid ():
    n = int(input("Enter the height of the pyramid: "))
    k = n -1

    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")

        k = k -1
        for j in range(0, i+1):
            print("* ", end="")
        print("\r")
def triangle():
    n = int(input("Enter the height of the triangle: "))
    fila = []
    for i in range(1,n+1):
        fila.append("*"*i)
    print("\n".join(fila))

def rombous():
    size = int(input("Enter the height of the rhombus: "))
    row = 1
    while (size >= row):
        for col in range(0, (size - row)):
            print(" ", end=" ")
        for ast in range(0, ((row * 2) - 1)):
            print("*", end=" ")
        print("\n")
        row = row + 1

    row = size - 1
    while (row >= 0):
        for col in range(0, (size - row)):
            print(" ", end=" ")
        for ast in range(0, ((row * 2) - 1)):
            print("*", end=" ")
        print("\n")
        row = row - 1


def drawingMachine ():

    print("WELCOME TO THE DRAWING MACHINE!")
    print("=========================")
    print("What do you want to draw?")
    print("=========================")
    print("1.- Drawing a pyramid.")
    print("2.- Drawing a triangle.")
    print("3.- Dawing a rombous.")


    print("5.- Exit program.")
    print("Enter the number of the exercise: ")

    option = int(input("Please, enter the number depending of the drawing you want to draw."))

    if option == 1:
        pyramid()
    if option == 2:
        triangle()
    if option == 3:
        rombous()

def howManyEvents(events):
    numberOfElements = len(events)

    print("Number of events active ", numberOfElements)

def deleteEventPosition(events):
    a = len(events)
    print(a)
    i=0
    while i < a:
        print(i+1,end=" ")
        print(events[i])
        i=i+1

    numberEvent = int(input("Select the position of the event: "))
    events.pop(numberEvent-1)
    print(events)

def ex1():

    lista=[]
    for x in range(1500, 2701):
        if (x % 7 == 0) and (x % 5 == 0):
            lista.append(str(x))
    print(','.join(lista))

def ex4():
    numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20)
    odd = 0
    even = 0
    for x in numbers:
        if not x % 2:
            even += 1
        else:
            odd += 1
    print("Number of even numbers :", even)
    print("Number of odd numbers :", odd)
def ex10():

    number = input("Enter the number yo want to see the multiplication table: ")
    for i in range(1, 11):
        print(number, 'x', i, '=', number * i)
def ex11():
    numbers = []
    for i in range(100, 401):
        s = str(i)
        if (int(s[0]) % 2 == 0) and (int(s[1]) % 2 == 0) and (int(s[2]) % 2 == 0):
            numbers.append(s)
    print(",".join(numbers))