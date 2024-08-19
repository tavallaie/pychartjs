# tests/test_colors.py

import unittest
from pychartjs.colors import ColorScheme
from pychartjs.datasets import Dataset


class TestColorScheme(unittest.TestCase):
    def test_color_scheme_application(self):
        datasets = [
            Dataset(label="Dataset 1", data=[10, 20, 30]),
            Dataset(label="Dataset 2", data=[15, 25, 35]),
            Dataset(label="Dataset 3", data=[20, 30, 40]),
            Dataset(label="Dataset 4", data=[25, 35, 45]),
            Dataset(label="Dataset 5", data=[30, 40, 50]),
            Dataset(label="Dataset 6", data=[35, 45, 55]),
            Dataset(label="Dataset 7", data=[40, 50, 60]),
            Dataset(label="Dataset 8", data=[45, 55, 65]),
        ]

        color_scheme = ColorScheme(
            backgroundColors=[
                "rgba(255, 99, 132, 0.2)",
                "rgba(54, 162, 235, 0.2)",
                "rgba(255, 206, 86, 0.2)",
                "rgba(75, 192, 192, 0.2)",
                "rgba(153, 102, 255, 0.2)",
                "rgba(255, 159, 64, 0.2)",
                "rgba(199, 199, 199, 0.2)",
            ],
            borderColors=[
                "rgba(255, 99, 132, 1)",
                "rgba(54, 162, 235, 1)",
                "rgba(255, 206, 86, 1)",
                "rgba(75, 192, 192, 1)",
                "rgba(153, 102, 255, 1)",
                "rgba(255, 159, 64, 1)",
                "rgba(199, 199, 199, 1)",
            ],
        )

        color_scheme.apply_to_datasets(datasets)

        self.assertEqual(datasets[0].backgroundColor, "rgba(255, 99, 132, 0.2)")
        self.assertEqual(datasets[7].backgroundColor, "rgba(255, 99, 132, 0.2)")
        self.assertEqual(datasets[1].backgroundColor, "rgba(54, 162, 235, 0.2)")
        self.assertEqual(datasets[7].borderColor, "rgba(255, 99, 132, 1)")


if __name__ == "__main__":
    unittest.main()
