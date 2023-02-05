"""
List of functions to be done

Created 1/22/23
"""

"""
Matplotlib is a visaul fucntion library for python: https://matplotlib.org/
"""
import matplotlib.pyplot as plt
import math

from GradeData import groups
from Course_Class import Course

from EasyA import *
from Faculty_Parser import *

#############################


def split_dept_and_level(courseKey: str):
    """
    Desc:
        Returns a tuple of course split into (dept, level):

        Use split_dept_and_level()[0] to get dept
            split_dept_and_level()[1] to get level

        Example:
            "MTH111" -> (MTH, 111)

    Parameters:
        courseKey (str) - Key to be split

    Returns:
        Tuple   (dept: str, level: int)

    """
    string = courseKey.strip()
    index = 0
    for i in range(len(string)):
        if string[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            index = i
            break
    return (string[0:index], string[index:len(string)])


def combine_dept_and_level(dept: str, level:int):
    """
    Desc:
        Returns a string of combines dept and level

        Example:
           combine_dept_and_level(MTH, 111) -> "MTH111"

    Parameters:
        dept    (str) - Department of course
        level   (str) - Level of course

    Returns:
        String
    """
    return dept + str(level)


#################################


def get_course(dept: str, level: int):
	"""
	Desc:
	    Searches the database for a course given the course's department and level
	    Returns with a dictionary of a list consisting of course offerings
	      that match the given criteria

	Parameters:
	    dept (str)  -  Department of class   Ex: "MTH"
	    level (int) -  Course Level          Ex: 111

	Returns:
	    A list of Course objects
	"""

	courseList = []
	key = dept + str(level)

	if key in groups:
		rawData = groups[key]
		for i in range(len(rawData)):
			offer = rawData[i]
			instructor = offer["instructor"]

			# Create new course object
			course = Course(dept, level, offer["crn"], offer["TERM_DESC"],
			                offer["aprec"], offer["bprec"], offer["cprec"], offer["dprec"], offer["fprec"],
			                instructor, checkIfRegularFaculty(instructor), 0)

			# Add course to list
			courseList.append(course);

		# Count times each instructor taught a course in this list
		for course in courseList:
		    course.numCourses = find_instr_count(courseList)

	return courseList


def get_department_courses(dept: str):
    """
    Desc:
        Searches the database for courses given in a department
        Returns a dictionary consisting of a list of course
            offering dictionaries within the department

    Parameters:
        dept    (str) - Department to retrieve classes in

    Returns:
        Dictionary  - With multiple Course objects within
        retVal = {"MTH111": [
                            {offering 1},
                            {offering 2},
                            {offering 3}
                            ]
                ,
                "MTH212":  [
                            {offering 1},
                            {offering 2},
                            {offering 3}
                            ]
                ,
                    ...
                }
    """

    # Get all course keys
    keysList = list(groups.keys())
    courseList = {}

    # Find matching department
    for key in keysList:
        lvl = key[len(key)-3:]
        if (dept == key[:-3]):
            # Add all courses in that particular level
            courseList[key] = get_course(dept, lvl)

    return courseList


def get_department_x00_level(dept: str, level: int):
	"""
	Desc:
	    Searches the database for courses at x00 level in a department
	    Returns a dictionary consisting of a list of course
	        offering dictionaries of x00 level within the department
	    Any level will be rounded down to nearest hundred (422 -> 400)

	Parameters:
	    dept (str)  -  Department of class   Ex: "MTH"
	    level (int) -  Course Level          Ex: 111    (this'll be rounded down to 100)

	Returns:
	    Dictionary  - With multiple courses within
	    retVal = {"MTH111": [
	                        {offering 1},
	                        {offering 2},
	                        {offering 3}
	                        ]
	            ,
	            "MTH115":   [
	                        {offering 1},
	                        {offering 2},
	                        {offering 3}
	                        ]
	            ,
	                ...
	            }
	"""

	# Get all course keys
	keysList = list(groups.keys())
	courseDict = {}

	# Find matching department
	for key in keysList:
		lvl = key[len(key)-3:]
		if dept == key[:-3]:
			if int(lvl) >= level and int(lvl) < level + 100:
				courseList = []
				if key in groups:
					rawData = groups[key]
					for i in range(len(rawData)):
						offer = rawData[i]
						instructor = offer["instructor"]

						isInstr = True#checkIfRegularFaculty(instructor)

						# Create new course object
						course = Course(dept, lvl, offer["crn"], offer["TERM_DESC"],
						                offer["aprec"], offer["bprec"], offer["cprec"], offer["dprec"], offer["fprec"],
						                instructor, isInstr, 0)

						# Add course to list
						courseList.append(course);

					# Count times each instructor taught a course in this list
					for course in courseList:
					    course.numCourses = find_instr_count(courseList)
					courseDict[key] = courseList

	return courseDict


def convert_to_Courses(classes_dict: dict):
    """
    Desc:
        Takes a class dictionary and converts all the offerings
        of courses into Course objects in a list
        Then returns that list of Courses

        (Useful for getting list of dictionaries prepped
            before adding to Graph)

    Parameters:
        classes_dict (dict) - Classes to be converted
            Ex: {"MTH111": [
                            {offering 1},
                            {offering 2},
                            {offering 3}
                            ]
                ,
                "MTH115":  [
                            {offering 1},
                            {offering 2},
                            {offering 3}
                            ]
                ,
                    ...
                }

    Returns:
        List (of Course objects)
    """
    # Check if it's already a list
    if (type(classes_dict) == list):
        return  # quit if it is

    courseList = [] # retVal
    keys = list(classes_dict.keys())    # list of keys

    for i in range(len(classes_dict)):  # For every key
        for j in range(len(classes_dict[keys[i]])): # For every item in list of value
            courseList.append(classes_dict[keys[i]][j]) # append to courseList
    return courseList
