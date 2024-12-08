import unittest
import os
from FileUtils import FileUtils
from StudentList import StudentList
from Student import Student

class TestFileUtils(unittest.TestCase):
    def setUp(self):
        self.file_name = "test_1.csv"
        self.student_list = StudentList()
        self.student = Student(name="Ivan", phone="123456789", kurs="1", group="KB-241")
        self.student_list.addNewElement(self.student)

    def test_saveDataToCsv(self):
        FileUtils.saveDataToCsv(self.file_name, self.student_list)
        self.assertTrue(os.path.exists(self.file_name))

    def test_loadDataFromCsv(self):
        FileUtils.loadDataFromCsv(self.file_name, self.student_list)
        new_list = StudentList()
        FileUtils.loadDataFromCsv(self.file_name, new_list)
        self.assertEqual(len(new_list.students), 1)
        self.assertEqual(new_list.students[0].name, "Ivan")

if __name__ == "__main__":
    unittest.main()