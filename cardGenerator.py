#!/usr/bin/env python

# Hello World in GIMP Python

from gimpfu import *
import copy

def create_cards() :
    list1 = [" red: ", " blue: ", " green: ", " yellow: " ]
    font = "Arial"
    size = 48
    realcolor = (0,0,0)
    '''for color in list1:
        string1 = color
        for i in range(3):
            pdb.python_fu_hello_world(string1 + str(i + 1), font, size, realcolor)
            list2 = copy.deepcopy(list1)
            try:
                list2.remove(color)
            except Exception as e:
                list2 = list
        try:
                for color2 in list2:
                    for j in range(3):
                        pdb.python_fu_hello_world(string1 + str(i + 1) + " " + color2 + str(j + 1), font, size, realcolor)
                    
        except Exception as e:
            list2 = list2
    
    for color in list1:
        string1 = color
        for i in range(3):
            for color2 in list1:
                string2 = color2
                if string1 != string2:
                    for j in range(3):
                        ##added new line character for spacing reasons
                        pdb.python_fu_hello_world(string1 + str(i + 1) + "\n" + color2 + str(j + 1), font, size, realcolor)'''

    ##I simplified everything into one horrible loop hope this helps
    for color in list1:
        string1 = color
        for i in range(3):
            ##all of the single cards generated here
            pdb.python_fu_hello_world(string1 + str(i + 1), font, size, realcolor)
            for color2 in list1:
                string2 = color2
                if string1 != string2:
                    for j in range(i + 1):
                        ##all of the 2 cards here (1,1) (2,1) (2,2) (3,1),(3,2)(3,3)
                        pdb.python_fu_hello_world(string1 + str(i + 1) + "\n" + color2 + str(j + 1), font, size, realcolor)
                        for color3 in list1:
                            string3 = color3
                            if string3!=string2 and string3 != string1:
                             ##all of the 3 cards here (1,1,1) (2,1,1) (2,2,2) (3,1,1),(3,2,2)(3,3,3)
                             ##follows design pattern from meeting without generating every possible combination (so no 1,2,3 or ,2,1,2)
                             ##there are a lot of duplicates but we knew that would be the case
                             pdb.python_fu_hello_world(string1 + str(i + 1) + "\n" + color2 + str(j + 1)+ "\n" + color3 + str(j + 1), font, size, realcolor)
                        



register(
    "python_fu_create_cards",
    "Create cards for the IE game",
    "Create cards",
    "David Williams and Maddie Mayans",
    "2023",
    "2023",
    "Create Cards (py)",
    "",      # Create a new image, don't work on an existing one
    [],
    [],
    create_cards, menu="<Image>/File/Create")

main()