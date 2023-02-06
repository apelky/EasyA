"""
User Input module, last modified on Sun Feb 5, 2023.
This handles user input, either via command line or graphical user interface.

Group 1:
Ethan Aasheim
Melodie Collins
Linnea Gilius
Timothy Nadeau
Angela Pelky
"""

"""
modules from the Python Standard Library:
argparse: parses command line options
os: contains miscellaneous operating system interfaces
sys: handles system - specific parameters and functions
"""
import argparse
import os
import sys

import tkinter as tk


# lists for option menus
natural_science = ['BI', 'CH', 'CIS', 'CIT', 'HPHY', 'MATH', 'PHYS', 'PSY']
subject_options = ['AA', 'AAA', 'AAAP', 'AAD', 'ACTG', 'AEIS', 'AFR', 'AIM', 'ANTH', 'ARB', 'ARCH', 'ARH', 'ART', 'ARTC',
'ARTD', 'ARTF', 'ARTM', 'ARTO', 'ARTP', 'ARTR', 'ARTS', 'ASIA', 'ASL', 'ASTR', 'BA', 'BE', 'BI', 'CAS', 'CDS', 'CFT', 'CH',
'CHN', 'CINE', 'CIS', 'CIT', 'CLAS', 'COLT', 'CPSY', 'CRES', 'CRWR', 'DAN', 'DANC', 'DSC', 'EALL', 'EC', 'EDLD', 'EDST',
'EDUC', 'ENG', 'ENVS', 'ES', 'EURO', 'FHS', 'FIN', 'FLR', 'FR', 'GEOG', 'GEOL', 'GER', 'GRK', 'HBRW', 'HC', 'HIST', 'HPHY',
'HUM', 'IARC', 'INTL', 'IST', 'ITAL', 'J', 'JC', 'JDST', 'JPN', 'KRN', 'LA', 'LAS', 'LAT', 'LAW', 'LERC', 'LIB', 'LING',
'LT', 'MATH', 'MDVL', 'MGMT', 'MIL', 'MKTG', 'MUE', 'MUJ', 'MUP', 'MUS', 'OAKI', 'OANG', 'OANU', 'OATH', 'OBA', 'OBIK',
'OBLN', 'OBRI', 'OBRT', 'OBWU', 'OCAM', 'OCBS', 'OCFP', 'OCHA', 'OCIE', 'OCUB', 'OCUR', 'ODEA', 'ODIS', 'ODUB', 'OESL',
'OEWH', 'OFAC', 'OFES', 'OFIB', 'OGAL', 'OGHA', 'OHAR', 'OHAU', 'OHKU', 'OHOU', 'OHUJ', 'OINT', 'OJCU', 'OJIL', 'OJWU',
'OKYO', 'OLAT', 'OLEC', 'OLEG', 'OLEI', 'OLIS', 'OLON', 'OLYO', 'OMCT', 'OMEI', 'ONEO', 'ONTU', 'ONUS', 'OOVI', 'OPAV',
'OPDG', 'OPOI', 'OQUE', 'OQUI', 'OROM', 'OROS', 'OSAS', 'OSCI', 'OSEG', 'OSEN', 'OSIE', 'OSIP', 'OSIT', 'OSLO', 'OSSP',
'OSTP', 'OSVL', 'OTAM', 'OUAB', 'OUDB', 'OUEA', 'OUNA', 'OUOT', 'OUPP', 'OVAN', 'OVIC', 'OVIE', 'OWAS', 'OXAF', 'OXAO',
'OXEU', 'OXFA', 'OXGL', 'OXLA', 'OYON', 'PD', 'PEAE', 'PEAQ', 'PEAS', 'PEF', 'PEI', 'PEIA', 'PEL', 'PEMA', 'PEMB', 'PEO',
'PEOL', 'PEOW', 'PERS', 'PERU', 'PETS', 'PEW', 'PHIL', 'PHYS', 'PORT', 'PPPM', 'PS', 'PSY', 'REES', 'REL', 'RL', 'RUSS',
'SAPP', 'SBUS', 'SCAN', 'SOC', 'SPAN', 'SPD', 'SPED', 'SPSY', 'SWAH', 'SWED', 'TA', 'TLC', 'WGS', 'WR']
level_options = [None, 100, 200, 300, 400, 500, 600, 700]


# constructing the tkinter widget
entry = tk.Tk()
# setting the window size and title
entry.geometry("600x400")
entry.title('Easy A')

