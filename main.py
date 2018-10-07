import main_menu

def main():

    main_menu_choice = main_menu.main_menu()
    if main_menu_choice == 1:
        print("TESTING PURPOSE:   NEW GAME")
    elif main_menu_choice == 2:
        print("TESTING PURPOSE:   LOAD GAME")
    elif main_menu_choice == 3:
        print("Exiting...\nGood Bye!")

# Game starts
main()