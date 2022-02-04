option=24
while option != 5:
    print("EXERCISES MENU")
    print("=========================")
    print("CHOOSE AN EXERCISE: ")
    print("=========================")
    print(
        "1.- Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included). ")
    print("2.- Python program to count the number of even and odd numbers from a series of numbers. ")
    print("3.- Python program to create the multiplication table (from 1 to 10) of a number.")
    print("4.- Python program to construct the number triangle pattern")
    print("5.- Exit program.")
    print("Enter the number of the exercise: ")

    option = int(input("Please, enter the number depending of the drawing you want to draw."))

    if option == 1:
        ex1()
    if option == 2:
        ex4()
    if option == 3:
        ex10()
    if option == 4:
        ex11()
