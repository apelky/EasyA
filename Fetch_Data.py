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

from Faculty_Parser import *

#############################


##### Helper functions #####
# Feel free to add on your own functions you can think of if it helps you
# Just document it well
def tuple_list_flip(alist):
	retList = []
	for i in range(len(alist)):
		retList.append((alist[i][1], alist[i][0]))
	return retList


def sort_dict(d: dict, hi2lo: bool=True):
    """
    Desc:
        Returns a sorted dicitonary of numbers from Hi to Lo by values
        Or if hi2low is False, then will return lo to hi values
        Ex:
            {"X": 1, "Y": 2, "Z": 3} -> {"Z": 3, "Y": 2, "X": 1}


        Useful for sorting Graph.plotting_data

    Parameters:
        d   (dict) - Dictionary to be sorted by values
        hi2lo (bool) - Optional flag to have values count low to high

    Return:
        Dictionary - Sorted dictionary
    """
    # should probably check if values are all same type so it can
    # genuinely distinguish which values are > and < others
    items = list(d.items())
    items = tuple_list_flip(items)
    items.sort()    # sort low to high
    if hi2lo:
        items.reverse() # sort high to low
    items = tuple_list_flip(items)

    retDict = dict()
    for i in range(len(items)):
        retDict[items[i][0]] = items[i][1]
    return retDict


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


def find_instr_count(courses: list):
    """
    Desc:
        Counts the number of times all instructors taught a course in the given data list.
        Returns a dictionary of {"Professor":teach_count} pairs

        Useful for when parsing data in update_plotting_data()

    Parameters:
        courses    (List of Course objects) - Courses count instructor's teach counts

    Returns:
        Dictionary   - {"Instructor":teach_count, ...}

    """
    instr_count = dict()
    for i in range(len(courses)):
        instr_name = courses[i].instructor
        if instr_name in instr_count:  # if already in dictionary
            instr_count[instr_name] += 1
        else:   # add to dictionary
            instr_count[instr_name] = 1

    return instr_count


def find_class_count(courses: list):
    """
    Desc:
        Counts the number of times all courses were offered in the given data list.
        Returns a dictionary of {"course": times_offered} pairs

        Useful for when parsing data in update_plotting_data()

    Parameters:
        courses    (List of Course objects) - Courses taught

    Returns:
        Dictionary   - {"course": times_offered, ...}

    """
    class_offerings = dict()
    for i in range(len(courses)):
        course_name = combine_dept_and_level(courses[i].dept, courses[i].level)
        if course_name in class_offerings:  # if already in dictionary
            class_offerings[course_name] += 1
        else:   # add to dictionary
            class_offerings[course_name] = 1

    return class_offerings


def calc_instr_avg(data: list, isEasyA: bool=True):
    """
    Desc:
        Searches list of Course objects for instructor's a% avg (or df% if isEasyA is False)
        Returns a dictionary of {"Instructor": _%avg} pairs of the data

        Useful for updating plotting data

    Parameters:
        data    (List of Course objects) - Courses count instructor's teach counts
        isEasyA (bool) - Search function option. A% if True, D/F% if False

    Returns:
        Dictionary - {"Instructor": _%avg}
    """
    sums_dict = dict()
    count_dict = dict()
    for i in range(len(data)):
        instr_name = data[i].instructor
        if isEasyA:
            if instr_name in count_dict:
                sums_dict[instr_name] += float(data[i].a_perc)
                count_dict[instr_name] += 1
            else:
                sums_dict[instr_name] = float(data[i].a_perc)
                count_dict[instr_name] = 1
        else:
            if instr_name in count_dict:
                sums_dict[instr_name] += float(data[i].df_perc)
                count_dict[instr_name] += 1
            else:
                sums_dict[instr_name] = float(data[i].df_perc)
                count_dict[instr_name] = 1

    instructors = list(sums_dict.keys())
    instr_avg = dict()
    for i in range(len(instructors)):
        instr_avg[instructors[i]] = round((sums_dict[instructors[i]] / count_dict[instructors[i]]), 2)

    return instr_avg


def calc_class_avg(data: list, isEasyA: bool=True):
    """
    Desc:
        Searches list of Course objects for class' a% avg (or df% if isEasyA is False)
        Returns a dictionary of {"Class": _%avg} pairs of the data

        Useful for updating plotting data

    Parameters:
        data    (List of Course objects) - Courses count class' teach counts
        isEasyA (bool) - Search function option. A% if True, D/F% if False

    Returns:
        Dictionary - {"Class": _%avg}
    """
    sums_dict = dict()
    count_dict = dict()
    for i in range(len(data)):
        course_name = combine_dept_and_level(data[i].dept, data[i].level)
        if isEasyA:
            if course_name in count_dict:
                sums_dict[course_name] += float(data[i].a_perc)
                count_dict[course_name] += 1
            else:
                sums_dict[course_name] = float(data[i].a_perc)
                count_dict[course_name] = 1
        else:
            if course_name in count_dict:
                sums_dict[course_name] += float(data[i].df_perc)
                count_dict[course_name] += 1
            else:
                sums_dict[course_name] = float(data[i].df_perc)
                count_dict[course_name] = 1

    classes = list(sums_dict.keys())
    class_avg = dict()
    for i in range(len(classes)):
        class_avg[classes[i]] = round((sums_dict[classes[i]] / count_dict[classes[i]]),2)

    return class_avg


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

    rawData = groups[dept + str(level)]
    courseList = []

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
                rawData = groups[key]
                courseList = []
                for i in range(len(rawData)):
                    offer = rawData[i]
                    instructor = offer["instructor"]

                    # Create new course object
                    course = Course(dept, lvl, offer["crn"], offer["TERM_DESC"],
                                    offer["aprec"], offer["bprec"], offer["cprec"], offer["dprec"], offer["fprec"],
                                    instructor, checkIfRegularFaculty(instructor), 0)
                    #checkIfRegularFaculty(instructor)

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
