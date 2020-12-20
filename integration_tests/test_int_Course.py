import unittest

from Ex_4_OOP_SC.Course import Course
from Ex_4_OOP_SC.Student import Student

"""
What should I integration-test?
- is the created Course object created correctly, is it of type/class Course?
- make sure the actual data contained Db (in tthis case; the hard-coded-values) is correct
"""


class TestIntegrationCourse(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.course = Course()
        cls.studentObj = Student(cls.course)

    def test_objectOfCorrectType(self):
        self.assertIsInstance(self.course, Course)
        self.assertIsInstance(self.studentObj, Student)

    def test_checkSampleData(self):
        sample_pos = {
            "s_name": "Kareem",  # D
            "mid1": 5.5,
            "mid2": 4.5
        }
        sample_neg = {
            "s_name": "John",  # D
            "mid1": 5.5,
            "mid2": 4.5
        }
        self.assertNotIn(sample_neg, self.course.course_info)

    def test_searchStudentReturnsVal(self):
        # Happy path tesing
        self.studentObj.set_name("Ahmed")
        student = self.course.search_student(self.studentObj)
        self.assertIsNotNone(student)

    def test_searchStudentReturnsNone(self):
        # Sad path tesing
        self.studentObj.set_name("dsnvksnvds")
        student = self.course.search_student(self.studentObj)
        self.assertIsNone(student)

    def test_calcAvgReturnsVal(self):
        # Happy path test
        self.studentObj.set_name("Ahmed")
        avg = self.course.calc_avg(self.studentObj)  # float
        self.assertIsInstance(avg, float)

    def test_calcAvgRaiseError(self):
        # Happy path test
        self.studentObj.set_name("kbvks")
        with self.assertRaises(KeyError):
            avg = self.course.calc_avg(self.studentObj)  # float
