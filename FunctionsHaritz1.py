from ExerciseExample import *
import os
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
    f = open("events.txt", "w+")

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
    option = 24
    while option != 4:
        print("WELCOME TO THE DRAWING MACHINE!")
        print("=========================")
        print("What do you want to draw?")
        print("=========================")
        print("1.- Drawing a pyramid.")
        print("2.- Drawing a triangle.")
        print("3.- Dawing a rombous.")
        print("4.- Exit program.")
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
    number = int(input("Enter the number you want to see the multiplication table: "))
    print("The Multiplication Table of: ", number)
    for count in range(1, 11):
        print(number, 'x', count, '=', number * count)
def ex11():
    filas = int(input("Enter his number of rows: "))
    filas = filas + 1
    for i in range(filas):
        for j in range(i):
            print(i, end=' ')
        print('')

def exercises():
    option = 24
    while option != 10:
        print("EXERCISES MENU")
        print("=========================")
        print("CHOOSE AN EXERCISE: ")
        print("=========================")
        print("1.- Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included). ")
        print("2.- Python program to count the number of even and odd numbers from a series of numbers. ")
        print("3.- Python program to create the multiplication table (from 1 to 10) of a number.")
        print("4.- Python program to construct the number triangle pattern")
        print("5.- Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number.")
        print("6.- Python program to get the smallest number from a list")
        print("7.- Python program to remove duplicates from a list.")
        print("8.- Python program to check a list is empty or not.")
        print("9.- Python program to get the second smallest number from a list")
        print("10.- Exit program.")
        print("Enter the number of the exercise: ")

        option = int(input("Please, enter the number of the exercise you want to see: "))

        if option == 1:
            ex1()
        if option == 2:
            ex4()
        if option == 3:
            ex10()
        if option == 4:
            ex11()
        if option == 5:
            exercise14()
        if option == 6:
            exercise19()
        if option == 7:
            exercise20()
        if option == 8:
            exercise21()
        if option == 9:
            secondSmallestNumber()
def secondSmallestNumber():
    nums = []
    print(end="Enter the Size of List: ")
    listSize = int(input())
    print(end="Enter " + str(listSize) + " Numbers for List: ")
    for i in range(listSize):
        nums.append(int(input()))

    small = nums[0]
    for i in range(listSize):
        if small > nums[i]:
            small = nums[i]

    secondSmall = nums[1]
    for i in range(listSize):
        if secondSmall > nums[i] and nums[i] != small:
            secondSmall = nums[i]

    if small == secondSmall:
        print("\nSecond Smallest Number doesn't exist!")
    else:
        print("\nSecond Smallest Number = " + str(secondSmall))
def saveEventsInAfile(le):

    print("Save events in a txt file.")
    print("==================================================")
    print("1--Rewrite")
    print("2--Add")

    option = int(input("Enter the number of an option from the menu: "))
    if option == 1:
        f = open("events.txt", "w+")

        for element in le:
            f.write(element + "\n")
        f.close()
    if option == 2:
        f = open("events.txt", "a+")

        for element in le:
            f.write(element + "\n")
        f.close()


def showDocument():
    f = open("events.txt", "r")
    a = 1
    while a != 0:
        file_line = f.readline()
        if not file_line:
            print("End Of File")
            a = 0
        else:
            print(file_line)
            print("")
            print(a)
            a = a + 1
    f.close()

