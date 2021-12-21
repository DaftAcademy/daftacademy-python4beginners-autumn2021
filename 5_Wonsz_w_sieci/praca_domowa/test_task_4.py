import time
import unittest

from task_4 import get_recepie_links
from task_4_solution import get_recepie_links as get_recepie_links_solution


class TestGetRecepieLinks(unittest.TestCase):

    TEST_KEYWORDS = ["placki", "ciasto", "kotlety", "schabowe"]

    def test_get_pair_candles(self):

        for keyword in self.TEST_KEYWORDS:
            time.sleep(0.5)

            expected_result = get_recepie_links_solution(keyword=keyword)
            result = get_recepie_links(keyword=keyword)

            self.assertEqual(result, expected_result)
