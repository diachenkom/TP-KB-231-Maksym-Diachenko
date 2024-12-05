import unittest
from Lab2 import loadDataFromCsv, saveDataToCsv, addNewElement, updateElement, deleteElement
global students


class TestLab2Functions(unittest.TestCase):
    def setUp(self):
        global students
        from Lab2 import students
        students.clear()

    def test_addNewElement(self):
        addNewElement("John Doe", "1234567890", "1", "A")
        self.assertEqual(len(students), 1)
        self.assertEqual(students[0]["name"], "John Doe")

    def test_deleteElement(self):
        addNewElement("John Doe", "1234567890", "1", "A")
        deleteElement("John Doe")
        self.assertEqual(len(students), 0)

    def test_deleteElement_not_found(self):
        addNewElement("John Doe", "1234567890", "1", "A")
        deleteElement("Jane Smith")
        self.assertEqual(len(students), 1)

    def test_updateElement(self):
        addNewElement("John Doe", "1234567890", "1", "A")
        updateElement("John Doe", "Jane Doe", "9876543210", "2", "B")
        self.assertEqual(students[0]["name"], "Jane Doe")
        self.assertEqual(students[0]["phone"], "9876543210")

    def test_loadDataFromCsv(self):
        test_csv = "test_lab2.csv"
        with open(test_csv, "w") as f:
            f.write("name,phone,kurs,group\n")
            f.write("JohnDoe,1234567890,1,A\n")
        loadDataFromCsv(test_csv)
        self.assertEqual(len(students), 1)
        self.assertEqual(students[0]["name"], "JohnDoe")

    def test_saveDataToCsv(self):
        test_csv = "test_output.csv"
        addNewElement("John Doe", "1234567890", "1", "A")
        saveDataToCsv(test_csv)
        with open(test_csv, "r") as f:
            lines = f.readlines()
        self.assertEqual(len(lines), 2) 

if __name__ == "__main__":
    unittest.main()