import unittest
from StudentList import StudentList
from Student import Student

class TestStudentList(unittest.TestCase):
    def setUp(self):
        self.student_list = StudentList()
        self.student = Student(name="Ivan", phone="123456789", kurs="1", group="kb-241")
        self.student_list.addNewElement(self.student)

    def test_add_student(self):
        self.assertEqual(len(self.student_list.students), 1)
        self.assertEqual(self.student_list.students[0].name, "Ivan")

    def test_remove_student(self):
        self.student_list.deleteElement("Ivan")
        self.assertEqual(len(self.student_list.students), 0)

    def test_remove_student_not_found(self):
        self.student_list.deleteElement("Zahar")
        self.assertEqual(len(self.student_list.students), 1)

    def test_update_student(self):
        self.student_list.updateElement("Ivan", name1="Ivan1", phone1="111111", kurs1="2", group1="kb-232")
        updated_student = self.student_list.students[0]
        self.assertEqual(updated_student.name, "Ivan1")
        self.assertEqual(updated_student.phone, "111111")

    def test_update_student_not_found(self):
        self.student_list.updateElement("Zahar", name1="Zahar1", phone1=None, kurs1=None, group1=None)
        self.assertEqual(len(self.student_list.students), 1)
        self.assertEqual(self.student_list.students[0].name, "Ivan")

if __name__ == "__main__":
    unittest.main()
