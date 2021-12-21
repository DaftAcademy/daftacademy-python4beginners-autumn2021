import unittest

from task_1 import (
    check_xkom_hotshot,
    get_matching_keywords,
    get_xkom_hotshot_product_data,
)
from task_1_solution import check_xkom_hotshot as check_xkom_hotshot_solution
from task_1_solution import (
    get_xkom_hotshot_product_data as get_xkom_hotshot_product_data_solution,
)


class TestXkomHotshot(unittest.TestCase):
    def test_get_xkom_hotshot_product_data(self):
        expected_result = get_xkom_hotshot_product_data_solution()
        result = get_xkom_hotshot_product_data()

        self.assertEqual(expected_result, result)

    def test_get_matching_keywords(self):
        TEST_CASES = (
            (
                {"placki"},
                {"keywords": {"orzeszki", "placki"}, "name": "Bardzo lubie placki"},
            ),
            (
                {"orzeszki", "placki"},
                {
                    "keywords": {"orzeszki", "placki"},
                    "name": "Bardzo lubie placki&orzeszki",
                },
            ),
            (
                {"orzeszki", "placki"},
                {
                    "keywords": {"orzeszki", "placki"},
                    "name": "Bardzo lubie Placki&OrzeszKi",
                },
            ),
            (
                set(),
                {
                    "keywords": {"orzeszki", "placki"},
                    "name": "Bardzo lubie owoce oraz warzywa",
                },
            ),
            (
                set(),
                {
                    "keywords": set(),
                    "name": "Bardzo lubie owoce oraz warzywa",
                },
            ),
            (
                set(),
                {
                    "keywords": {"nie pasuje"},
                    "name": "Bardzo lubie owoce oraz warzywa",
                },
            ),
            (
                set(),
                {
                    "keywords": set(),
                    "name": "",
                },
            ),
        )

        for test_case in TEST_CASES:
            expected_result, kwargs = test_case

            self.assertEqual(get_matching_keywords(**kwargs), expected_result)

    def test_check_xkom_hotshot(self):
        expected_result = check_xkom_hotshot_solution({"samsung", "nokia", "asus"})
        result = check_xkom_hotshot({"samsung", "nokia", "asus"})

        self.assertEqual(expected_result, result)
