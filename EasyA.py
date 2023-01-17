"""
EasyA.py created by Ethan Aasheim on Fri Jan 13, 2023.

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
"""
import argparse


"""
This variable is for the file containing all of the grade data from the EGT.
It's a global varialbe so that there is less overhead when reading data into this program.
The data file is read on user request only because the data file is very large and only a small portion is needed at any given time.

Commented out for now since I don't know if files can be global variables
"""
#f = None

dataFile = "GradeData_SmallTest.txt" # "GradeData.txt"


# started making list of all subject code, but there are just so many that I think checking probably is not would be worthy it right now
"""subjectCodes = ["AA", "AAA", "AAAP", "AAD", "ACTG", "AEIS", "AFR", "AIM", "ANTH", "ARB", "ARCH", "ARH", "ART", "ARTC", "ARTD",
                "ARTF", "ARTM", "ARTO", "ARTP", "ARTR", "ARTS", "ASIA", "ASL", "ASTR", "BA", "BE", "BI", "CAS", "CDS", "CFT", "CH",
                "CHN", "CINE", "CIS", "CIT", "CLAS", 'COLT', "CPSY", "CRES", "CRWR", 'DAN', "DANC", "DSC", "EALL", "EC", "EDLD", "EDST",
                ]
"""


#  --- Set to False before submit
DEBUG = True

# Only prints if DEBUG == true
def debugPrint(*args):
    if DEBUG:
        print(*args)


# Template function if we need it for something later
def helperFunction():
    print("helperFunction() unfinished")


# Gets input parameters from user via a command line interface
# Returns strings 'year', 'subject', and 'course'
def getInput():
    print("getInput() unfinished")
    return year, subject, course


# Gets the value from the key/value pairs of the data file
def parseDataValue(str):
    print("[" + str + "]")
    start = str.index(": \"") + 3
    if str[-2] == ',':
        end = len(str) - 3
    else:
        end = len(str) - 2
    return str[start:end]


