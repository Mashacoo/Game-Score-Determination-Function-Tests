import random
from unittest import TestCase
from ..core_task import get_score, generate_game


class GetScoreTestCase(TestCase):

    TESTS_QUANTITY = 20

    @classmethod
    def setUpClass(cls):
        cls.test_data = generate_game()

    def test_offset_exists(self):
        test_info = random.sample(self.test_data, self.TESTS_QUANTITY)

        for line in test_info:
            with self.subTest():
                result = get_score(self.test_data, line['offset'])

                self.assertIn(str(line['offset']), result)
                self.assertIn(str(line['score']["away"]), result)
                self.assertIn(str(line['score']["home"]), result)

    def test_offset_does_not_exist(self):

        test_info = []  # list of offset values that does not exist

        for _ in range(self.TESTS_QUANTITY):
            element_exist = random.choice(self.test_data)
            index_exist = self.test_data.index(element_exist)
            right_element = self.test_data[index_exist+1]
            left_element = self.test_data[index_exist-1]

            if right_element['offset'] - element_exist['offset'] >= 2:
                test_info.append({"offset": element_exist['offset'] + 1})
            if element_exist['offset']-left_element['offset'] >= 2:
                test_info.append({"offset": element_exist['offset'] - 1})

        for line in test_info:
            with self.subTest():
                result = get_score(self.test_data, line['offset'])

                self.assertIn(str(line['offset']), result)
                self.assertIn('Try again', result)
