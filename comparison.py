""" This file is part of the File I/O exercise.

It should be used with the two input files, fruits_1.txt and fruits_2.txt."""

def open_and_read_file(filename):
    """Opens file as a file object and returns list of contents."""

    # Write your code below.


    fruit_file = open(filename)
    fruit_data_list = fruit_file.read()
    fruit_file.close()
    fruit_data_list = fruit_data_list.strip()
    fruit_data_list = fruit_data_list.split("\n")
    return fruit_data_list


def compare(lst1, lst2):
    """Takes in two lists and returns a list of items in common. """

    # Write your code below.

    empty_list = []

    for fruit in lst1:
        if fruit in lst2:
            empty_list.append(fruit)

    print empty_list


# Call your functions at the bottom, after they've been defined.
lst1 = open_and_read_file("fruits_1.txt")
lst2 = open_and_read_file("fruits_2.txt")
compare(lst1, lst2)
