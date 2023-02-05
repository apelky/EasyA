'''
Faculty_Parser.py created by Angela Pelky on Tue Jan 17, 2023.

Group 1:
Ethan Aasheim
Melodie Collins
Linnea Gilius
Timothy Nadeau
Angela Pelky

This is a part of the system that implements an update to the Emerald Grade Tracker (EGT).
The original EGT can be found here: 'https://emeraldmediagroup.github.io/grade-data'
The EGT displays the letter-grade distribuition across all professors in a particular department of the natural science at the University of Oregon.
This system builds upon the original EGT by directly comparing professors in the same department on the same graph, and is only concerned with the extreme ends of the letter-grade spectrum.

----------------------------------------

Developer must provide "Regular_Faculty.txt" if any updates/changes have been made to the Natural Sciences faculty.

EasyA.py uses Python 3.10
'''

# File containing regular faculty for all Natural Sciences
# Data pulled from https://web.archive.org/web/20141107201343/http://catalog.uoregon.edu/arts_sciences/
dataFile = "Reg Faculty.txt"


def getFacultyNames():
    """
    Reads the file and puts the names into a list.

    Parameters:
        none

    Returns:
        without_dups (str) - A list of names ex: ['Gregory M. Williams', 'Zena M. Ariola']
    """

    # Open dataset file
    f = open(dataFile, "r")
    lines = f.readlines()

    # Initalized list for names to be appended to
    names_list = []

    # Read data in from file
    for line in lines:
         # - Traverse dataset -

        # Find the first instance of a comma
        name_position = line.find(",")
        if name_position != -1:
            # Grab everything before the comma
            name = line[:name_position]
            # Append the name into the list
            names_list.append(name)

    # Remove duplicates
    without_dups = list(set(names_list))

    # Close dataset file
    f.close()

    return without_dups


def parseFacultyNames():
    """
    Sort the list to get it in Last Name, First Name Middle Name order to match data in EasyA

    Parameters:
        none

    Returns:
        new_names_list (str) - A list of names ex: ['Williams, Gregory M.', 'Ariola, Zena M.']
    """
    names_list = getFacultyNames()
    new_names_list = []

    for name in names_list:
        # Find the last instance of a space
        last_index = name.rfind(" ")
        # Grab everything after that space
        last = name[last_index+1:]
        # Grab everything before that space
        first = name[:last_index]
        # Concatenate the string into the desired format
        l_comma_f = last + ", " + first
        # Append the formatted name to a list
        new_names_list.append(l_comma_f)

    return new_names_list


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


# Intializes the program
def main():
    parseFacultyNames()


# This calls the 'main' function when this script is executed
if __name__ == "__main__":
    main()
