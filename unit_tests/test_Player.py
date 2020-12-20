import unittest

from Ex_3_OOP_Player.Player import Player

""" TEST CASES:
- ARGS Should not be empty? ===> DONE
- Class? is that class instansiable ? ====> DONE
- fname,lname --> str ==> DONE
- speed -> int ==> DONE
- EXAMLE NICKNAME: ====> DONE
- Check the id count of craeted objects ==> DONE
"""


class TestPlayer(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.p1 = Player("Kareem", "Gamal", 100)  # 2
        # gets executed once oniy at the start before the rest of test/instance methods

    def setUp(self):
        # this gets executed before evry single test method
        # print("..STARTING BEFORE THIS UPCOMING METHOD...")
        pass

    def test_createObjWithInvalidParams(self):
        with self.assertRaises(AssertionError):
            Player("", "", None)

    def test_FLnameValType(self):
        self.assertIsInstance(self.p1.fname, str)
        self.assertIsInstance(self.p1.lname, str)

        with self.assertRaises(AssertionError):
            Player(True, 2121, 212)

    def test_speedValType(self):
        # HAppy path test --> int
        self.assertIsInstance(self.p1.speed, int)

        with self.assertRaises(AssertionError):
            Player("Ahmed", "Mohamed", "212")

    def test_canCreateObj(self):
        # Sad testing path
        with self.assertRaises(TypeError):
            Player()

    def test_playerID(self):
        self.assertEqual(self.p1.id, 1)

    def test_nickname(self):
        self.p1.set_nickname()
        self.assertEqual(self.p1.nickname, "K.Gamal")
