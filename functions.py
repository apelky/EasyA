"""
List of functions to be done

Created 1/22/23
"""

from Graph_Class import Graph
from Course_Class import Course

from GradeData import groups
##### Test dictionaries #####
single_course_test = {"MTH111": [
                                    {
                                        "TERM_DESC": "Winter 2015",
                                        "aprec": "10.0",
                                        "bprec": "20.0",
                                        "cprec": "30.0",
                                        "crn": "123456",
                                        "dprec": "20.0",
                                        "fprec": "20.0",
                                        "instructor": "John Smith"
                                    },
                                    {
                                        "TERM_DESC": "Fall 2016",
                                        "aprec": "30.0",
                                        "bprec": "10.0",
                                        "cprec": "10.0",
                                        "crn": "123456",
                                        "dprec": "10.0",
                                        "fprec": "40.0",
                                        "instructor": "Matt Le Blanc"
                                    }
                                ]
                    }


multiple_course_test = {"MTH111": [
                                    {
                                        "TERM_DESC": "Winter 2015",
                                        "aprec": "10.0",
                                        "bprec": "20.0",
                                        "cprec": "30.0",
                                        "crn": "123456",
                                        "dprec": "20.0",
                                        "fprec": "20.0",
                                        "instructor": "John Smith"
                                    },
                                    {
                                        "TERM_DESC": "Fall 2016",
                                        "aprec": "30.0",
                                        "bprec": "10.0",
                                        "cprec": "10.0",
                                        "crn": "123456",
                                        "dprec": "10.0",
                                        "fprec": "40.0",
                                        "instructor": "Matt Le Blanc"
                                    }
                                ],
                        "MTH212": [
                                    {
                                        "TERM_DESC": "Winter 2015",
                                        "aprec": "20.0",
                                        "bprec": "30.0",
                                        "cprec": "40.0",
                                        "crn": "567894",
                                        "dprec": "20.0",
                                        "fprec": "10.0",
                                        "instructor": "Arthur Pendragon"
                                    },
                                    {
                                        "TERM_DESC": "Fall 2015",
                                        "aprec": "5.0",
                                        "bprec": "15.0",
                                        "cprec": "40.0",
                                        "crn": "645642",
                                        "dprec": "10.0",
                                        "fprec": "30.0",
                                        "instructor": "Robert Henry"
                                    }
                                ]
                    }


#############################



##### Helper functions #####
# Feel free to add on your own functions you can think of if it helps you
# Just document it well

def sort_dict(d: dict):
    """
    Desc:
        Returns a sorted dicitonary of numbers from Hi to Lo by values
        Ex:
            {"X": 1, "Y": 2, "Z": 3} -> {"Z": 3, "Y": 2, "X": 1}

        Useful for sorting Graph.plotting_data

    Parameters:
        d   (dict) - Dictionary to be sorted by values

    Return:
        Dictionary - Sorted dictionary
    """
    # should probably check if values are all same type so it can
    # genuinely distinguish which values are > and < others
    pass


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
        Counts the number of times all classes were offered in the given data list.
        Returns a dictionary of {"Class": times_offered} pairs

        Useful for when parsing data in update_plotting_data()

    Parameters:
        courses    (List of Course objects) - Courses of classes taught

    Returns:
        Dictionary   - {"Class":times_offered, ...}

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
                sums_dict[instr_name] += data[i].a_perc 
                count_dict[instr_name] += 1
            else:
                sums_dict[instr_name] = data[i].a_perc 
                count_dict[instr_name] = 1
        else:
            if instr_name in count_dict:
                sums_dict[instr_name] += data[i].df_perc 
                count_dict[instr_name] += 1
            else:
                sums_dict[instr_name] = data[i].df_perc
                count_dict[instr_name] = 1

    instructors = list(sums_dict.keys())
    instr_avg = dict()
    for i in range(len(instructors)):
        instr_avg[instructors[i]] = (sums_dict[instructors[i]] / count_dict[instructors[i]])

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
                sums_dict[course_name] += data[i].a_perc 
                count_dict[course_name] += 1
            else:
                sums_dict[course_name] = data[i].a_perc 
                count_dict[course_name] = 1
        else:
            if course_name in count_dict:
                sums_dict[course_name] += data[i].df_perc 
                count_dict[course_name] += 1
            else:
                sums_dict[course_name] = data[i].df_perc
                count_dict[course_name] = 1

    classes = list(sums_dict.keys())
    class_avg = dict()
    for i in range(len(classes)):
        class_avg[classes[i]] = (sums_dict[classes[i]] / count_dict[classes[i]])

    return class_avg