# defining tkinter variables
subject_var = tk.StringVar()
subject_var.set(subject_options[0])
course_var = tk.StringVar()
course_var.set("")
level_var = tk.StringVar()
level_var.set(level_options[0])
view_var = tk.IntVar(entry, 1)
instructor_var = tk.IntVar(entry, 1)
easy_a_var = tk.IntVar(entry, 1)
count_var = tk.IntVar()


# default values for subject, course, level, all_instruct, easy_a, show_count
# defined as globals for easy modification
subject_entry = "AA"
course_entry = ""
level_entry = None
instruct_entry = 1
easy_a_entry = 1
count_entry = 0


def level_view(event):
    """
    function called upon clicking the level option meu
    handles the user selecting if they want to view by instructor or by course number
    """
    # define labels
    view_label = tk.Label(entry, text = 'view by: ', font = ('calibre', 14, 'bold'))
    view_instructor = tk.Radiobutton(entry, text = 'instructor' , variable = view_var, value = 1, justify = 'left')
    view_class = tk.Radiobutton(entry, text = 'class' , variable = view_var, value = 0, justify = 'left')

    # set labels in grid
    view_label.grid(row = 4, column = 3, pady = (10, 0))
    view_instructor.grid(row = 4, column = 4, sticky = 'W', pady = (10, 0))
    view_class.grid(row = 4, column = 5, sticky = 'W', pady = (10, 0))


def submit():
    """
    function called upon clicking the "submit" button
    gets and formats user input from tkinter widget
    """

    global subject_entry
    global course_entry
    global level_entry
    global instruct_entry
    global easy_a_entry
    global count_entry

    subject_entry = subject_var.get()
    course_entry = course_var.get()
    if course_entry == 'ex: 111':
        course_entry = ""

    level_entry = [level_var.get(), view_var.get()]

    instruct_entry = instructor_var.get()
    easy_a_entry = easy_a_var.get()
    count_entry = count_var.get()

    entry.destroy()


def clear(event, box):
    """
    function called upon clicking the course number entry box
    clears the suggested text
    """
    box.delete(0, tk.END)


def window():
    """
    driver for handling user input from a graphical user interface
    """

    # define labels
    subject_label = tk.Label(entry, text = 'Subject Code:', font = ('calibre', 14, 'bold'))
    subject_menu = tk.OptionMenu(entry , subject_var , *subject_options )

    blank = tk.Label(entry, text = ' ')
    args_label = tk.Label(entry, text = 'Optional Fields:', font = ('calibre', 14, 'bold'))

    course_label = tk.Label(entry, text = 'Course Number:', font = ('calibre', 14, 'bold'))
    enter_course = tk.Entry(entry, textvariable = course_var, font = ('calibre', 14, 'normal'), width = 10)

    enter_course.insert(0, 'ex: 111')
    enter_course.bind("<Button-1>", lambda event: clear(event, enter_course))

    level_label = tk.Label(entry, text = 'All Courses At Level:', font = ('calibre', 14, 'bold'))
    level_menu = tk.OptionMenu(entry, level_var, *level_options, command = level_view)

    instructor_label = tk.Label(entry, text = 'Show Instructors: ', font = ('calibre', 14, 'bold'))
    instructor_button = tk.Radiobutton(entry, text = 'All Instructors' , variable = instructor_var, value = 1, justify = 'left')
    faculty_button = tk.Radiobutton(entry, text = 'Regular Faculty' , variable = instructor_var, value = 0, justify = 'left')

    easy_a_label = tk.Label(entry, text = 'Grade Type: ', font = ('calibre', 14, 'bold'))
    easy_a_button = tk.Radiobutton(entry, text = 'Easy A' , variable = easy_a_var, value = 1, justify = 'left')
    just_pass_button = tk.Radiobutton(entry, text = 'Just Pass' , variable = easy_a_var, value = 0, justify = 'left')

    count_label = tk.Label(entry, text = 'Show # of Classes:', font = ('calibre', 14, 'bold'), justify = 'left')
    count_button = tk.Checkbutton(entry, variable = count_var, justify = 'left')

    submission = tk.Button(entry, text = 'submit', command = submit)
    entry.update()

    # set labels in grid
    label_col = 1
    entry_col = 2
    pad_y = (10, 0)

    subject_label.grid(row = 0, column = label_col, pady = pad_y)
    subject_menu.grid(row = 0, column = entry_col, pady = pad_y)

    blank.grid(row = 1)
    args_label.grid(row = 2, column = entry_col)

    course_label.grid(row = 3, column = label_col, pady = pad_y)
    enter_course.grid(row = 3, column = entry_col, pady = pad_y)

    level_label.grid(row = 4, column = label_col, pady = pad_y)
    level_menu.grid(row = 4, column = entry_col, pady = pad_y)

    instructor_label.grid(row = 5, column = label_col, pady = pad_y)
    instructor_button.grid(row = 5, column = entry_col, sticky = 'W', pady = pad_y)
    faculty_button.grid(row = 5, column = entry_col + 1, sticky = 'W', pady = pad_y)

    easy_a_label.grid(row = 6, column = label_col, pady = pad_y)
    easy_a_button.grid(row = 6, column = entry_col, sticky = 'W', pady = pad_y)
    just_pass_button.grid(row = 6, column = entry_col + 1, sticky = 'W', pady = pad_y)

    count_label.grid(row = 7, column = label_col, sticky = 'W', pady = pad_y)
    count_button.grid(row = 7, column = entry_col, sticky = 'W', pady = pad_y)

    submission.grid(row = 8, column = label_col, pady = (20, 0), padx = (10, 0))

    entry.mainloop()

    return subject_entry, course_entry, level_entry, instruct_entry, easy_a_entry, count_entry


