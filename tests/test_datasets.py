# tests/test_datasets.py

import unittest
from pychartjs.datasets import Dataset


class TestDataset(unittest.TestCase):
    def test_dataset_creation(self):
        dataset = Dataset(
            label="Sales",
            data=[10, 20, 30],
            backgroundColor="rgba(255, 99, 132, 0.2)",
            borderColor="rgba(255, 99, 132, 1)",
            borderWidth=2,
            fill=True,
            order=1,
            tension=0.4,
            pointStyle="circle",
            hoverBackgroundColor="rgba(255, 99, 132, 0.4)",
            steppedLine=False,
            pointRadius=5,
            pointHoverRadius=7,
            pointHoverBackgroundColor="rgba(255, 99, 132, 0.6)",
        )
        self.assertEqual(dataset.label, "Sales")
        self.assertEqual(dataset.data, [10, 20, 30])
        self.assertEqual(dataset.backgroundColor, "rgba(255, 99, 132, 0.2)")
        self.assertEqual(dataset.borderColor, "rgba(255, 99, 132, 1)")
        self.assertEqual(dataset.borderWidth, 2)
        self.assertTrue(dataset.fill)
        self.assertEqual(dataset.order, 1)
        self.assertEqual(dataset.tension, 0.4)
        self.assertEqual(dataset.pointStyle, "circle")
        self.assertEqual(dataset.hoverBackgroundColor, "rgba(255, 99, 132, 0.4)")
        self.assertFalse(dataset.steppedLine)
        self.assertEqual(dataset.pointRadius, 5)
        self.assertEqual(dataset.pointHoverRadius, 7)
        self.assertEqual(dataset.pointHoverBackgroundColor, "rgba(255, 99, 132, 0.6)")

    def test_dataset_to_dict(self):
        dataset = Dataset(label="Revenue", data=[100, 200, 300])
        dataset_dict = dataset.to_dict()
        self.assertEqual(dataset_dict["label"], "Revenue")
        self.assertEqual(dataset_dict["data"], [100, 200, 300])
        self.assertIsNone(dataset_dict.get("backgroundColor"))
        self.assertIsNone(dataset_dict.get("borderColor"))

    def test_dataset_with_partial_data(self):
        dataset = Dataset(
            label="Profit",
            data=[50, 150, 250],
            backgroundColor="rgba(75, 192, 192, 0.2)",
        )
        dataset_dict = dataset.to_dict()
        self.assertEqual(dataset_dict["label"], "Profit")
        self.assertEqual(dataset_dict["data"], [50, 150, 250])
        self.assertEqual(dataset_dict["backgroundColor"], "rgba(75, 192, 192, 0.2)")
        self.assertIsNone(dataset_dict.get("borderColor"))


if __name__ == "__main__":
    unittest.main()
