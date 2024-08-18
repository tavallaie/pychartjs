import unittest
from pychartjs.plugins import Plugin, DecimationOptions


class TestPlugin(unittest.TestCase):
    def test_plugin_creation(self):
        plugin = Plugin(plugin_name="testPlugin", options={"option1": True})
        plugin_dict = plugin.to_dict()
        self.assertEqual(plugin_dict["plugin_name"], "testPlugin")
        self.assertEqual(plugin_dict["options"]["option1"], True)

    def test_decimation_options(self):
        decimation = DecimationOptions(enabled=False, algorithm="min-max", samples=500)
        decimation_dict = decimation.to_dict()
        self.assertFalse(decimation_dict["enabled"])
        self.assertEqual(decimation_dict["algorithm"], "min-max")
        self.assertEqual(decimation_dict["samples"], 500)


if __name__ == "__main__":
    unittest.main()