def update_data(file):
    """
    handles a system administrator updating the system with new data
    input file must be a JSON (.json) file

    parameter: file name (string)
    """

    if not file.lower().endswith('.json'):
        print("ERROR: file must be a JSON file (.json)")
        exit()
    try:
        fstream = open(file, "r+")
    except:
        print("ERROR: cannot open file", file)
        exit()
    else:
        first_line, remainder = fstream.readline(), fstream.read()
        with open("temp.py", 'w') as new_file:
            new_file.write('groups = {\n')
            new_file.write(remainder)

        os.replace("temp.py", "Modules/GradeData.py")

        print("SUCCESS: system updated with new data")
        exit()


def command_line():
    """
    driver for handling user input from the command line
    """

    # creates an argparse.ArgumentParser instance
    parser = argparse.ArgumentParser()

    # optional arguments
    parser.add_argument('-s', '--subject', help = 'a single subject such as "Math"')
    parser.add_argument('-c', '--course', type = int, help = 'a single course level, such as "111"')
    parser.add_argument('-l', '--level', type = int, help = 'all courses of a particular x00 level, such as "100"')
    parser.add_argument('-r', action = argparse.BooleanOptionalAction, help = 'include to only show regular faculty')
    parser.add_argument('-j', action = argparse.BooleanOptionalAction, help = 'include to only show Just Pass')
    parser.add_argument('-n', action = argparse.BooleanOptionalAction, help = 'include to show number of classes')
    parser.add_argument('-f', '--file', help = 'a JSON (.json) file containing grade data')

    # parse and process command line arguments
    args = parser.parse_args()
    subject         = args.subject
    course          = str(args.course)
    level           = args.level
    all_instruct    = int(not args.r)
    easy_a          = int(not args.j)
    show_count      = int(not args.n)
    file            = args.file

    if file:
        # call update_data to process file
        update_data(file)

    if subject is None:
        print("ERROR: subject code is mandatory")
        subject = input("Enter subject code: ")

    if subject.upper() not in subject_options:
        print("ERROR: invalid subject code")
        exit()

    if level is not None:
        level = (level // 100) * 100
        if level not in level_options:
            print("ERROR: invalid level; levels are 100 - 700")
            exit()
        level = [level, 1]

    return subject.upper(), course, level, all_instruct, easy_a, show_count


def getInput():
    """
    gets input parameters from user via a command line or graphical user interface
    returns:
        two strings: 'subject' and 'course'
        one list of type [int, int] or NoneType: 'level'
            if the user specifies a level, [level (rounded down to the nearest 100), view] is returned.
                if view is 1, the user wants to view by instructor
                if view is 0, the user wants to view by class
            if the user does not specify a level, None is returned
        three integers: 'all_instruct', 'easy_a', 'show_count'
            if all_instruct is 1, the user wants to see all instructors
            if all_instruct is 0, the user wants to only see regular faculty

            if easy_a is 1, the user wants to see percent A's
            if easy_a is 0, the user wants to see percent D's and F's

            if show_count is 1, the user wants to see the class count
    """

    subject, course, level, all_instruct, easy_a, show_count = window() if len(sys.argv) == 1 else command_line()

    return subject, course, level, all_instruct, easy_a, show_count
