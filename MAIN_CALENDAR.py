from FunctionsHaritz1 import *
from rock_paper_scisors import *


list_events = []

option=24
while option!=11:
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
    print("9-Exit")
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








