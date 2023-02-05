"""
List of functions to be done

Created 1/22/23
"""

"""
Matplotlib is a visaul fucntion library for python: https://matplotlib.org/
"""
import matplotlib.pyplot as plt
import math
#from datetime import datetime

from Fetch_Data import *
from Course_Class import Course
from Graph_Class import Graph


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


# Creat a graph object from a course object
def createGraph(course, graphType, easyA=True, allInstructors=True, showCount=False):
    """
    Draw a graph given a list of course offers
    using matplotlib functions

    Parameters: A list
        course    = list of Course objects
        easyA     = bool
        showGraph = bool

    Return:
        None    print(graph)
    """

    # Get all instructors and check for duplicates
    instructor_grades = {}
    instructor_count  = {}

    # Go through all offers of the course
    for offer in course:
        key = offer.instructor
        if showCount:
            key += " (" + str(offer.numCourses) + ")"
        if key not in instructor_grades:
            instructor_grades[key] = 0
            instructor_count[key] = 0

        # Increment grade percentage
        instructor_grades[key] += offer.a_perc if easyA else offer.df_perc
        instructor_count[key] += 1

    # Second pass of instructors for average grade percentage
    for name in instructor_grades.keys():
        instructor_grades[name] /= instructor_count[name]

    # Get list of instructor names
    names = []
    grades = []
    for name in instructor_grades.keys():
        names.append(name)
        grades.append(instructor_grades[name])

    graph = Graph(graphType, easyA, allInstructors, showCount)
    graph.add_data(course)
    update_plotting_data(graph)

    first_offer = course[0]
    if graphType == 0:
        graph.title = first_offer.dept + " " + str(first_offer.level)
    elif graphType == 1:
        graph.title = "All " + first_offer.dept + " Classes"
    else:
        graph.title = "All " + first_offer.dept + " " + first_offer.level + "-Level"

    # default_offer = course[0]
    # graph.title = default_offer.dept + " " + default_offer.level + " " + default_offer.term_desc
    # graph.title += " - Easy A" if graph.isEasyA else " - Just Pass"

    # graph.x_axis_label = "Instructors"
    # if graph.isEasyA:
    #     graph.y_axis_label = "% As"
    # else:
    #     graph.y_axis_label = "% D/Fs"

    return graph


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

    graph.plotting_data = new_data

    if graph.show_count:
        # edit x axis names to add instructor count
            # do this by taking the keys

        data_keys = list(new_data.keys())
        if (graph.type == 3):
            xaxis_count = find_class_count(processing_data) # get a dict of counts

        else: # The other types of graph that's now by class
            xaxis_count = find_instr_count(processing_data) # get a dict of counts

        xaxis_count = sort_dict(xaxis_count)    # sort the dict
        xaxis_count_items = list(xaxis_count.items())
        shown_count_points = dict()
        # print(xaxis_count_items)
        for i in range(len(new_data)):
            shown_count_points[xaxis_count_items[i][0] + " ("  + str(xaxis_count_items[i][1]) + ")"] = new_data[xaxis_count_items[i][0]]
        graph.plotting_data = shown_count_points



    graph.plotting_data = sort_dict(graph.plotting_data, graph.isEasyA)

    graph.update_labels() # should be last thing in this function hopefuly


def plot_graphs(graphs : list, subject, courseNum, level):
    """
    Desc:
        Plots list of graph objects. Using matplotlib library
           If more than 1, put them on same plot side-by-side (using subplots)

    Parameters:
        graphs (list of Graph objects) - Graphs to be plotted
        subject, courseNum, level - for the .pdf file name

    Returns:
        None

    Documentation/Demo for graphing w/ subplots
    https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html
    """
    # *Hopefully* this can be done in a loop since every graph should have
    # the data it needs for it to have a title, label, etc

    # also double check to make sure every element in the list is a Graph type
    """
    g = Graph(0, True, True, True)
    for graph in graphs:
        print(graph.graphType)

    self.type = 0
    self.isAllInstructors = is_AllInstructors   # JustFaculty if false
    self.data = []                              # list of Course objects
    self.plotting_data = {}                     # Dict of data w/ plot points
    self.title = ""
    self.x_axis_label = ""
    self.y_axis_label = ""
    """

    # Get number of graphs
    graphsRemaining = len(graphs)

    # Maximum number of graphs that can be displayed at a time (3x3 grid)
    maxGraphs = 9

    # Current set of graphs to be shown
    set = 1

    # Get time of graph creation
    #time = "TIME" #datetime.now().strftime("_%d:%m:%Y_%H-%M-%S")

    # While there are still graphs to display
    while graphsRemaining > 0:

        # Get the number of graphs to display in the current set
        numDisplayGraphs = graphsRemaining
        if graphsRemaining > maxGraphs:
            numDisplayGraphs = maxGraphs
        if graphsRemaining == maxGraphs + 1:
            numDisplayGraphs -= 1

        # Arrange graph layout
        W = math.ceil(math.sqrt(numDisplayGraphs))
        H = math.ceil(numDisplayGraphs / W)
        figure, axis = plt.subplots(H, W, figsize=(16, 9))

        # Graph location in grid
        x = 0
        y = 0

        offset = len(graphs) - graphsRemaining
        for i in range(numDisplayGraphs):
            graph = graphs[offset + i]

            # Graph data
            names = list(graph.plotting_data.keys())
            for j in range(len(names)):
                name_parts = names[j].split(",")
                names[j] = name_parts[0]
            grades = graph.plotting_data.values()

            # Render graph
            plt.subplot(W, H, i+1)
            plt.bar(range(len(names)), grades, tick_label=names)
            plt.title(graph.title)

            # Axis labels
            plt.tick_params(axis ='x', rotation = -90, direction = "in", pad = 3)
            plt.ylabel(graph.y_axis_label)
            plt.rc('xtick', labelsize = 10)

            # Max y value is 100%
            ax = plt.subplot(W, H, i+1)
            ax.set_ylim(0, 100)

            # Where the graph should be displayed in the grid of graphs
            x += 1
            if x >= W:
                x = 0
                y += 1

        # Graph styling
        plt.subplots_adjust(left = 0.1, right = 0.95, bottom = 0.1, top = 0.95, wspace = 0.25, hspace = 0.5)

        # Append set number to end of graph
        setText = "" if (set == 1 and graphsRemaining <= maxGraphs) else "_" + str(set)

        # Save graph .pdf in the EasyA pdf folder
        filename = "./EasyA_pdfs/"
        filename += "EasyA_result" if graph.isEasyA else "JustPass_result"

        # Add query description to filename
        if subject != None and subject != "None" and subject != "":
            filename += "_" + subject
            if courseNum != None and courseNum != "None" and courseNum != "":
                filename += "_" + courseNum
            else:
                filename += "_All"
                if level != None and level != "None" and level != "":
                    filename += "_" + level
                else:
                    filename += "_All"

        # Save graph as a .pdf
        filename += setText + ".pdf"
        plt.savefig(filename, format="pdf")

        # Show graphs
        plt.show()

        # Decrement by graphs shown and move to next set
        graphsRemaining -= numDisplayGraphs
        set += 1
