from FunctionsHaritz1 import *
from rock_paper_scisors import *


list_events = []

option=24
while option!=12:
    print("THE CALENDAR MENU (Choose a task typing its number!)")
    print("==================================================")
    print("1--Print calendar")
    print("2--Add event")
    print("3--Remove events")
    print("4--Show events")
    print("5--Play Rock,Paper,Scissors")
    print("6--Show how many events are added.")
    print("7-Dawing machine.")
    print("8--Exercises.")
    print("9--Save events in a txt file.")
    print("10--Show the txt file with the events")
    print("11--Search in the file.")
    print("12-Exit")

    option= int(input("Enter the number of an option from the menu: "))
    if option==1:
        print_calendar()
    if option==2:
        addevents(list_events)
    if option == 7:
        drawingMachine()
    if option == 4:
        show_events(list_events)
    if option == 3:
        deleteEventPosition(list_events)
    if option == 6:
        howManyEvents(list_events)
    if option == 8:
        exercises()
    if option == 5:
        rock_paper_scisors()
    if option == 9:
        saveEventsInAfile(list_events)
    if option == 10:
        showDocument()
    if option == 11:
        findInFile()








