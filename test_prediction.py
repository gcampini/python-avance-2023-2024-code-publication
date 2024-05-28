import unittest
import pandas as pd
from sales_prediction.prediction import train_model, predict_sales


class TestSalesPrediction(unittest.TestCase):

    def setUp(self):
        self.data = pd.DataFrame(
            {
                "date": pd.to_datetime(["2023-01-01", "2023-01-01", "2023-01-02"]),
                "revenue": [50, 45, 70],
            }
        )

    def test_train_model(self):
        model = train_model(self.data)
        self.assertIsNotNone(model)

    def test_predict_sales(self):
        model = train_model(self.data)
        new_data = pd.DataFrame({"date": pd.to_datetime(["2023-02-01", "2023-02-02"])})
        predictions = predict_sales(model, new_data)
        self.assertEqual(len(predictions), len(new_data))


if __name__ == "__main__":
    unittest.main()
