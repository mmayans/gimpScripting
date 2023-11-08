#!/usr/bin/env python

# Hello World in GIMP Python

from gimpfu import *
import copy

def create_cards() :
    list1 = [" red: ", " blue: ", " green: ", " yellow: " ]
    font = "Arial"
    size = 32
    realcolor = (0,0,0)
    for color in list1:
        string1 = color
        for i in range(3):
            pdb.python_fu_hello_world(string1 + str(i + 1), font, size, realcolor)
            '''list2 = copy.deepcopy(list1)
            try:
                list2.remove(color)
            except Exception as e:
                list2 = list
        try:
                for color2 in list2:
                    for j in range(3):
                        pdb.python_fu_hello_world(string1 + str(i + 1) + " " + color2 + str(j + 1), font, size, realcolor)
                    
        except Exception as e:
            list2 = list2'''
    
    for color in list1:
        string1 = color
        for i in range(3):
            for color2 in list1:
                string2 = color2
                if string1 != string2:
                    for j in range(3):
                        pdb.python_fu_hello_world(string1 + str(i + 1) + " " + color2 + str(j + 1), font, size, realcolor)



register(
    "python_fu_create_cards",
    "Create cards for the IE game",
    "Create cards",
    "David Williams and Maddie",
    "2023",
    "2023",
    "Create Cards (py)",
    "",      # Create a new image, don't work on an existing one
    [],
    [],
    create_cards, menu="<Image>/File/Create")

main()