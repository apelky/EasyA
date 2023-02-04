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

User input:
    Enter <year>    only has data from 2013 to 2016
    Enter <subject code>
    Enter <course number>

EasyA.py uses Python 3.10
"""

"""
Matplotlib is a visaul fucntion library for python: https://matplotlib.org/
"""
import matplotlib.pyplot as plt

"""
argparse is a module from the Python Standard Library which parses command line options
sys is a module from the Python Standard Library which handles system - specific parameters and functions
"""
import argparse
import sys

from Course_Class import *
from Graph_Class import *
from Faculty_Parser import *
from functions import *
from User_Input import *

"""
This variable is for the file containing all of the grade data from the EGT.
It's a global varialbe so that there is less overhead when reading data into this program.
The data file is read on user request only because the data file is very large and only a small portion is needed at any given time.

Commented out for now since I don't know if files can be global variables
"""
#f = None

dataFile = "GradeData.txt" # "GradeData_SmallTest.txt"


# List of all subject code, but there are just so many that I think checking probably is not would be worthy it right now
subjectCodes = ["AA", "AAA", "AAAP", "AAD", "ACTG", "AEIS", "AFR", "AIM", "ANTH", "ARB", "ARCH", "ARH", "ART", "ARTC", "ARTD",
                "ARTF", "ARTM", "ARTO", "ARTP", "ARTR", "ARTS", "ASIA", "ASL", "ASTR", "BA", "BE", "BI", "CAS", "CDS", "CFT", "CH",
                "CHN", "CINE", "CIS", "CIT", "CLAS", 'COLT', "CPSY", "CRES", "CRWR", 'DAN', "DANC", "DSC", "EALL", "EC", "EDLD", "EDST",
                ]



# List of all subject code, but there are just so many that I think checking probably is not would be worthy it right now
subjectCodes = ["AA", "AAA", "AAAP", "AAD", "ACTG", "AEIS", "AFR", "AIM", "ANTH", "ARB", "ARCH", "ARH", "ART", "ARTC", "ARTD",
                "ARTF", "ARTM", "ARTO", "ARTP", "ARTR", "ARTS", "ASIA", "ASL", "ASTR", "BA", "BE", "BI", "CAS", "CDS", "CFT", "CH",
                "CHN", "CINE", "CIS", "CIT", "CLAS", 'COLT', "CPSY", "CRES", "CRWR", 'DAN', "DANC", "DSC", "EALL", "EC", "EDLD", "EDST",
                ]


# --- Set to False before submit
DEBUG = True


# Only prints if DEBUG == true
def debugPrint(*args):
    if DEBUG:
        print(*args)


# Gets input parameters from user via a command line interface
# Returns 'subject' (string), 'courseLvl' (int or None), 'level' (int or None), and 'year' (int or None)
def getInput(): #def updateData():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', help='a json file containing grade data')
    args = parser.parse_args()
    file = args.f

    if not file.lower().endswith('.json'):
        print("ERROR: file must be a JSON file (.json)")
        return

    try:
        fstream = open(file)
    except:
        print("ERROR: cannot open file", file)
    else:
        for line in fstream:
            continue

        print("system updated with new data")

###
    # Optional arguments
    parser.add_argument('-s', help='A single subject code, such as "Math"')
    parser.add_argument('-c', type=int, help='A single course level, such as "111"')
    parser.add_argument('-l', type=int, help='All courses of a particular level, such as "100"')
    parser.add_argument('-y', type=int, help='A year from 2013 to 2016')
    parser.add_argument('-g', type=int, help='Whether to show the graph')

    # Parameter variables
    args        = parser.parse_args()
    subject     = args.s
    courseLvl   = args.c
    level       = args.l
    year        = args.y
    showGraph   = args.g == None or (args.g != 0 and args.g != False)

    # Make sure that a subject code is provided if it wasn't a command line argument
    if args.s is None:
        subject = input("Enter subject code: ")

    # Make sure that a course number is provided if it wasn't a command line argument
    if args.c is None:
        view_course = input("Do you want view a specific course? [y or n]: ")
        if view_course:
            courseLvl = int(input("Enter course number: "))
        else:
            view_level = None
            if (args.l is None):
                view_level = input("Do you want view all courses of a specific level? [y or n]: ")
            else:
                view_level = input("Do you want view all courses of level", level + "? [y or n]: ")
            if view_level:
                level = int(input("Enter course level: "))

    # Make sure that a year provided if it wasn't a command line argument
    if args.y is None:
        view_year = input("Do you want view a specific year? [y or n]: ")
        if view_year:
            year = int(input("Enter a year from 2013 to 2016: "))
###

def getInput():
###
    """
    debugPrint("Optional subject code argument: ", subject)
    debugPrint("Optional course argument: ", courseLvl)
    debugPrint("Optional level argument: ", level)
    debugPrint("Optional year argument: ", year)
    debugPrint("Optional graph argument: ", showGraph)
    """

    return subject, courseLvl, level, year, showGraph
###

# Gets the value from the key/value pairs of the data file
def parseDataValue(str):

    # Error checking
    if str.find(": \"") == -1:
        return None

    # Get part of string after ': "'
    start = str.index(": \"") + 3
    if str[-2] == ',':
        end = len(str) - 3
    else:
        end = len(str) - 2
    return str[start:end]


# Determine if an instructor is a permanent faculty hire at UofO
def checkIfRegularFaculty(instructor):
    """
    Compares list of Regular Faculty to list of data of all
    instuctors

    Parameters:
        instructor (str) - Name of instructor/professor - Ex: "Hornof, Anthony"

    Returns:
        isRegularFaculty (bool) - Whether a given name is Regular Faculty
    """

    # Get list of Regular Faculty
    regularFaculty = parseFacultyNames()

    # If the instructor is faculty
    isRegularFaculty = False

    # Search list of Regular Faculty for given name
    #debugPrint("Given name: ", instructor)
    for name in regularFaculty:
        if instructor == name:
            '''TODO: this doesn't address the issue of middle inital'''
            #debugPrint(instructor, " is regular faculty")
            isRegularFaculty = True

    return isRegularFaculty


# Count the number of courses an instructor has taught
def countInstructorCourses(instructor):
    """
    Counts the number of courses an instructor/professor
    teaches in a singular subject

    Parameters:
        instructor (Str) - Name of instructor - Ex: "Hornof, Anthony"

    Returns:
        numCourses (int) - # of courses instructor teaches
    """

    # Open dataset file
    f = open(dataFile, "r")

    read = True
    numCourses = 0

    # Search file for instructor
    while read == True:
        line = f.readline()

        # End of data check
        if line.find("};") != -1:
            read = False

        # Number of courses instructor has taught
        if line.find(instructor) != -1:
            numCourses += 1

    # Close dataset file
    f.close()
    return numCourses


# Gets data from data file based on string parameters 'year', 'subject', and 'course'
def getData(subject, courseLvl, year):
    """
    Looks in global 'datafile' = "GradeData.txt", for data
    given a course, subject, and year. Returns a dictionary of that specfic class
    found.

    CURRENTLY ONLY RETURNS INFORMATION ON ONE OFFERING OF A COURSE
        (if multiple classes found w/ same year, subject, and course #, only 1 will be returned)

    Parameters:
        year (str) - Year course was offered - Ex: "2015"
        subject (str) - Department it's in - Ex: "MTH"
        course (str) - Level of course - Ex: "111"

    Returns list of Course objects
    """
    print("Subject Code:", subject, "   Course Number:", courseLvl, "   Year:", year)

    # Open dataset file
    f = open(dataFile, "r")

    # The key of the data we need is the subject code followed by the course number
    key = subject + courseLvl

    read        = True  # Whether to keep reading file --- is set to False when target data found or at end of data
    layer       = 0     # Current depth in dataset --- 0 = all data, 1 = specific course, 2 = all course terms, 3 = specific term
    line        = ""    # Store contents of readline() here
    foundKey    = False # Whether the subject and course have been found yet
    foundYear   = False # Whether the year has been found yet
    dataList    = []    # All of the course data that was found and is returned
    resultData  = None  # A single course that matchs the request
    count       = 0     # Number of terms a course was offered in the specified year

    # First line of file is just an initialization we should get out of the way
    f.readline()

    # Read data in from file
    while read == True:
        line = f.readline()

        # End of data check
        if line.find("};") != -1:
            read = False

        # - Traverse dataset -

        # Go down a layer in the dataset
        if line.find("{") != -1:
            layer += 1

        # Go up a layer in the dataset
        if line.find("}") != -1:
            layer -= 1

        # Go down a layer in the dataset, into a course
        if line.find("[") != -1:
            # Check line from data file for subject code and course number
            if line.find(key) != -1:
                foundKey = True
                #debugPrint("Found course", subject, course)
            layer += 1

        # Go up a layer in the dataset, exiting a course
        if line.find("]") != -1:
            # If finished searching requested subject and course
            if foundKey == True:
                # If found year
                #if foundYear == True:
                    #debugPrint("Found course", subject, courseLvl, "in", year, count, "time(s)")
                # If could not find year
                if not foundYear:
                    debugPrint("Course", subject, courseLvl, "not found for", year, count, "time(s)")
                read = False
            layer -= 1

        # - Layer specific steps -

        # Layer == 0 --- End of data file and request not found
        if layer == 0:
            debugPrint("End of dataset - course", subject, courseLvl, "not found")
            read = False

        # Layer == 1 --- Searching for subject and course
        if layer == 1:
            continue

        # Layer == 2 --- Within requested subject and course, searching for year
        #if layer == 2:

        # Layer == 3 --- Within a specific term that may or may not be the requested year
        if layer == 3:
            if foundKey == False:
                continue

            # Check if this is the requested year
            line = f.readline()
            term = parseDataValue(line)
            if term == None:
                continue
            if term.find(year) != -1:
                foundYear = True

                # For all of the years requested course was offered
                while line.find(year) != -1:

                    # Load the rest of the data in
                    termDesc = parseDataValue(line);        line = f.readline()
                    aprec = float(parseDataValue(line));    line = f.readline()
                    bprec = float(parseDataValue(line));    line = f.readline()
                    cprec = float(parseDataValue(line));    line = f.readline()
                    crn   = parseDataValue(line);           line = f.readline()
                    dprec = float(parseDataValue(line));    line = f.readline()
                    fprec = float(parseDataValue(line));    line = f.readline()
                    instructor = parseDataValue(line)
                    isProfessor = checkIfRegularFaculty(instructor)
                    numCourses = countInstructorCourses(instructor)

                    course = Course(subject, courseLvl, crn, termDesc, aprec, bprec, cprec,
                                        dprec, fprec, instructor, isProfessor, numCourses)

                    # Add data to list and increase count of courses found
                    dataList.append(course);
                    count += 1

                    # Skip to next course description
                    line = f.readline(); line = f.readline(); line = f.readline()
                read = False

    # Close dataset file
    f.close()

    debugPrint("Course", subject, courseLvl, "was offered", count, "times in", year, "\n")
    return dataList


# Draws a graph from the usser requested data with matplotlib functions
def drawGraph(course, EasyA=True, showGraph=False):
    """
    Draw a graph given a list of course offers
    using matplotlib functions

    Parameters: A list
        course    = list of Course objects
        EasyA     = bool
        showGraph = bool

    Return:
        None
    """

    # Get all instructors and check for duplicates
    instructor_grades = {}
    instructor_count  = {}

    # Go through all offers of the course
    for offer in course:
        if offer.instructor not in instructor_grades:
            instructor_grades[offer.instructor] = 0
            instructor_count[offer.instructor] = 0

        # Increment grade percentage
        instructor_grades[offer.instructor] += offer.a_perc if EasyA else offer.df_perc
        instructor_count[offer.instructor] += 1

    # Second pass of instructors for average grade percentage
    for name in instructor_grades.keys():
        instructor_grades[name] /= instructor_count[name]

    # Get list of instructor names
    names = []
    grades = []
    min_thresh = 2
    for name in instructor_grades.keys():
        if instructor_count[name] > min_thresh:
            names.append(name)
            grades.append(instructor_grades[name])

    print(instructor_grades)
    print(instructor_count)

    graph = Graph(0, EasyA, True, True)
    graph.data = courseList
    graph.plotting_data = grades

    default_offer = courseList[0][0]
    graph.title = default_offer.dept + " " + default_offer.level + " " + default_offer.term_desc

    graph.x_axis_label = "Instructors"
    graph.y_axis_label = "%"


    """
    # Graph title
    default_offer = courseList[0][0]
    plt.title(default_offer.dept + " " + default_offer.level + " " + default_offer.term_desc)

    # Plot graph
    plt.bar(range(len(names)), grades, tick_label=names)
    plt.tick_params(axis ='x', rotation = -90)

    # Axis labels
    plt.xlabel("Instructors")
    plt.ylabel("%")

    # Save graph as .pdf file
    plt.savefig("EasyA_result.pdf")

    # Show graph
    if showGraph:
        plt.show()
    """


# This function is called when the program starts and manages the other functions
def main():
    """
    Main funciton for Easy A Program.

    Prompt users for input, then spits out a graph based on user input

    Returns none
    """

    print("- EasyA Program -")
    print("Created by Group 1\n")

    dept, courseLvl, level, year, showGraph = getInput()

    # Get data from data file based on input parameters
    #dataList = getData(subject, courseLvl, year)

    # Get course based on input
    courseDict = get_department_x00_level(dept, courseLvl)

    EasyA = True

    # If requested data was found
    if courseDict != None:
        courseList = list(courseDict.values())
        if len(courseList) > 0:
            debugPrint("********\n")
            #for i in range(len(courseList)):
                #debugPrint("- Course", i+1, "of", len(courseList), "-")
                #debugPrint(courseList[i])

            # Generate graph
            for course in courseList:
                for offer in course:
                    debugPrint(offer)
                    """
                    if offer.instructor not in instructor_grades:
                        instructor_grades[offer.instructor] = offer.a_perc
                        instructor_count[offer.instructor] = 1
                    else:
                        instructor_grades[offer.instructor] += offer.a_perc
                        instructor_count[offer.instructor] += 1
                    """
            #   drawGraph(course, EasyA, showGraph)
            debugPrint("********\n")

    # The requested data was not found
    else:
        debugPrint("- Data not found -")
    return


# This calls the 'main' function when this script is executed
if __name__ == "__main__":
    main()
