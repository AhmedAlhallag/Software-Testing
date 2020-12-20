import unittest

from Ex_5_OOP_FP.Files import Files


class TestIntegrationFiles(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fObj = Files()

    def test_objectOfCorrectType(self):
        self.assertIsInstance(self.fObj, Files)

    def test_readFileValidFile(self):
        self.fObj.set_filename("test_data.txt")
        data = self.fObj.read_file()  # "123\n"
        self.assertEqual(data, ["123\n"])

    def test_readFileInValidFile(self):
        self.fObj.set_filename("non-existant.txt")
        with self.assertRaises(FileNotFoundError):
            data = self.fObj.read_file()

    def test_checkRealData(self):
        self.fObj.set_filename("data.txt")
        data = self.fObj.read_file()
        # breakpoint()
        # check the headers
        headers = data[0].split(",")
        headers[-1] = headers[-1].replace("\n", "")
        self.assertEqual(headers[0], "Name")
        self.assertEqual(headers[1], "Age")
        self.assertEqual(headers[2], "Major")
        self.assertEqual(headers[3], "Year")
        # check the content
        row = data[1].split(",")
        row[-1] = row[-1].replace("\n", "")
        self.assertIsInstance(eval(row[1]), int)
