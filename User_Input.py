"""
UI model
"""

"""
argparse is a module from the Python Standard Library which parses command line options
os is a module from the Python Standard Library which contains miscellaneous operating system interfaces
sys is a module from the Python Standard Library which handles system - specific parameters and functions
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

# BA and LAW have 700 level courses
level_options = [None, 100, 200, 300, 400, 500, 600, 700]


entry = tk.Tk()
# setting the windows size
entry.geometry("600x400")
entry.title('Easy A')

# defining variables
subject_var = tk.StringVar()
subject_var.set(subject_options[0])
course_var = tk.StringVar()
course_var.set("")
level_var = tk.StringVar()
level_var.set(level_options[0])
view_var = tk.IntVar(entry, 1)
instructor_var = tk.IntVar(entry, 1)
easy_a_var = tk.IntVar(entry, 1)

# default values
subject_entry = "AA"
course_entry = ""
level_entry = None
instruct_entry = 1
easy_a_entry = 1


def level_view(event):
    view_label = tk.Label(entry, text = 'view by: ', font = ('calibre', 14, 'bold'))
    view_instructor = tk.Radiobutton(entry, text = 'instructor' , variable = view_var, value = 1, justify = 'left')
    view_class = tk.Radiobutton(entry, text = 'class' , variable = view_var, value = 0, justify = 'left')

    view_label.grid(row = 4, column = 3, pady = (10, 0))
    view_instructor.grid(row = 4, column = 4, sticky = 'W', pady = (10, 0))
    view_class.grid(row = 4, column = 5, sticky = 'W', pady = (10, 0))


# function called upon "submit" button being pushed
def submit():
    global subject_entry
    global course_entry
    global level_entry
    global instruct_entry
    global easy_a_entry

    subject_entry = subject_var.get()
    course_entry = course_var.get()
    if course_entry == 'ex: 111':
        course_entry = ""

    level_entry = level_var.get()
    if level_entry != "None":
        level_entry = [int(level_entry)]
        level_entry.append(view_var.get())

    instruct_entry = instructor_var.get()
    easy_a_entry = easy_a_var.get()

    """ subject_var.set(subject_options[0])
    course_var.set("")
    level_var.set(level_options[0])
    view_var.set(1)
    instructor_var.set(1)
    easy_a_var.set(1) """

    entry.destroy()


def clear(event, box):
    box.delete(0, tk.END)


# main function
def window():

    # define labels
    subject_label = tk.Label(entry, text = 'Subject Code:', font = ('calibre', 14, 'bold'))
    subject_menu = tk.OptionMenu(entry , subject_var , *subject_options )

    blank = tk.Label(entry, text = ' ')
    args_label = tk.Label(entry, text = 'Optional Fields:', font = ('calibre', 14, 'bold'))

    course_label = tk.Label(entry, text = 'Course Number', font = ('calibre', 14, 'bold'))
    enter_course = tk.Entry(entry, textvariable = course_var, font = ('calibre', 14, 'normal'), width = 10)

    enter_course.insert(0, 'ex: 111')
    enter_course.bind("<Button-1>", lambda event: clear(event, enter_course))

    level_label = tk.Label(entry, text = 'All Courses At Level', font = ('calibre', 14, 'bold'))
    level_menu = tk.OptionMenu(entry, level_var, *level_options, command = level_view)

    instructor_label = tk.Label(entry, text = 'Show Instructors: ', font = ('calibre', 14, 'bold'))
    instructor_button = tk.Radiobutton(entry, text = 'All Instructors' , variable = instructor_var, value = 1, justify = 'left')
    faculty_button = tk.Radiobutton(entry, text = 'Regular Faculty' , variable = instructor_var, value = 0, justify = 'left')

    easy_a_label = tk.Label(entry, text = 'Grade Type: ', font = ('calibre', 14, 'bold'))
    easy_a_button = tk.Radiobutton(entry, text = 'Easy A' , variable = easy_a_var, value = 1, justify = 'left')
    just_pass_button = tk.Radiobutton(entry, text = 'Just Pass' , variable = easy_a_var, value = 0, justify = 'left')

    submission = tk.Button(entry, text = 'submit', command = submit)
    entry.update()

    # set in grid
    label_col = 1
    entry_col = 2
    pad_y = (10, 0)

    subject_label.grid(row = 0, column = label_col, pady = (10, 0))
    subject_menu.grid(row = 0, column = entry_col, pady = (10, 0))

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

    submission.grid(row = 8, column = label_col, pady = (20, 0), padx = (10, 0))


    entry.mainloop()

    return subject_entry, course_entry, level_entry, instruct_entry, easy_a_entry, True

    """
    global subject_entry
    global course_entry
    global level_entry
    global instruct_entry
    global easy_a_entry
    """
    return subject_entry, course_entry, level_entry, instruct_entry, easy_a_entry


def updateData(file):
    if not file.lower().endswith('.json'):
        print("ERROR: file must be a JSON file (.json)")
        exit()
    try:
        fstream = open(file)
    except:
        print("ERROR: cannot open file", file)
        exit()
    else:
        global dataFile
        dataFile = "empty.json"
        os.replace(file, dataFile)
        # data = json.load(f)
        fstream.close()
        print("SUCCESS: system updated with new data")
        exit()


def command_line():
    parser = argparse.ArgumentParser()

    # optional arguments
    parser.add_argument('-s', '--subject', help = 'a single subject such as "Math"')
    parser.add_argument('-c', '--course', type = int, help = 'a single course level, such as "111"')
    parser.add_argument('-l', '--level', type = int, help = 'all courses of a particular x00 level, such as "100"')
    parser.add_argument('-r', action = argparse.BooleanOptionalAction, help = 'include to only show regular faculty')
    parser.add_argument('-j', action = argparse.BooleanOptionalAction, help = 'include to only show Just Pass')
    parser.add_argument('-f', help = 'a JSON (.json) file containing grade data')

    args = parser.parse_args()
    print(args)

    subject         = args.subject
    course          = args.course
    level           = args.level
    all_instruct    = int(not args.r)
    easy_a          = int(not args.j)
    file            = args.f

    if file:
        updateData(file)

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

    return subject, course, level, all_instruct, easy_a, True


# returns 'subject' (string), 'course' ([int, int] or None), 'level' (int or None), and 'all_instruct' (int)
def getInput():
    """
    gets input parameters from user via a command line or graphical user interface
    returns:
        one strings: 'subject', 'course', and 'level'
        two bools as ints: 'all_instruct' and 'easy_a'
            if all_instruct is 1, the user wants to see all instructors
            if all_instruct is 0, the user wants to only see regular faculty

            if easy_a is 1, the user wants to see percent A's
            if easy_a is 0, the user wants to see percent D's and F's
    """

    subject, course, level, all_instruct, easy_a, show_count = window() if len(sys.argv) == 1 else command_line()

    return subject, course, level, all_instruct, easy_a, show_count
