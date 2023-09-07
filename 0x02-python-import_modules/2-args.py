#!/usr/bin/python3
import sys

def getArg():
    n_arg = len(argv)- 1
    end = "."
    if (n_arg > 0) : end = ":"

    print(f"{n_arg} arguments{end}")

    if(n_arg > 0):
        for i in range(n_arg):
            print(f"{i + 1}: {argv[i + 1]}")

if __name__ == "__main__" :
   argv = sys.argv
getArg()
