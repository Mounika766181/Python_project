import unittest
from utils import calculate_overlap, compute_scores


class TestUtils(unittest.TestCase):
    def test_calculate_overlap(self):
        self.assertEqual(calculate_overlap("2020-01-01", "2020-12-31", "2020-06-01", "2021-01-01"), 213)
        self.assertEqual(calculate_overlap("2020-01-01", "2020-06-01", "2020-07-01", "2020-12-01"), 0)

    def test_compute_scores(self):
        sample_data = [
            {
                "first": "John",
                "last": "Doe",
                "experience": [{"company": "ABC Corp", "start": "2020-01-01", "end": "2021-01-01"}]
            },
            {
                "first": "Jane",
                "last": "Smith",
                "experience": [{"company": "ABC Corp", "start": "2020-06-01", "end": None}]
            }
        ]
        results = compute_scores(sample_data)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0][0], "John Doe")
        self.assertEqual(results[0][1], "Jane Smith")
