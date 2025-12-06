"""
Mung Khual & Sara Negash
Program ID: Assignment 1- Concert Reservation System
Purpose: exercise programming concept  from building around concert reservation system.

    "When the program starts, it will load a file containing a previously saved concert hall layout.
    You will demonstrate your ability to create a looping menu system,
    display and manipulate data using a 2D list, perform file input and output operations,
    and handle exceptions appropriately." Stacey

Revision History:
    Created by Mung Khual Nov 5 2025
    Starting loop program by Mung Khual Nov 10 2025
    Load file function by Sara Negash Nov 11 2025
    Display chart function by Sara Negash Nov 11 2025
    Save file function by Sara Negash Nov 11 2025
    Display file function by Mung Khual Nov 11 2025
    Edits and debugging by Mung Khual Nov 11 2025
    New Reservation Function by Mung Khual Nov 17 2025
    Edit reservation function by Mung Khual Nov 17 2025
    Cancel reservation function by Mung Khual Nov 17 2025
    Add code and debugging by Mung Khual Nov 19 2025
    Add code and debugging by Mung Khual Nov 24 2025
    Add code and debugging by Mung Khual Nov 25 2025
    Add code and debugging by Mung Khual Nov 27 2025
    Test Program by Sara Negash Nov 27 2025
    Test Program by Mung Khual Nov 27 2025
    Add code and debugging by Mung Khual Nov 29 2025

"""


def display_file(file): # this will display any file as plain text
    try:
        file = open(file, "r")
        for line in file:
            print(line, end="")
    except FileNotFoundError as f:
        print(f"Error: File not found - {f}")
    except Exception as e: # catch any missed exception in general
        print(f"Error: {e}")

def load_file(filename): # turning a data into 2d list(aka lists of list)
    concert_hall = []
    try:
        with open(filename, 'r') as file:
            n_rows = int(file.readline().strip())
            n_cols = int(file.readline().strip())
            for _ in range(n_rows):
                row = []
                for _ in range(n_cols):
                    seat = file.readline().strip()
                    row.append(seat)
                concert_hall.append(row)
            return concert_hall
    except FileNotFoundError:
        print(f"Error in loading, exiting.")
        exit()
    except ValueError:
        print(f"Error: Invalid file format")
        exit()
    except TypeError:
        print(f"Error: parameter was not given")
    except Exception as e: # catch any missed exception in general
        print(f"Error: {e}")

def display_chart(concert_hall): # display lists as seating chart (2d table)
    try:
        for i, rows in enumerate(concert_hall, start=1):
            row_str = '\t'.join(rows)
            print(f"Rows: {i}:\t{row_str}", end="")
            print()
    except TypeError:
        print(f"Error: parameter was not given")
    except Exception as e: # catch any missed exception in general
        print(f"Error: {e}")

def save_file(filename, concert_hall):  # save the selected data into a given file name
    try:
        with open(filename, 'w') as file:
            file.write(str(len(concert_hall)) + '\n')
            file.write(str(len(concert_hall[0])) + '\n')
            for row in concert_hall:
                for seat in row:
                    file.write(seat + '\n')
        print()
        print("File saved successfully")
        print()
    except FileNotFoundError as f:
        print("Error in saving file:", f)
        print()
    except TypeError:
        print(f"Error: parameter was not given")
    except Exception as e:  # catch any missed exception in general
        print(f"Error: {e}")
        print()
def input_row_coln(list):   # repeating input of row&column in 1-3 menu options
    row_len = len(list) + 1
    coln_len = 0
    for inner in list:
        coln_len = len(inner) + 1
    while True:
        try:
            row = int(input("Enter desire row : "))
            if row >= row_len:  # Validate range
                raise IndexError("Invalid row, try again.")
            if row <= 0:  # Validate integer
                raise IndexError("Invalid value, input must be positive integer.")
            else:
                break
        except IndexError as i:
            print(f"Error: Out of range - {i}")
        except ValueError as v:
            print(f"Error: It must be an integer - {v}")
        except Exception as e:  # catch any missed exception in general
            print(f"Error: {e}")
    while True:
        try:
            coln = int(input("Enter desire column : "))
            if coln >= coln_len:  # Validate integer
                raise IndexError("Invalid column, try again.")
            if coln <= 0:  # Validate integer
                raise Exception("Invalid value, input must be positive integer.")
            else:
                break
        except IndexError as i:
            print(f"Error: Out of range - {i}")
        except ValueError as v:
            print(f"Error: It must be an integer - {v}")
        except Exception as e:  # catch any missed exception in general
            print(f"Error: {e}")
    return row, coln

def new_reservation(list):  # add seat into empty place and can't change existing seat
    while True:
        try:
            filename = list
            row, coln = input_row_coln(list)
            if filename[row - 1][coln - 1].isalpha():
                print("Seat is already taken, choose another seat")
                break
            while True:
                seat = input("Enter your name: ")
                if seat == "":
                    print("Name cannot be empty. ")
                else:
                    filename[row - 1][coln - 1] = seat
                    exit_both_loop = True
                    break
            print()
            print("Seat reserved successfully.")
            print()
            if exit_both_loop == True:
                break
        except IndexError as i:
            print(f"Error: Out of range - {i}")
        except ValueError as v:
            print(f"Error: It must be an integer - {v}")
        except Exception as e:  # catch any missed exception in general
            print(f"Error: {e}")
    return list

def edit_reservation(list): # edit the existing seat and can't change empty seat
    exit_both_loop = False
    while True:
        try:
            filename = list
            row, coln = input_row_coln(list)
            if filename[row - 1][coln - 1].isdigit():
                raise Exception("Seat is empty")
            while True:
                seat = input("Enter your a new name: ")
                if seat == "":
                    print("Name cannot be empty. ")
                else:
                    filename[row - 1][coln - 1] = seat
                    exit_both_loop = True
                    break
            print()
            print("Seat reserved successfully.")
            print()
            if exit_both_loop == True:
                break
        except ValueError as v:
            print(f"Error: It must be an integer - {v}")
        except IndexError as i:
            print(f"Error: Out of range - {i}")
        except Exception as e:  # catch any missed exception in general
            print(f"Error: {e}")
    return list

def cancel_reservation(list): # make a seat empty with appropriate number
    exit_both_loop = False
    while True:
        filename = list
        row, coln = input_row_coln(list)
        if exit_both_loop == True:
            break
        try:
            if filename[row - 1][coln - 1].isdigit():
                raise Exception("Seat is empty")
            else:
                print(f"Seat reserved for: {filename[row - 1][coln - 1]}")
                decide_case=str(input("Confirm reserve cancellation. (y/n): "))
            while True:
                if exit_both_loop == True:
                    break
                match decide_case:
                    case "y":
                        filename[row - 1][coln - 1] = str(coln)
                        print("Seat cancelled successfully.")
                        exit_both_loop = True
                        return filename
                    case "n":
                        print("Seat is not cancelled.")
                        exit_both_loop = True
                        return filename
                    case _:
                        print("You have not decided")
                        return filename
        except ValueError as e:
            print(f"Error: It must be an integer - {e}")
        except IndexError as i:
            print(f"Error: Out of range - {i}")
        except Exception as e:  # catch any missed exception in general
            print(f"Error: {e}")
            print()
    return list
#------------------------------------------------------------------------------------------------------------------#
## Programs start here
menu="menu.txt"
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











