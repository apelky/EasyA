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


    def __str__(self):
        result =  "    Title:     {0}\n".format(self.title)
        result += "    Type:      {0}\n".format(self.type)
        result += "    X axis:    {0}\n".format(self.x_axis_label)
        result += "    Y axis:    {0}\n".format(self.y_axis_label)
        result += "    EasyA:     {0}\n".format(self.isEasyA)
        result += "    AllInstr:  {0}\n".format(self.isAllInstructors)
        result += "    DataLen:   {0}\n".format(len(self.self.data))

        return result


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

        ## Set title
        if self.type == 0:
            self.title = f"{self.data[0].dept} {self.data[0].level}"

        elif self.type == 1:
            self.title = f"All {self.data[0].dept} Classes"

        else:
            x00_level = int(self.data[0].level) - (int(self.data[0].level) % 100)
            self.title = f"All {self.data[0].dept} {x00_level}-level"

        ## Set X-axis title
        if self.type in [0, 1, 2]:

            if self.show_count == True:
                self.x_axis_label = "Instructor (and number of classes taught)"
            else:
                self.x_axis_label = "Instructor"
        else:
            if self.show_count == True:
                self.x_axis_label = "Class (and number of classes taught)"
            else:
                self.x_axis_label = "Class"

        # Set Y-axis & Append to titles - EasyA or - Just Pass
        if self.isEasyA:
            self.title += " - EasyA"
            self.y_axis_label = "% As"
        else:
            self.title += " - Just Pass"
            self.y_axis_label = "% D/Fs"