#################################

def get_course(dept: str, level: int):
    """
    Desc:
        Searches the database for a course given the course's department and level
        Returns with a dictionary of a list consisting of course offering dictionaries
          that match the given criteria

    Parameters:
        dept (str)  -  Department of class   Ex: "MTH"
        level (int) -  Course Level          Ex: 111

    Returns:
        A list of Course objects
    """

    rawData = groups[dept + level]
    courseList = []

    for i in range(len(rawData)):
        offer = rawData[i]
        instructor = offer["instructor"]

        # Create new course object
        course = Course(dept, level, offer["crn"], offer["TERM_DESC"],
                        offer["aprec"], offer["bprec"], offer["cprec"], offer["dprec"], offer["fprec"],
                        instructor, False, 1)
        #checkIfRegularFaculty(instructor)
        #countInstructorCourses(instructor)

        # Add course to list
        courseList.append(course);

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
                "MTH115":  [
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
                                    instructor, False, 1)
                    #checkIfRegularFaculty(instructor)
                    #countInstructorCourses(instructor)

                    # Add course to list
                    courseList.append(course);
                courseDict[key] = courseList

    return courseDict


def update_plotting_data(graph: Graph):
    """
    MUST BE CALLED AFTER ADDING DATA TO GRAPH FOR NEW DATA TO APPEAR

    Desc:
        Recalculates plotting data
        (Useful if graph.data gets updated)


    Parameters:
        graph (Graph) - Graph to update plotting data in

    Returns:
        True    - successful
        False   - unsuccessful



    NOTE: (delete me later)
        Doing this as a global function allows us to use other helper
        functions to do this as well instead of having the Graph.py
        class 1) import the main file? and 2) assume functional functions from another file


    """

    # Filter out Faculty
    processing_data = graph.data

    # Check that processing data is all Course objects
    for i in range(len(processing_data)):
        if type(processing_data[i]) != Course:
            return False    # Found an element that's not a Course object 
    

    # Filter out all Non-faculty if needed
    if not graph.isAllInstructors: # If FacultyOnly
        #remove all instructors from processing_data
        for i in reversed(range(len(graph.data))):
            if processing_data[i].isProfessor:  # we remove the professors, right?
                processing_data.pop(i)

    new_data = dict()
    if (graph.type in [0, 1, 2]): # Single Class
        # This type will assume self.data is a List of Course objects
        new_data = calc_instr_avg(processing_data, graph.isEasyA)
        new_data = sort_dict(new_data)


    elif (graph.type == 3): # <Dept> x00 level Classes (by class)
        new_data = calc_class_avg(processing_data, graph.isEasyA)
        new_data = sort_dict(new_data)



    if graph.show_count:
        # edit x axis names to add instructor count
            # do this by taking the keys
        
        data_keys = list(new_data.keys())
        if (graph.type == 3):
            xaxis_count = find_class_count(processing_data) # get a dict of counts 

        else: # The other types of graph that's now by class
            xaxis_count = find_instr_count(processing_data) # get a dict of counts

        for i in range(len(new_data)):
            pass

    graph.plotting_data = new_data
    graph.update_labels() # should be last thing in this function hopefuly




def plot_graphs(graphs : list):
    """
    Desc:
        Plots list of graph objects. Using matplotlib library
           If more than 1, put them on same plot side-by-side (using subplots)

    Parameters:
        List (of Graph objects) - Graphs to be plotted

    Returns:
        None

    Documentation/Demo for graphing w/ subplots
    https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html
    """
    # *Hopefully* this can be done in a loop since every graph should have
    # the data it needs for it to have a title, label, etc

    # also double check to make sure every element in the list is a Graph type
    pass



def save_as_pdf(filename: str, graphs: list):
    """
    Desc:
        Save Graphs to .PDF file of <filename>.pdf

    Parameters:
        filename (str) - Name of file to save as
        graphs (list of Graphs) - Graphs to plot and save onto .PDF

    Returns:
        None (but also technically <filename>.pdf ;D )


    NOTE:
        As of right now, idk if plot_graphs may just do this,
        or what. But graphs gotta be put it in some sort of plot.
        @Ethan, if you're looking at this, feel free to adjust
        this function or plot_graphs() to fit this requirement.
        Only thing need to keep is graphs (list of Graph objects)
        parameter.
    """
    pass





########### TESTING / DEBUGGING ##########
def main():
    """Main function to run
    FOR TESTING PURPOSES ONLY
    """

    pass



if __name__ == "__main__":
    main()
