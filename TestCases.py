import unittest

import os
from EasyA import *
from Graph_Class import Graph
from Course_Class import Course
from functions import get_course

class TestEasyA(unittest.TestCase):

    # get_course() test
    def test_get_course(self):
        AAA_321_Offers = get_course("AAA", "321")
        for offer in AAA_321_Offers:
            print(offer)

    # get_department_courses() test
    def test_get_department_courses(self):
        MATH_Dept = get_department_courses("MATH")
        self.assertEqual(len(list(MATH_Dept)), 68, "There are 68 MATH courses")

    # get_department_x00_level() test
    def test_get_department_x00_level(self):
        CIS_Dept = get_department_x00_level("CIS", 100)
        self.assertEqual(len(list(CIS_Dept)), 6, "There are 6 CIS 1xx courses")
        print("\nThere are 6 CIS 1xx courses:")
        for level in CIS_Dept:
            print("  {0}".format(level))

"""
    # countInstructorCourses() test
    def test_countInstructorCourses(self):
        self.assertEqual(countInstructorCourses("Leahy, John F."),          2, "Leahy taught 2 courses")
        self.assertEqual(countInstructorCourses("Sardell, Shannon Mical"),  3, "Sardell taught 3 courses")
        self.assertEqual(countInstructorCourses("Gurley, Gregory C."),      14, "Gurley taught 14 courses")


    # getData() test
    def test_getData(self):
        dataList = getData("AAA", "510", "2014")
        for i in range(1):
            data = dataList[i]
            self.assertEqual(data["aprec"], "85.7",                   "The A% is 85.7%")
            self.assertEqual(data["fprec"], "0.0",                    "The F% is 0.0%")
            self.assertEqual(data["instructor"], "Lachman, Charles",  "The instructor is Lachman, Charles")
            self.assertEqual(data["isProfessor"], False,              "Lachman, Charles is not a professor")


    # checkIfRegularFaculty() test
    def test_checkIfRegularFaculty(self):
        self.assertEqual(checkIfRegularFaculty("Barkan, Alice"),        True, "Barkan IS a professor")
        self.assertEqual(checkIfRegularFaculty("Thornton, Joseph W."),  True, "Thornton IS a professor")
        self.assertEqual(checkIfRegularFaculty("Turner, David Graves"), False, "Turner is NOT a professor")
        self.assertEqual(checkIfRegularFaculty("Eisen, Judith S."),     True, "Thornton IS a professor")
        self.assertEqual(checkIfRegularFaculty("Huette, Scott Edward"), False, "Turner is NOT a professor")


    # Entire program test
    def test_program(self):
        # Course not found
        os.system("python3 EasyA.py -s AAA -c 110 -y 2016 -g 0")

        # Course offered 2 times
        os.system("python3 EasyA.py -s AAD -c 199 -y 2014 -g 0")

        # Course offered 4 times
        os.system("python3 EasyA.py -s AAD -c 250 -y 2013 -g 0")
"""

if __name__ == '__main__':
    unittest.main()
