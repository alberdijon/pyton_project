def rock_paper_scisors():
    def winning(play_again):
        print("Congratulations you won!!!  :)")
        play_again = int(input(" Do you want to play again 1 for yes 2 for no"))
    def loosing (play_again):
        print("Bad luck you losed :(")
        play_again = int(input(" Do you want to play again 1 for yes 2 for no"))
    def main_game(play_again, players_choice):
        while play_again != 2:
            print("1 for Rock \n"
                "2 for paper \n"
                "3 for scisors")
            players_choice = int(input("Wich one you choice"))
            bots_choice = random.randrange(1,4)
            print(f"Your choice is {players_choice} and the bot's choice is {bots_choice}")

            if bots_choice == players_choice:
                print("It has been draw  :|")
                play_again = int(input(" Do you want to play again 1 for yes 2 for no"))
            elif bots_choice == 1 and players_choice == 2:
                print("Congratulations you won!!!  :)")
                play_again = int(input(" Do you want to play again 1 for yes 2 for no"))
            elif bots_choice == 1 and players_choice == 3:
                 print("Bad luck you losed :(")
                 play_again = int(input(" Do you want to play again 1 for yes 2 for no"))
            elif bots_choice == 2 and players_choice == 1:
                print("Bad luck you losed :(")
                play_again = int(input(" Do you want to play again 1 for yes 2 for no"))
            elif bots_choice == 2 and players_choice == 3:
                print("Congratulations you won!!!  :)")
                play_again = int(input(" Do you want to play again 1 for yes 2 for no"))
            elif bots_choice == 3 and players_choice == 1:
                print("Congratulations you won!!!  :)")
                play_again = int(input(" Do you want to play again 1 for yes 2 for no"))
            else:
                print("Bad luck you losed :(")
                play_again = int(input(" Do you want to play again 1 for yes 2 for no"))

    import random
    opttion_rps = 0

    while opttion_rps != 3:
        print ("Menu")
        print("1-Play")
        print("2-Rules")
        print("3-Exit")
        opttion_rps = int(input("What do you want to do?"))
        if opttion_rps == 1:
            play_again = 0
            players_choice = 0
            main_game(play_again,players_choice)
        elif opttion_rps == 2:
            print("These arae the rules of the game:\n"
                  "1-Rocks win scisors\n"
                  "2-Scisors wins paper\n"
                  "3-Paper wins rocks\n"
                  "4-You will play against the computer\n"
                  "5-Computer will select his option randomly\n"
                  "6-You will decide what do you select\n"
                  "7-Once you decide the result will be shown on the screen \n"
                  "8-When the game ends you will decide to play again or finish")

rock_paper_scisors()

#aa