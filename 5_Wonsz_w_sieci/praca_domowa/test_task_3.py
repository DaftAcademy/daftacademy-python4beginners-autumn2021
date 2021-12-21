import unittest

from task_3 import get_daftcode_contact_info
from task_3_solution import Contact


class TestDaftcodeContactInfo(unittest.TestCase):
    def test_get_daftcode_contact_info(self):
        expected_result = Contact(
            email="hello@daftcode.pl",
            phone="+48 22 100 55 58",
            address="Plac Europejski 1, 00-844 Warszawa",
            instagram="https://www.instagram.com/daftcode/",
        )

        self.assertEqual(get_daftcode_contact_info(), expected_result)
