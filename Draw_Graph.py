"""
List of functions to be done

Created 1/22/23
"""

"""
Matplotlib is a visaul fucntion library for python: https://matplotlib.org/
"""
import matplotlib.pyplot as plt
import math
from datetime import datetime

from Graph_Class import Graph

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
        if offer.instructor not in instructor_grades:
            instructor_grades[offer.instructor] = 0
            instructor_count[offer.instructor] = 0

        # Increment grade percentage
        instructor_grades[offer.instructor] += offer.a_perc if easyA else offer.df_perc
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

    graph = Graph(graphType, easyA, allInstructors, showCount)
    graph.data = course
    graph.plotting_data = instructor_grades

    default_offer = course[0]
    graph.title = default_offer.dept + " " + default_offer.level + " " + default_offer.term_desc
    graph.title += " - Easy A" if graph.isEasyA else " - Just Pass"

    graph.x_axis_label = "Instructors"
    if graph.isEasyA:
        graph.y_axis_label = "% As"
    else:
        graph.y_axis_label = "% D/Fs"

    return graph


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
    numTotalGraphs = len(graphs)

    # Maximum number of graphs that can be displayed at a time (3x3 grid)
    maxGraphs = 9

    # Current set of graphs to be shown
    set = 1

    # Get time of graph creation
    time = datetime.now().strftime("_%d:%m:%Y_%H-%M-%S")

    # While there are still graphs to display
    while numTotalGraphs > 0:

        # Get the number of graphs to display in the current set
        numDisplayGraphs = numTotalGraphs
        if numTotalGraphs > maxGraphs:
            numDisplayGraphs = maxGraphs
        if numTotalGraphs == 10:
            numDisplayGraphs -= 1

        # Arrange graph layout
        W = math.ceil(math.sqrt(numDisplayGraphs))
        H = math.ceil(numDisplayGraphs / W)
        figure, axis = plt.subplots(W, H)

        # Graph location
        x = 0
        y = 0

        for i in range(numDisplayGraphs):
            graph = graphs[i]

            # Graph data
            names = list(graph.plotting_data.keys())
            for j in range(len(names)):
                name_parts = names[j].split(",")
                names[j] = name_parts[0]
            grades = graph.plotting_data.values()

            # Render graph
            barChart = None
            if numDisplayGraphs >= 3:
                barChart = axis[x, y]
            elif numDisplayGraphs > 1:
                barChart = axis[x]
            else:
                barChart = plt
            barChart.bar(range(len(names)), grades, tick_label=names)
            barChart.set_title(graph.title)

            # Axis labels
            plt.tick_params(axis ='x', rotation = -90, direction = "in", pad = 3)
            plt.ylabel(graph.y_axis_label)
            plt.rc('xtick', labelsize = 8)

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

        # Save graph as a .pdf

        # Append set number to end of graph
        setText = "" if (set == 1 and numTotalGraphs <= maxGraphs) else "_" + str(set)

        # Save graph .pdf in the EasyA pdf folder
        filename = "./EasyA_pdfs/"
        filename += "EasyA_result" if graph.isEasyA else "JustPass_result"
        filename += time + setText + ".pdf"
        plt.savefig(filename, format="pdf")

        # Show graphs
        plt.show()

        # Decrement by graphs shown and move to next set
        numTotalGraphs -= numDisplayGraphs
        set += 1
