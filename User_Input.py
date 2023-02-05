"""
UI model
"""
import tkinter as tk

"""
argparse is a module from the Python Standard Library which parses command line options
sys is a module from the Python Standard Library which handles system - specific parameters and functions
"""
import argparse

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
entry.geometry("480x320")
entry.title('Easy A')

# defining variables
subject = tk.StringVar()
subject.set(subject_options[0])
course = tk.StringVar()
course.set("")
level = tk.StringVar()
level.set(level_options[0])
instructor = tk.IntVar(entry, 1)
easy_a = tk.IntVar(entry, 1)


subject_entry = "AA"
course_entry = ""
level_entry = None
instruct_entry = 1
easy_a_entry = 1


# function called upon "submit" button being pushed
def submit():
    global subject_entry
    global course_entry
    global level_entry
    global instruct_entry
    global easy_a_entry

    subject_entry = subject.get()
    course_entry = course.get()
    if course_entry == 'ex: 111':
        course_entry = ""

    level_entry = level.get()
    if level_entry != "None":
        level_entry = int(level_entry)

    instruct_entry = instructor.get()
    easy_a_entry = easy_a.get()

    print("subject: ", subject_entry)
    print("course: ", course_entry)
    print("level: ", level_entry)
    print("all instructors?: ", instruct_entry)
    print("easy_a?: ", easy_a_entry)

    subject.set(subject_options[0])
    course.set("")
    level.set(level_options[0])
    instructor.set(1)
    easy_a.set(1)

    entry.destroy()


def clear(event, box):
    box.delete(0, tk.END)


# main function
def window():

    # define labels
    subject_label = tk.Label(entry, text = 'Subject Code:', font = ('calibre', 14, 'bold'))
    subject_menu = tk.OptionMenu(entry , subject , *subject_options )

    blank = tk.Label(entry, text = ' ')
    args_label = tk.Label(entry, text = 'optional fields:', font = ('calibre', 14, 'bold'))

    course_label = tk.Label(entry, text = 'Course Number', font = ('calibre', 14, 'bold'))
    enter_course = tk.Entry(entry, textvariable = course, font = ('calibre', 14, 'normal'), width = 10)

    enter_course.insert(0, 'ex: 111')
    enter_course.bind("<Button-1>", lambda event: clear(event, enter_course))

    level_label = tk.Label(entry, text = 'All Courses At Level', font = ('calibre', 14, 'bold'))
    level_menu = tk.OptionMenu(entry, level, *level_options)

    instructor_label = tk.Label(entry, text = 'Show Instructors: ', font = ('calibre', 14, 'bold'))
    instructor_button = tk.Radiobutton(entry, text = 'All Instructors' , variable = instructor, value = 1, justify = 'left')
    faculty_button = tk.Radiobutton(entry, text = 'Regular Faculty' , variable = instructor, value = 0, justify = 'left')

    easy_a_label = tk.Label(entry, text = 'Grade Type: ', font = ('calibre', 14, 'bold'))
    easy_a_button = tk.Radiobutton(entry, text = 'Easy A' , variable = easy_a, value = 1, justify = 'left')
    just_pass_button = tk.Radiobutton(entry, text = 'Just Pass' , variable = easy_a, value = 0, justify = 'left')

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

    return subject_entry, course_entry, level_entry, instruct_entry, easy_a_entry


# Gets input parameters from user via a command line interface
# Returns 'subject' (string), 'courseLvl' (int or None), 'level' (int or None), and 'year' (int or None)
def getInput(): #def updateData():
    """
    debugPrint("Optional subject code argument: ", subject)
    debugPrint("Optional course argument: ", courseLvl)
    debugPrint("Optional level argument: ", level)
    debugPrint("Optional year argument: ", year)
    debugPrint("Optional graph argument: ", showGraph)
    """

    # Optional arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', help='A single subject code, such as "MATH"')
    parser.add_argument('-c', type=int, help='A single course level, such as "111"')
    parser.add_argument('-l', type=int, help='All courses of a particular x00 level, such as "100"')
    parser.add_argument('-r', type=int, help='Whether to only show regular faculty')
    parser.add_argument('-a', type=int, help='Whether to show Easy A instead of Just Pass')
    parser.add_argument('-f', help='A .json file containing grade data')
    args = parser.parse_args()
    file = args.f

    if file is not None:
        if not file.lower().endswith('.json'):
            print("ERROR: file must be a JSON file (.json)")
            return
        try:
            fstream = open(file)
        except:
            print("ERROR: cannot open file", file)
        else:
            for line in fstream:
                continue
            print("system updated with new data")

    # Argument variables
    args        = parser.parse_args()
    subject     = args.s
    courseNum   = args.c
    level       = args.l
    allInstr    = not (args.r == None or (args.a != 0 and args.a != False))
    easyA       = args.a == None or (args.a != 0 and args.a != False)

    # If no command line arguments, open user interface
    if args.s is None and args.c is None and args.l is None and args.r is None:
        subject, courseNum, level, allInstr, easyA = window()

    # Make sure that all arguments are provided by line input if not through the command line
    else:

        # Subject code (mandatory)
        if args.s is None:
            subject = input("Enter subject code: ")

        # Course number or level (optional)
        if args.c is None and args.l is None:
            view_course = input("Do you want view a specific course number? [y or n]: ")
            if view_course:
                courseNum = int(input("Enter course number: "))
            else:
                view_level = input("Do you want view a specific course level (x00)? [y or n]: ")
                if view_level:
                    level = (int((input("Enter level (x00) for all courses you want to view: ")) / 100) * 100)

        # All instructors or regular faculty (mandatory)
        if args.r is None:
            allInstr = not (input("Do you want only view regular faculty? [y or n]: "))

    return subject, courseNum, level, allInstr, easyA
