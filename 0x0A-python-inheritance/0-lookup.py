#!/usr/bin/python3
def lookup(obj):
    """ THIS TO LOOK FOR THE ATTRIBUTE IN THE CLASS """
    lis = []
    for ls in dir (obj):
        lis.append(ls)
        
    return (lis);

