"""
Graph class

TYPES:
    0 = Single course       ("MTH 111")
    1 = Single department   ("MTH")
    2 = Dept x00 level      ("MTH" 100 level)
    3 = Dept x00 level by class ("MTH" 100 level)
"""
from Course_Class import Course

class Graph():

    def __init__(self, graphType: int,
                is_EasyA: bool=True,
                is_AllInstructors=True,
                showCount: bool=False):
        """
        ### VARIABLES FOR GRAPH CLASS ###
        self.type       (int) - Determines what type of graph it is. This variable doesn't change
                                    0 = Single course       ("MTH 111")
                                    1 = Single department   ("MTH")
                                    2 = Dept x00 level      ("MTH", 100 level)
                                    3 = Dept x00 level by class ("MTH", 100 level)

        self.show_count (bool) - Optional flag to show class count of professor (False by default)
        self.isEasyA    (bool) - Optional flag to calculate EasyAs vs JustPasses (True by default)
        self.isAllInstructors (bool) - Optional flag to include Professors & Faculty (True by default)
                                            False will include only Faculty
        self.data  (list of Courses) - List of all courses for which this graph will use data from
                                            Filters like self.isAllInstructors are not applied to this list
        self.plotting_data    (dict) - Dictionary of all plot points for graph. Key is X value, Value is Y value
                                            Ex: {“Patel”: 60.0,
                                                 “Wang”: 40.0,
                                                 “Smith”: 30.0,
                                                 “Garcia”: 20.0}
        self.title         (str) - Title of graph. Needs to be updated by self.update_labels() after data has been
                                    added, and before the graph has been plotted (Empty str by default)
        self.x_axis_label  (str) - Label of X axis values. Needs to be updated by self.update_labels() after data has been
                                    added, and before the graph has been plotted (Empty str by default)
        self.y_axis_label  (str) - Label of Y axis values. Needs to be updated by self.update_labels() after data has been
                                    added, and before the graph has been plotted (Empty str by default)

        """
        self.type = graphType
        self.isEasyA = is_EasyA
        self.isAllInstructors = is_AllInstructors   # JustFaculty if false
        self.show_count = showCount
        self.data = []                              # list of Course objects
        self.plotting_data = {}                     # Dict of data w/ plot points
        self.title = ""
        self.x_axis_label = ""
        self.y_axis_label = ""
        # self.w = 0
        # self.h = 0


    def add_data(self, new_data: list):
        """
        Desc:
            Takes a set of data to input into graph's data.
            Checks if the list consists of only Course objects
            Returns T/F if successful/failure

        Parameters:
            new_data    (List of Course objects (not dicts)) - Data to replace self.data

        Returns:
            True  - if successful
            False - error occured (bad data)
        """
        for i in range(len(new_data)):      # check if all items in list are classes
            if type(new_data[i]) != Course:     # if not a Course Class type, abort
                return False
        self.data = new_data                # add data to self.data
        return True


    def update_labels(self):
        """
        CALL AFTER self.add_data() AND BEFORE PLOTTING

        Desc:
            Updates the Graph's title & axes labels

            Titles & Axes are empty strs when Graph is init'd
                only until after data has been added, can we
                know specifically what these need to be.
                Thus the reason for this function

        Parameters:
            None

        Returns:
            None
        """
        # This function will update them after data has been added

        # This function updates
        #     Title
        #     X-axis label
        #     Y-Axis label

        # for each type

        # Each graph.type will vary slightly. account for that
          self.x_axis_label = "Instructor"

            if self.isEasyA == True:
                self.y_axis_label = "% As"
            else:
                self.y_axis_label = "% D/Fs"

        if self.type == 2:
            # Title: All <dept> x00-level
            # X axs: Instructor  (if showcount, Instructor (and number of classes taught))
            # Y axs: % As        (if isEasyA, % D/Fs otherwise)

            self.title = "All " + self.data.dept + " " + self.data.courseLevel + "-level"

            if self.show_count == True:
                self.x_axis_label = "Instructor (and number of classes taught)"
            else:
                self.x_axis_label = "Instructor"

            if self.isEasyA == True:
                self.y_axis_label = "% As"
            else:
                self.y_axis_label = "% D/Fs"

        if self.type == 3:
            # Title: All <dept> x00-level
            # X axs: Class       (if showcount, Class (and number of classes taught))
            # Y axs: % As        (if isEasyA, % D/Fs otherwise)

            self.title = "All " + self.data.dept + " " + self.data.courseLevel + "-level"

            if self.show_count == True:
                self.x_axis_label = "Class (and number of classes taught)"
            else:
                self.x_axis_label = "Class"

            if self.isEasyA == True:
                self.y_axis_label = "% As"
            else:
                self.y_axis_label = "% D/Fs"


##### Old, brainstorming stuff. Can discuss why this is commented out #####
    # def update_plotting_data(self):
    #     """
    #     Desc:
    #         Recalculates plotting data
    #         (Useful if self.data gets updated)

    #     Don't change graph.data
    #     Use the copy (processing_data) to parse through and update the

    #     Parameters:
    #         none

    #     Returns:
    #         none
    #     """
    #     # Filter out Faculty
    #     processing_data = self.data
    #     if not self.isAllInstructors: # If FacultyOnly
    #         #remove all instructors from processing_data
    #         pass


    #     if (self.type == 0): # Single Class
    #         # This type will assume self.data is a List of Course objects
    #         pass

    #     elif (self.type == 1): # Single Department
    #         # This type will assume self.data is a List of Course objects
    #         pass

    #     elif (self.type == 2): # <Dept> x00 level Classes (by instructor)
    #         # This type will assume self.data is a List of Course objects
    #         pass

    #     elif (self.type == 3): # <Dept> x00 level Classes (by class)
    #         pass

    #     if self.show_count:
    #         # edit x axis names to add instructor count
    #             # do this by taking the keys
    #         pass



    # def drawGraph():
    #     """
    #     draws the graph using self.plotting_data to
    #     draw a graph
    #     """
    #     pass
