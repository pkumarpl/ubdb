#!/usr/bin/env python
# -*- coding=utf-8 -*-

"""
tab_file
NAME     
        tab_file - avg multipoles value in csv file as vector
SYNTAX
        tab_file [FILE]
"""
import sys
import os
import itertools

def usage(code):
    """ tab_file usage """
    print(__doc__)
    exit(code)


def tab_file(args):
    # ----------------------------------------------------------
    #  options
    # ----------------------------------------------------------
    narg = len(args)
    if narg == 2:
        if args[1] == "-h" or args[1] == "--help":
            usage(0)
        else:
            if not os.path.exists(args[1]):
                print("Error : file {0} does not exist".format(args[1]))
                exit(1)
            else:
                outfilename = args[1].strip()
                outfile = open(outfilename, "r")
    else:
        print(args)
        print("Error : bad arguments")
        usage(1)
# ----------------------------------------------------------
# read general data
    mean = []
    esd = []
    line = outfile.readline()
    end = True
    while line != "":
        line = outfile.readline()
        if "MEAN" in line:
            mn = line.split() # Split the line based on space
            mn.remove("MEAN") # Removing charecter string from list
            mean.append(mn)


        elif "ESD" in line:
            ed = line.split() # Split the line based on space
            ed.remove("ESD") # Removing charecter string from list
            esd.append(ed)

        elif "Averaged pseudoatom parameters in databank format:" in line:
            end = False
            break
    if end:
        print("Check if averaging is done properly")

    merged_mn = list(itertools.chain(*mean)) # Merging list of lists
    merged_ed = list(itertools.chain(*esd)) # Merging list of lists
    print(outfilename[:4], end=" ") #Print four CHAR of inputfile name
    for a, b in zip(merged_mn, merged_ed):
        print(float(a), float(b), end=" ")
    print("\n")
if __name__ == "__main__":
    tab_file(sys.argv)