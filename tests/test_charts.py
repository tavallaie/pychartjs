import unittest
from pychartjs.charts import Chart
from pychartjs.datasets import Dataset
from pychartjs.enums import ChartType
from pychartjs.options import ChartOptions, Legend, Title, Tooltip, Animation


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
        self.assertEqual(chart.labels, ["Jan", "Feb", "Mar"])

    def test_chart_render_basic(self):
        chart = Chart(
            chart_type=ChartType.LINE,
            datasets=[Dataset(label="Test Dataset", data=[10, 20, 30])],
            labels=["Jan", "Feb", "Mar"],
        )
        rendered_html = chart.render()
        self.assertIn('<canvas id="', rendered_html)
        self.assertIn("</canvas>", rendered_html)
        self.assertIn("new Chart(", rendered_html)

    def test_chart_render_with_options(self):
        chart = Chart(
            chart_type=ChartType.LINE,
            datasets=[Dataset(label="Test Dataset", data=[10, 20, 30])],
            labels=["Jan", "Feb", "Mar"],
            options=ChartOptions(
                responsive=False,
                legend=Legend(display=False),
                title=Title(display=True, text="Test Title"),
                tooltip=Tooltip(enabled=True),
                animation=Animation(duration=500),
            ),
        )
        rendered_html = chart.render()
        self.assertIn("new Chart(", rendered_html)
        self.assertIn('"responsive": false', rendered_html)
        self.assertIn('"display": false', rendered_html)  # Legend
        self.assertIn('"text": "Test Title"', rendered_html)  # Title
        self.assertIn('"duration": 500', rendered_html)  # Animation

    def test_chart_with_context(self):
        context = {"year": "2023", "month": "April"}
        chart = Chart(
            chart_type=ChartType.LINE,
            datasets=[Dataset(label="Sales Data {year}", data=[10, 20, 30])],
            labels=["Jan", "Feb", "{month}"],
        )
        rendered_html = chart.render(context=context)
        self.assertIn("Sales Data 2023", rendered_html)  # Check dataset label context
        self.assertIn('["Jan", "Feb", "April"]', rendered_html)  # Check labels context

    def test_chart_multiple_datasets(self):
        chart = Chart(
            chart_type=ChartType.BAR,
            datasets=[
                Dataset(label="Dataset 1", data=[10, 20, 30]),
                Dataset(label="Dataset 2", data=[15, 25, 35]),
            ],
            labels=["Jan", "Feb", "Mar"],
        )
        rendered_html = chart.render()
        self.assertIn('"label": "Dataset 1"', rendered_html)
        self.assertIn('"label": "Dataset 2"', rendered_html)
        self.assertIn('"data": [10, 20, 30]', rendered_html)
        self.assertIn('"data": [15, 25, 35]', rendered_html)

    def test_chart_with_custom_scripts(self):
        chart = Chart(
            chart_type=ChartType.LINE,
            datasets=[Dataset(label="Test Dataset", data=[10, 20, 30])],
            labels=["Jan", "Feb", "Mar"],
        )
        chart.add_custom_script("console.log('Custom Script');")
        rendered_html = chart.render()
        self.assertIn("<script>", rendered_html)
        self.assertIn("console.log('Custom Script');", rendered_html)

    def test_chart_render_with_mixed_types(self):
        chart = Chart(
            datasets=[
                Dataset(
                    label="Dataset 1",
                    data=[10, 20, 30],
                    backgroundColor="rgba(255, 99, 132, 0.2)",
                    borderColor="rgba(255, 99, 132, 1)",
                ),
                Dataset(
                    label="Dataset 2",
                    data=[15, 25, 35],
                    backgroundColor="rgba(54, 162, 235, 0.2)",
                    borderColor="rgba(54, 162, 235, 1)",
                ),
            ],
            labels=["Jan", "Feb", "Mar"],
        )
        rendered_html = chart.render()
        self.assertIn('"backgroundColor": "rgba(255, 99, 132, 0.2)"', rendered_html)
        self.assertIn('"borderColor": "rgba(54, 162, 235, 1)"', rendered_html)


if __name__ == "__main__":
    unittest.main()
