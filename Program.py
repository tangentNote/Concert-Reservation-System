"""
Program ID: Concert Reservation System
Purpose: exercise programming concept  from building around concert reservation system.

    "When the program starts, it will load a file containing a previously saved concert hall layout.
    You will demonstrate your ability to create a looping menu system,
    display and manipulate data using a 2D list, perform file input and output operations,
    and handle exceptions appropriately."

Revision History:
    Created Nov 5 2025

"""
from functions import *
menu="menu.txt"

#------------------------------------------------------------------------------------------------------------------#
## Programs start here

try:
    selected_file = str(input("Enter file name to load: "))  # user must enter existing data file name
    contain_list = load_file(selected_file)  # save store of data lists
except Exception as e: # catch any missed exception in general
    print(f"Error: {e}")
else:
    print()
    print("File loaded successfully. ")
    print()
    print()
display_chart(contain_list) # 2d table list
print()
display_file(menu) # menu info
print()

while True: # Run program when file exist until exiting
    try:
        select_from_menu= int(input( "Select an options(1-6): "))
        if select_from_menu == 1: # add seat to empty seat
            print()
            display_chart(contain_list)  # 2d table list
            print()
            contain_list=new_reservation(contain_list)
            print()
            display_chart(contain_list) # 2d table list
            print()
            display_file(menu) # menu info
            print()
        elif select_from_menu == 2: # edit existing seat
            print()
            display_chart(contain_list)  # 2d table list
            print()
            contain_list = edit_reservation(contain_list)
            print()
            display_chart(contain_list)
            print()
            display_file(menu)
            print()
        elif select_from_menu == 3: # make the list empty with ascending order
            print()
            display_chart(contain_list)
            print()
            contain_list = cancel_reservation(contain_list)
            print()
            display_chart(contain_list)
            print()
            display_file(menu)
            print()
        elif select_from_menu == 4: # display the lastest list
            print()
            display_chart(contain_list)
            print()
            print(display_file(menu))
            print()
        elif select_from_menu == 5: # save the new list as given name by user
            save_to_file=str(input("Enter filename to save (existing file will be overwritten): "))
            save_file(save_to_file, contain_list)
            print()
            print(display_file(menu))
            print()
        elif select_from_menu == 6: # exiting program with massage
            print()
            print("Thank you for using concert seat booking system")
            print()
            print("Goodbye")
            exit()
        else: # the integer is out of range
            raise IndexError("Invalid option, try again.")
    except ValueError as v: # a string is not of an options
        print(f"Error: Input must be an integer - {v}")
    except IndexError as i: # not in range
        print(f"Error: Out of range - {i}")
    except Exception as e: # catch any missed exception in general1
        print(f"Error: {e}")











