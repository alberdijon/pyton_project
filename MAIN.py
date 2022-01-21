from CALENDAR.FunctionsHaritz import *

list_events = []

option=24
while option!=10:
    print("THE CALENDAR MENU (Choose a task typing its number!)")
    print("==================================================")
    print("1--Print calendar")
    print("2--Add event")
    print("3--Remove events")
    print("4--Search if a day have events or not")
    print("5--Search event by name")
    print("6--Show events")
    print("7--Playu Rock,Paper,Scissors")
    print("8--Show how many events are added.")
    print("9-Dawing machine.")
    print("10--Exit")
    option= int(input("Enter an option from the menu"))
    if option==1:
        print_calendar()
    if option==2:
        addevents(list_events)
    if option == 9:
        drawingMachine()
    if option == 6:
        show_events(list_events)
    if option == 3:
        delete_events(list_events)







