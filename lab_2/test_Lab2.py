import unittest
from Lab2 import loadDataFromCsv, saveDataToCsv, addNewElement, updateElement, deleteElement
global students

class TestLab2Functions(unittest.TestCase):
    def setUp(self):
        global students
        from Lab2 import students
        students.clear()

    def test_addNewElement(self):
        addNewElement("Maksym", "1234567890", "2", "kb-231")
        self.assertEqual(len(students), 1)
        self.assertEqual(students[0]["name"], "Maksym")

    def test_deleteElement(self):
        addNewElement("Maksym", "1234567890", "2", "kb-231")
        deleteElement("Maksym")
        self.assertEqual(len(students), 0)

    def test_deleteElement_not_found(self):
        addNewElement("Maksym", "1234567890", "2", "kb-231")
        deleteElement("Jane")
        self.assertEqual(len(students), 1)

    def test_updateElement(self):
        addNewElement("Maksym", "1234567890", "2", "kb-231")
        updateElement("Maksym", "Jane", "9876543210", "2", "kb-231")
        self.assertEqual(students[0]["name"], "Jane")
        self.assertEqual(students[0]["phone"], "9876543210")

    def test_loadDataFromCsv(self):
        test_csv = "test_lab2.csv"
        with open(test_csv, "w") as f:
            f.write("name,phone,kurs,group\n")
            f.write("Maksym,1234567890,2,kb-231\n")
        loadDataFromCsv(test_csv)
        self.assertEqual(len(students), 1)
        self.assertEqual(students[0]["name"], "Maksym")

    def test_saveDataToCsv(self):
        test_csv = "test_output.csv"
        addNewElement("Maksym", "1234567890", "2", "kb-231")
        saveDataToCsv(test_csv)
        with open(test_csv, "r") as f:
            lines = f.readlines()
        self.assertEqual(len(lines), 2) 

if __name__ == "__main__":
    unittest.main()