def countInstructorClasses(instructor):
    """
    Counts the number of classes an instructor/professor
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

        if line.find(instructor) != -1:
            numCourses += 1

    # Close dataset file
    f.close()
    return numCourses


# Gets data from data file based on string parameters 'year', 'subject', and 'course'
def getData(year, subject, course):
    """
    Looks in global 'datafile' = "GradeData.txt", for data
    given a course, subject, and year. Returns a dictionary of that specfic class
    found. 

    CURRENTLY ONLY RETURNS INFORMATION ON ONE CLASS 
        (if multiple classes found w/ same year, subject, and course #, only 1 will be returned)

    Parameters:
        year (str) - Year class was offered - Ex: "2015"
        subject (str) - Department it's in - Ex: "MTH"
        course (str) - Level of course - Ex: "111"

    Returns a dictionary:
        resultData = {
                    "TERM_DESC": term,
                    "aprec": "",
                    "bprec": "",
                    "cprec": "",
                    "crn": "",
                    "dprec": "",
                    "fprec": "",
                    "instructor": ""
                    "isProfessor": ""
                }
    """
    print("Year:", year, "   Subject Code", subject, "   Course Number", course)

    # Open dataset file
    f = open(dataFile, "r")

    # The key of the data we need is the subject code followed by the course number
    key = subject + course

    read = True         # Whether to keep reading file --- is set to False when target data found or at end of data
    layer = 0           # Current depth in dataset --- 0 = all data, 1 = specific course, 2 = all course terms, 3 = specific term
    line = ""           # Store contents of readline() here
    foundKey = False    # Whether the subject and course have been found yet
    foundYear = False   # Whether the year has been found yet
    resultData = None   # The data that was found and is returned
    count = 0           # Number of terms a course was offered in the specified year --- I'm checking because I don't know if it's ever > 1

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
                debugPrint("Found subject", subject, "and course", course)
            layer += 1

        # Go up a layer in the dataset, exiting a course
        if line.find("]") != -1:
            # If finished searching requested subject and course
            if foundKey == True:
                # If found year
                if foundYear == True:
                    debugPrint("Found year", year, "for subject code", subject, "and course number", course)
                # If could not find year
                else:
                    debugPrint("Year", year, "not found for subject code", subject, "and course number", course)
                read = False
            layer -= 1

        # - Layer specific steps -

        # Layer == 0 --- End of data file and request not found
        if layer == 0:
            debugPrint("End of dataset - subject code", subject, "and course number", course, "not found")
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

            line = f.readline()
            term = parseDataValue(line)
            if term.find(year) != -1:
                foundYear = True

                # Create data dictionary to return
                resultData = {
                    "TERM_DESC": term,
                    "aprec": "",
                    "bprec": "",
                    "cprec": "",
                    "crn": "",
                    "dprec": "",
                    "fprec": "",
                    "instructor": "",
                    "isProfessor": "",
                    "numCourses": ""
                }

                # Load the rest of the data in
                line = f.readline()
                resultData["aprec"] = parseDataValue(line); line = f.readline()
                resultData["bprec"] = parseDataValue(line); line = f.readline()
                resultData["cprec"] = parseDataValue(line); line = f.readline()
                resultData["crn"]   = parseDataValue(line); line = f.readline()
                resultData["dprec"] = parseDataValue(line); line = f.readline()
                resultData["fprec"] = parseDataValue(line); line = f.readline()
                resultData["instructor"] = parseDataValue(line)
                resultData["numCourses"] = countInstructorClasses(resultData["instructor"])

                # This is a check to see if the courses was offered more than one term per year,
                # because I don't know if there are any that were
                count += 1
                read = False

    # Close dataset file
    f.close()

    debugPrint("Course", course, "was offered", count, "times in", year, "\n")
    return resultData



# Draws a graph from the usser requested data with matplotlib functions
def drawGraph(data):
    print("drawGraph() unfinished")
    print("Current graph style will likely be changed in the future")

    # Graph title
    plt.title(data["instructor"] + "    " + data["TERM_DESC"])

    # Set and plot points of graph
    x = [1, 2, 3, 4, 5]
    y = [data["aprec"], data["bprec"], data["cprec"], data["dprec"], data["fprec"]]
    plt.plot(x, y)

    # Axis labels
    plt.xlabel("Letter Grades")
    plt.ylabel("Percentages")

    # Show graph
    plt.show()





# This function is called when the program starts and manages the other functions
def main():
    """
    Main funciton for Easy A Program.
    
    Prompt users for input, then spits out a graph based on user input
    
    Returns none
    """

    parser = argparse.ArgumentParser()

    # required argument (optional arguments have '-')
    parser.add_argument('dep', help='a single department such as "Math"')
    parser.add_argument('-c', help='a single class such as "Math111"')
    # parser.add_argument('-c', nargs=2, help='class')
    parser.add_argument('-l', type=int, help='all classes of a particular level such as "100"')

    args = parser.parse_args()
    department = args.dep
    clss = args.c
    level = args.l
    
    debugPrint("department argument: ", department)
    debugPrint("optional class argument: ", clss)
    debugPrint("optional level argument: ", level)

    
    print("- EasyA Program -")
    print("Created by Group 1\n")

    #year, subject, course = getInput()

    # Fixed parameters for now --- will eventually be set based on user input
    year = "2014"       # Can range from 2013 to 2016
    subject = "AAAP"     # I considered making an array of all possible subject codes (see top of doc),
                        # but there are just os many that I don't think it's worth it
    course = "510"

    # Get data from data file based on input parameters
    data = getData(year, subject, course)

    # If requested data was found
    if data != None:
        debugPrint("--------")
        debugPrint("- Data -")
        debugPrint("    TERM_DESC:", data["TERM_DESC"])
        debugPrint("    CRN:", data["crn"])
        debugPrint("    aprec:", data["aprec"])
        debugPrint("    bprec:", data["bprec"])
        debugPrint("    cprec:", data["cprec"])
        debugPrint("    dprec:", data["dprec"])
        debugPrint("    fprec:", data["fprec"])
        debugPrint("    instructor:", data["instructor"])
        debugPrint("    numCourses:", data["numCourses"])
        debugPrint("--------\n")

        drawGraph(data)

    # The requested data was not found
    else:
        debugPrint("- Data not found -")
    return


# This calls the 'main' function when this script is executed
if __name__ == "__main__":
    main()
