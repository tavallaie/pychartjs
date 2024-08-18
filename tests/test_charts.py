import unittest
from pychartjs.charts import Chart
from pychartjs.datasets import Dataset
from pychartjs.enums import ChartType
from pychartjs.options import ChartOptions, Legend


class TestChart(unittest.TestCase):
    def test_chart_creation(self):
        chart = Chart(
            chart_type=ChartType.BAR,
            datasets=[Dataset(label="Test Dataset", data=[10, 20, 30])],
            labels=["Jan", "Feb", "Mar"],
        )
        self.assertEqual(chart.chart_type, ChartType.BAR)
        self.assertEqual(len(chart.datasets), 1)
        self.assertEqual(chart.datasets[0].label, "Test Dataset")

    def test_chart_render(self):
        chart = Chart(
            chart_type=ChartType.LINE,
            datasets=[Dataset(label="Test Dataset", data=[10, 20, 30])],
            labels=["Jan", "Feb", "Mar"],
        )
        rendered_html = chart.render()
        self.assertIn('<canvas id="', rendered_html)
        self.assertIn("</canvas>", rendered_html)


if __name__ == "__main__":
    unittest.main()
