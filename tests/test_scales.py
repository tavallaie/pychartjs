import unittest
from pychartjs.scales import LinearScale, LogarithmicScale, TimeScale, GridLines
from pychartjs.enums import ScaleType, Position


class TestScales(unittest.TestCase):
    def test_linear_scale(self):
        scale = LinearScale(
            scale_type=ScaleType.LINEAR,
            display=True,
            position=Position.LEFT,
            gridLines=GridLines(color="rgba(0, 0, 0, 0.1)", lineWidth=1),
            beginAtZero=True,
            min=0,
            max=100,
            stepSize=10,
        )
        scale_dict = scale.to_dict()
        self.assertEqual(scale_dict["type"], "linear")
        self.assertTrue(scale_dict["display"])
        self.assertEqual(scale_dict["position"], "left")
        self.assertTrue(scale_dict["gridLines"]["color"], "rgba(0, 0, 0, 0.1)")
        self.assertTrue(scale_dict["beginAtZero"])

    def test_logarithmic_scale(self):
        scale = LogarithmicScale(scale_type=ScaleType.LOGARITHMIC, min=1, max=1000)
        scale_dict = scale.to_dict()
        self.assertEqual(scale_dict["type"], "logarithmic")
        self.assertEqual(scale_dict["min"], 1)
        self.assertEqual(scale_dict["max"], 1000)

    def test_time_scale(self):
        scale = TimeScale(
            scale_type=ScaleType.TIME,
            time_format="%Y-%m-%d",
            tooltipFormat="ll",
            unit="month",
            stepSize=1,
            displayFormats={"month": "MMM YYYY"},
        )
        scale_dict = scale.to_dict()
        self.assertEqual(scale_dict["type"], "time")
        self.assertEqual(scale_dict["time"]["parser"], "%Y-%m-%d")
        self.assertEqual(scale_dict["time"]["tooltipFormat"], "ll")
        self.assertEqual(scale_dict["time"]["unit"], "month")
        self.assertEqual(scale_dict["time"]["displayFormats"]["month"], "MMM YYYY")


if __name__ == "__main__":
    unittest.main()
