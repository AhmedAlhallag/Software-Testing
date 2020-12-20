import unittest
from Ex_4_OOP_SC.Student import Student
from Ex_4_OOP_SC.Course import Course


"""
What should I test? 
- Are instansiated objects are of correct types? ==> DONE
- Asscoaition is implemeted correctly? Does the Student Obj contain a Course obj ? (testing rolename)
- 
"""


class TestIntegrationStudent(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.courseObj = Course()
        cls.studentObj = Student(cls.courseObj)

    def test_objectsAreOfTheCorectType(self):
        self.assertIsInstance(self.courseObj, Course)
        self.assertIsInstance(self.studentObj, Student)

    def test_studentHasCourseObj(self):
        self.assertIn("courseObj", self.studentObj.__dict__)
        self.assertIsInstance(self.studentObj.courseObj, Course)

    def test_getAvg(self):
        # Happy Path testing
        self.studentObj.set_name("Ahmed")
        self.assertIsNotNone(self.studentObj.get_avg())
        # Sad Path testing
        self.studentObj.set_name("djkbvdsks")
        with self.assertRaises(KeyError):
            self.studentObj.get_avg()

    def test_getAvg_v2(self):
        self.studentObj.set_name("Ahmed")
        grade = self.studentObj.get_avg_v2()
        self.assertEqual(grade, "A")

        self.studentObj.set_name("Mohamed")
        grade = self.studentObj.get_avg_v2()
        self.assertEqual(grade, "B")

        self.studentObj.set_name("Gamal")
        grade = self.studentObj.get_avg_v2()
        self.assertEqual(grade, "C")

        self.studentObj.set_name("Kareem")
        grade = self.studentObj.get_avg_v2()
        self.assertEqual(grade, "D")

        self.studentObj.set_name("Haidy")
        grade = self.studentObj.get_avg_v2()
        self.assertEqual(grade, "F")

        self.studentObj.set_name("dsnk dsjndsv")
        with self.assertRaises(KeyError):
            grade = self.studentObj.get_avg_v2()
