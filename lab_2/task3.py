import unittest
from task1_t import students_list, add_new_element, delete_element, update_element

class TestStudentDirectory(unittest.TestCase):
    def setUp(self):
        students_list = [
    {"name": "Bob", "phone": "0631234567", "kurs": "2", "group": "kb-231"},
    {"name": "Emma", "phone": "0631234567", "kurs": "3", "group": "kb-222"},
    {"name": "Jon", "phone": "0631234567", "kurs": "2", "group": "kb-232"},
    {"name": "Zak", "phone": "0631234567", "kurs": "3", "group": "kb-221"}
]

    def test_add_new_element(self):
        add_new_element({"name": "Charlie", "phone": "5555555555", "kurs": "3", "group": "kb-303"})
        self.assertEqual(len(students_list), 5)

    def test_delete_element(self):
        delete_element("Zak")
        self.assertEqual(len(students_list), 4)
        self.assertNotIn({"name": "Zak", "phone": "0631234567", "kurs": "3", "group": "kb-221"}, students_list)

    def test_update_element(self):
        update_element("Bob", {"name": "Bobby", "phone": "1111111111", "kurs": "2", "group": "kb-231"})
        self.assertEqual(students_list[0]["name"], "Bobby")

if __name__ == "__main__":
    unittest.main()