import unittest
from Ex_4_OOP_SC.Course import Course
import mock
"""
What can we unit test ?
- course information exists --> Done  
- Can create an object ==> Done
- seaarch_Student  ==> Done
- calc_avg  ==> Done
"""

class TestCourse(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.course = Course()
        cls.mockedStudentObj = mock.Mock()

    def test_canCreateObj(self):
        with self.assertRaises(TypeError):
            Course("Dummy")

    def test_InfrExists(self):
        self.assertIsNotNone(self.course.course_info)

    def test_searchStudentRuternsVal(self):
        self.mockedStudentObj.name = "Ahmed"
        student = self.course.search_student(self.mockedStudentObj)
        self.assertIsNotNone(student)

    def test_searchStudentRuternsNone(self):
        self.mockedStudentObj.name = "ajkbvdshk"
        student = self.course.search_student(self.mockedStudentObj)
        self.assertIsNone(student)

    def test_calcAvgReturnsVal(self):
        self.mockedStudentObj.name = "Ahmed"
        avg = self.course.calc_avg(self.mockedStudentObj)
        self.assertIsNotNone(avg)

    def test_calcAvgReturnsVal(self):
        self.mockedStudentObj.name = "dsnvbks"
        with self.assertRaises(KeyError):
            avg = self.course.calc_avg(self.mockedStudentObj)