import unittest
import pandas as pd
from data_processing.processing import load_data, clean_data, extract_features


class TestDataProcessing(unittest.TestCase):

    def setUp(self):
        self.data = pd.DataFrame(
            {
                "date": ["2023-01-01", "2023-01-01", "2023-01-02"],
                "product": ["Product A", "Product B", "Product A"],
                "price": [10.0, 15.0, 10.0],
                "quantity": [5, 3, 7],
            }
        )

    def test_load_data(self):
        data = load_data("test_sales_data.csv")  # this file must be created in the same directory as the test file
        self.assertIsInstance(data, pd.DataFrame)

    def test_clean_data(self):
        cleaned_data = clean_data(self.data.copy())
        self.assertFalse(cleaned_data.isnull().values.any())

    def test_extract_features(self):
        cleaned_data = clean_data(self.data.copy())
        features = extract_features(cleaned_data)
        self.assertIn("revenue", features.columns)
        self.assertEqual(features["revenue"].sum(), 165)


if __name__ == "__main__":
    unittest.main()
