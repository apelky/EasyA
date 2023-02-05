"""
EasyA.py created on Fri Jan 13, 2023.

Group 1:
Ethan Aasheim
Melodie Collins
Linnea Gilius
Timothy Nadeau
Angela Pelky

This implements an system that is an update to the Emerald Grade Tracker (EGT).
The original EGT can be found here: 'https://emeraldmediagroup.github.io/grade-data'
The EGT displays the letter-grade distribuition across all professors in a particular department of the natural science at the University of Oregon.
This system builds upon the original EGT by directly comparing professors in the same department on the same graph, and is only concerned with the extreme ends of the letter-grade spectrum.

----------------------------------------

EasyA.py uses Python 3.10
"""

"""
Matplotlib is a visaul fucntion library for python: https://matplotlib.org/
"""
import matplotlib.pyplot as plt
import math
import sys
sys.path.insert(0, "Modules")

from Course_Class import *
from Graph_Class import *

from User_Input import *
from Faculty_Parser import *
from Fetch_Data import *
from Draw_Graph import *

# --- Set to False before submit
DEBUG = True

# Only prints if DEBUG == true
def debugPrint(*args):
    if DEBUG:
        print(*args)


# This function is called when the program starts and manages the other functions
def main():
    """
    Main funciton for Easy A Program.

    Prompt users for input, then spits out a graph based on user input

    Returns none
    """

    print("- EasyA Program -")
    print("Created by Group 1\n")

    subject, courseNum, levelParams, allInstructors, easyA, showCount = getInput()

    # Handle level parameters
    level = None
    viewByInstr = False
    if levelParams != None:
        level = levelParams[0]
        viewByInstr = levelParams[1]

    # List of all graphs
    graphs = []

    # Get all offers of specified course
    if courseNum is not None and courseNum != "":
        debugPrint("get_course")
        offerList = get_course(subject, courseNum)
        if len(offerList) > 0:
            graph = createGraph(offerList, 0, easyA, allInstructors, showCount)
            graphs.append(graph)
        else:
            print("Data not found for subject", subject, "and course number", courseNum)

    # Get all offers of all courses in same x00 level
    elif level is not None and level != "None":
        debugPrint("get_department_x00_level", viewByInstr)
        courseDict = get_department_x00_level(subject, level)
        courseList = list(courseDict.values())
        if len(courseList) > 0:
            for course in courseList:
                graph = createGraph(course, 3 - viewByInstr, easyA, allInstructors, showCount)
                graphs.append(graph)
        else:
            print("Data not found for subject", subject, "and x00 level", level)

    # Get all offers of all courses in the subject department
    else:
        debugPrint("get_department_courses")
        courseList = get_department_courses(subject)
        if len(courseList) > 0:
            for course in courseList:
                graph = createGraph(courseList[course], 1, easyA, allInstructors, showCount)
                graphs.append(graph)
        else:
            print("Data not found for subject", subject)

    print("ready to graph")

    # Plot and display graphs
    plot_graphs(graphs, subject, courseNum, level)

    return


# This calls the 'main' function when this script is executed
if __name__ == "__main__":
    main()
