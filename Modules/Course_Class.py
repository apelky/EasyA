"""
Course_Class.py created on Jan 22, 2023.

All functions related to graphing the data

Course_Class.py last modified on Sun Feb 5 2023.

Group 1:
Ethan Aasheim
Melodie Collins
Linnea Gilius
Timothy Nadeau
Angela Pelky

A Class representation of This:
        {
            "TERM_DESC": term,
            "aprec": "",
            "bprec": "",
            "cprec": "",
            "crn": "",
            "dprec": "",
            "fprec": "",
            "instructor": ""
        }
"""


class Course():

    def __init__(self, department: str,
                        courseLevel: str,
                        crn: str,
                        termDesc: str,
                        a: float,
                        b: float,
                        c: float,
                        d: float,
                        f: float,
                        instr: str,
                        isProf: bool,
                        n: int):

        self.dept        = department  # include this just for ease of access
        self.level       = courseLevel
        self.crn         = crn
        self.term_desc   = termDesc
        self.a_perc      = float(a)
        self.b_perc      = float(b)
        self.c_perc      = float(c)
        self.d_perc      = float(d)
        self.f_perc      = float(d)
        self.df_perc     = float(d) + float(f)
        self.instructor  = instr.split(",")[0]
        self.isProfessor = isProf
        self.numCourses  = n

    def __str__(self):
        #result =     f'    Dep: {self.dept}\n'
        result =  "    Dep:  {0}\n".format(self.dept)
        result += "    LVL:  {0}\n".format(self.level)
        result += "    CRN:  {0}\n".format(self.crn)
        result += "    A%:   {0}\n".format(str(self.a_perc))
        result += "    D+F%: {0}\n".format(str(self.df_perc))
        result += "    instructor: {0} - ".format(self.instructor)

        if (self.isProfessor):
            result += "is faculty and "
        result += "taught " + str(self.numCourses) + " courses\n"

        return result
