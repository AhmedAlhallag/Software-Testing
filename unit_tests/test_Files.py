import unittest

from Ex_5_OOP_FP.Files import Files
import mock
from io import StringIO

"""
What should we unit-test? (isolated, unit: Files Class) DONE
- can create an object? DONE
- (open/read) read_file() --> FP DONE
- (open/write) write_file() --> FP DONE
- prints() --> stdout DONE
"""


class TestFiles(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fObj = Files("fake.txt")

    def test_canCreateObj(self):
        fObj1 = Files()
        fObj2 = Files("fake.txt")
        self.assertIsNone(fObj1.filename)
        self.assertIsNotNone(fObj2.filename)

    def test_readFile(self):
        with mock.patch("builtins.open", mock.mock_open(read_data="EXPECTED")) as mockedFileObj:
            data = self.fObj.read_file()
            self.assertEqual(data, ["EXPECTED"])
            mockedFileObj.assert_called_with(self.fObj.filename, "r")

    def test_writeFile(self):
        with mock.patch("builtins.open", mock.mock_open()) as mockedOpenedFileObj:
            self.fObj.write_file("FAKE", "w")
            mockedOpenedFileObj.return_value.write.assert_called_with("FAKE\n")
            mockedOpenedFileObj.assert_called_with(
                self.fObj.filename, "w")

    def test_sayHello(self):
        """
        - Mock standard output stream --> by piping the output into a 'TEMP FILE OBJ' 
        that we create on the spot instead.
        """
        with mock.patch("sys.stdout", new=StringIO()) as fakeOutStream:
            self.fObj.say_hello("Ahmed")
            self.assertEqual(fakeOutStream.getvalue(), "Hello Ahmed!\n")

        with mock.patch("sys.stdout", new=StringIO()) as fakeOutStream:
            self.fObj.say_hello()
            self.assertEqual(fakeOutStream.getvalue(), "Hello Stranger!\n")
