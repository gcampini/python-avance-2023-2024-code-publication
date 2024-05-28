import unittest
import pandas as pd
from data_analysis.analysis import compute_statistics


class TestDataAnalysis(unittest.TestCase):

    def setUp(self):
        self.data = pd.DataFrame(
            {
                "date": pd.to_datetime(["2023-01-01", "2023-01-01", "2023-01-02"]),
                "revenue": [50, 45, 70],
            }
        )

    def test_compute_statistics(self):
        stats = compute_statistics(self.data)
        self.assertIn("mean", stats.index)
        self.assertEqual(stats.loc["mean", "revenue"], 55.0)


if __name__ == "__main__":
    unittest.main()
