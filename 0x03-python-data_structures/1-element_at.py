#!/usr/bin/python3
def element_at(my_list, idx):

    length = len(my_list) - 1

    if (length < idx or 0 > my_list[idx]):
        return("None")
    else:
        return(my_list[idx])
