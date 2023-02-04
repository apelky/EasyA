import tkinter as tk


options = ["AA", "AAA", "AAAP", "AAD", "ACTG", "AEIS", "AFR", "AIM", "ANTH", "ARB", "ARCH", "ARH", "ART", "ARTC", "ARTD",
            "ARTF", "ARTM", "ARTO", "ARTP", "ARTR", "ARTS", "ASIA", "ASL", "ASTR", "BA", "BE", "BI", "CAS", "CDS", "CFT", "CH",
            "CHN", "CINE", "CIS", "CIT", "CLAS", 'COLT', "CPSY", "CRES", "CRWR", 'DAN', "DANC", "DSC", "EALL", "EC", "EDLD", "EDST"
]

entry = tk.Tk()
 
# setting the windows size
entry.geometry("600x400")

subject = tk.StringVar()
subject.set(options[0])
course = tk.StringVar()
level = tk.StringVar()
year = tk.StringVar()


def submit():
    # print("getting entries")
    subject_entry = subject.get()
    course_entry = course.get()
    level_entry = level.get()
    year_entry = year.get()
     
    # print("printing entries")
    print("subject: ", subject_entry)
    print("course: ", course_entry)
    print("level: ", level_entry)
    print("subject: ", year_entry)
     
    """ print("resetting entries")
    subject.set("")
    course.set(0)
    level.set(0)
    year.set(0) """
    entry.destroy()


def clear(event, box):
    box.delete(0, tk.END)
    # box.unbind('<Button-1>', tk.click_event)


subject_label = tk.Label(entry, text = 'subject', font = ('calibre', 14, 'bold'))
# enter_subject = tk.Entry(entry, textvariable = subject, font = ('calibre', 14, 'normal'))
subject_menu = tk.OptionMenu(entry , subject , *options )

# enter_subject.pack()
""" enter_subject.insert(0, 'Math')
enter_subject.bind("<Button-1>", lambda event: clear(event, enter_subject)) """

course_label = tk.Label(entry, text = 'course', font = ('calibre', 14, 'bold'))
enter_course = tk.Entry(entry, textvariable = course, font = ('calibre', 14, 'normal'))

level_label = tk.Label(entry, text = 'level', font = ('calibre', 14, 'bold'))
enter_level = tk.Entry(entry, textvariable = level, font = ('calibre', 14, 'normal'))

year_label = tk.Label(entry, text = 'year', font = ('calibre', 14, 'bold'))
enter_year = tk.Entry(entry, textvariable = year, font = ('calibre', 14, 'normal'))

submission = tk.Button(entry, text = 'submit', command = submit)

subject_label.grid(row = 0, column = 0)
subject_menu.grid(row = 0, column = 1)

course_label.grid(row = 1, column = 0)
enter_course.grid(row = 1, column = 1)

level_label.grid(row = 2, column = 0)
enter_level.grid(row = 2, column = 1)

year_label.grid(row = 3, column = 0)
enter_year.grid(row = 3, column = 1)

submission.grid()

entry.mainloop()