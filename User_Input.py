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
    subject_label = tk.Label(entry, text = 'subject', font = ('calibre', 14, 'bold'))
    subject_menu = tk.OptionMenu(entry , subject , *subject_options )

    blank = tk.Label(entry, text = ' ')
    args_label = tk.Label(entry, text = 'optional fields:', font = ('calibre', 14, 'bold'))

    course_label = tk.Label(entry, text = 'course', font = ('calibre', 14, 'bold'))
    enter_course = tk.Entry(entry, textvariable = course, font = ('calibre', 14, 'normal'), width = 10)
    
    enter_course.insert(0, 'ex: 111')
    enter_course.bind("<Button-1>", lambda event: clear(event, enter_course))
    
    level_label = tk.Label(entry, text = 'level', font = ('calibre', 14, 'bold'))
    level_menu = tk.OptionMenu(entry, level, *level_options)

    instructor_label = tk.Label(entry, text = 'show: ', font = ('calibre', 14, 'bold'))
    instructor_button = tk.Radiobutton(entry, text = 'All Instructors' , variable = instructor, value = 1, justify = 'left')
    faculty_button = tk.Radiobutton(entry, text = 'Regular Faculty' , variable = instructor, value = 0, justify = 'left')

    easy_a_label = tk.Label(entry, text = 'show: ', font = ('calibre', 14, 'bold'))
    easy_a_button = tk.Radiobutton(entry, text = 'Easy A' , variable = instructor, value = 1, justify = 'left')
    just_pass_button = tk.Radiobutton(entry, text = 'Just Pass' , variable = instructor, value = 0, justify = 'left')
    
    submission = tk.Button(entry, text = 'submit', command = submit)
    entry.update()

    # set in grid
    label_col = 0
    entry_col = 1
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

    global subject_entry
    global course_entry
    global level_entry
    global instruct_entry
    global easy_a_entry

    return subject_entry, course_entry, level_entry, instruct_entry, easy_a_entry
    # return subject.get(), course.get(), level.get(), instructor.get(), easy_a.get()