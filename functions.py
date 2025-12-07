
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

def create_data_set(row, coln): # creates empty data set of any size, always save as in data_set.txt
    file = open("data_set.txt", "w")
    file.write(f"{row}\n{coln}\n")
    for i in tqdm(range(row), desc= "Writing data set"):
        for j in range(coln):
            file.write(f"{j+1}\n")

import time
from tqdm import tqdm

if __name__ == '__main__':
    create_data_set(2**12, 2**10)
    display_chart(load_file("data_set.txt"))
    print(f"\n the data set has been created successfully. timer: {elapsed_time:.4f}s ")

