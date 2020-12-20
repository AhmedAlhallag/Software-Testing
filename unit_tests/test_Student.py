import unittest
import mock
from Ex_4_OOP_SC.Student import Student


"""
What should I test? 
- Is this class instantiable ?
- test the setter (set_name()) #MAY be skipped
- test the boiler-plate that ahs no logic (get_avg()) 
and decoupling dependencies via mocking  # SHOULD be skipped in unit but #MAY be integration tested
(illustrated to introduce mocking)
- test boiler-plate that has some logic (get_avg_v2()) 
# SHOULD NOT be skipped  in either unit or integration testing
"""


class TestStudent(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        courseMockedObj = mock.Mock()
        cls.student = Student(courseMockedObj)

    def test_canCreateObj(self):
        with self.assertRaises(Exception):
            Student()

    def test_setName(self):
        """
        Testing setters/getters in unit/integration may be skipped
        """
        self.student.set_name("Ahmed")
        self.assertEqual(self.student.name, "Ahmed")

    def test_getAvg(self):
        """
        Testing boiler-plate (has no extra logic): SHOULD be skipped in unit testing
        MAY be integration-tested 
        """
        # pass
        self.student.courseObj.calc_avg.return_value = True
        self.assertIsNotNone(self.student.get_avg(), None)

    def test_getAvg_v2(self):
        """
        Testing boiler-plate (HAS extra logic): SHOULD be unit-tested/integration-tested
        """
        self.student.courseObj.calc_avg.side_effect = [9, 8, 7, 6, 4]
        grade = self.student.get_avg_v2()  # 1--> 9
        self.assertEqual(grade, "A")

        grade = self.student.get_avg_v2()  # 2--> 8
        self.assertEqual(grade, "B")

        grade = self.student.get_avg_v2()  # 3--> 7
        self.assertEqual(grade, "C")

        grade = self.student.get_avg_v2()  # 4--> 6
        self.assertEqual(grade, "D")

        grade = self.student.get_avg_v2()  # 5--> 4
        self.assertEqual(grade, "F")
