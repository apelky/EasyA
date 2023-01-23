"""
Course Class.py

Created: 1/22/23
"""


class Course():

    def __init__(self, department: str, 
                        classLevel: int, 
                        termDesc: str, 
                        a: float, 
                        b: float, 
                        c: float, 
                        d: float, 
                        f: float, 
                        instr: str):
        self.dept = department  # include this just for ease of access
        self.level = classLevel 
        self.term_desc = termDesc
        self.a_perc = a
        self.b_perc = b
        self.c_perc = c
        self.d_perc = d
        self.f_perc = f
        self.df_perc = (d + f) / 2
        self.instructor = instr