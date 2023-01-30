import tkinter as tk


subject_options = ["AA", "AAA", "AAAP", "AAD", "ACTG", "AEIS", "AFR", "AIM", "ANTH", "ARB", "ARCH", "ARH", "ART", "ARTC", "ARTD",
                    "ARTF", "ARTM", "ARTO", "ARTP", "ARTR", "ARTS", "ASIA", "ASL", "ASTR", "BA", "BE", "BI", "CAS", "CDS", "CFT", "CH",
                    "CHN", "CINE", "CIS", "CIT", "CLAS", 'COLT', "CPSY", "CRES", "CRWR", 'DAN', "DANC", "DSC", "EALL", "EC", "EDLD", "EDST"
]

level_options = [None, 100, 200, 300, 400]
year_options = [None, 2013, 2014, 2015, 2016]

class Input():
    def __init__(self) -> None:
        pass

entry = tk.Tk()
 
# setting the windows size
entry.geometry("600x400")

subject = tk.StringVar()
subject.set(subject_options[0])
course = tk.StringVar()
level = tk.StringVar()
level.set(level_options[0])
year = tk.StringVar()
year.set(year_options[0])
graph = tk.IntVar()


def submit():
    global subject_entry
    global course_entry
    global level_entry
    global year_entry
    global graph_entry

    subject_entry = subject.get()
    course_entry = course.get()
    if course_entry == 'ex: 111':
        course_entry = ""
    
    level_entry = level.get()
    if level_entry != "None":
        level_entry = int(level_entry)
    
    year_entry = year.get()
    
    graph_entry = bool(graph.get())
    
     
    print("subject: ", subject_entry)
    print("course: ", course_entry)
    print("level: ", level_entry)
    print("year: ", year_entry)
    print("show graph: ", graph_entry)
    
    entry.destroy()


def clear(event, box):
    box.delete(0, tk.END)
    # box.unbind('<Button-1>', tk.click_event)


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

    year_label = tk.Label(entry, text = 'year', font = ('calibre', 14, 'bold'))
    year_menu = tk.OptionMenu(entry, year, *year_options)

    entry.update()

    graph_label = tk.Label(entry, text = 'show graph', font = ('calibre', 14, 'bold'))
    enter_graph = tk.Checkbutton(entry, variable = graph)
    enter_graph.select()
    

    submission = tk.Button(entry, text = 'submit', command = submit)

    # set in grid
    subject_label.grid(row = 0, column = 0)
    subject_menu.grid(row = 0, column = 1)

    blank.grid(row = 1)
    args_label.grid(row = 2, column = 1)

    course_label.grid(row = 3, column = 0)
    enter_course.grid(row = 3, column = 1)

    level_label.grid(row = 4, column = 0)
    level_menu.grid(row = 4, column = 1)

    year_label.grid(row = 5, column = 0)
    year_menu.grid(row = 5, column = 1)

    graph_label.grid(row = 6, column = 0)
    enter_graph.grid(row = 6, column = 1)

    submission.grid()

    entry.mainloop()
    return subject_entry, course_entry, level_entry, year_entry, graph_entry