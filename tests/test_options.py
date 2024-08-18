# tests/test_options.py

import unittest
from pychartjs.options import (
    ChartOptions,
    Legend,
    Tooltip,
    Title,
    Animation,
    Layout,
    Interaction,
)
from pychartjs.enums import Position, InteractionMode, AnimationEasing


class TestChartOptions(unittest.TestCase):
    def test_legend_creation(self):
        legend = Legend(
            display=False, position=Position.BOTTOM, labels={"color": "blue"}
        )
        self.assertFalse(legend.display)
        self.assertEqual(legend.position, Position.BOTTOM)
        self.assertEqual(legend.labels, {"color": "blue"})

    def test_tooltip_creation(self):
        tooltip = Tooltip(enabled=False, mode=InteractionMode.INDEX, intersect=False)
        self.assertFalse(tooltip.enabled)
        self.assertEqual(tooltip.mode, InteractionMode.INDEX)
        self.assertFalse(tooltip.intersect)

    def test_title_creation(self):
        title = Title(display=True, text="Sales Chart", position=Position.TOP)
        self.assertTrue(title.display)
        self.assertEqual(title.text, "Sales Chart")
        self.assertEqual(title.position, Position.TOP)

    def test_animation_creation(self):
        animation = Animation(duration=500, easing=AnimationEasing.EASE_IN_OUT_QUAD)
        self.assertEqual(animation.duration, 500)
        self.assertEqual(animation.easing, AnimationEasing.EASE_IN_OUT_QUAD)

    def test_layout_creation(self):
        layout = Layout(padding={"left": 10, "right": 10})
        self.assertEqual(layout.padding, {"left": 10, "right": 10})

    def test_interaction_creation(self):
        interaction = Interaction(mode=InteractionMode.DATASET, intersect=True)
        self.assertEqual(interaction.mode, InteractionMode.DATASET)
        self.assertTrue(interaction.intersect)

    def test_chart_options_creation(self):
        options = ChartOptions(
            responsive=False,
            maintainAspectRatio=False,
            legend=Legend(display=True, position=Position.RIGHT),
            tooltip=Tooltip(enabled=True, mode=InteractionMode.POINT),
            title=Title(display=True, text="Revenue Chart"),
            animation=Animation(duration=1000, easing=AnimationEasing.EASE_OUT_CUBIC),
            layout=Layout(padding={"left": 20, "right": 20}),
            interaction=Interaction(mode=InteractionMode.X, intersect=False),
        )
        self.assertFalse(options.responsive)
        self.assertFalse(options.maintainAspectRatio)
        self.assertTrue(options.legend.display)
        self.assertEqual(options.legend.position, Position.RIGHT)
        self.assertTrue(options.tooltip.enabled)
        self.assertEqual(options.tooltip.mode, InteractionMode.POINT)
        self.assertTrue(options.title.display)
        self.assertEqual(options.title.text, "Revenue Chart")
        self.assertEqual(options.animation.duration, 1000)
        self.assertEqual(options.animation.easing, AnimationEasing.EASE_OUT_CUBIC)
        self.assertEqual(options.layout.padding, {"left": 20, "right": 20})
        self.assertEqual(options.interaction.mode, InteractionMode.X)
        self.assertFalse(options.interaction.intersect)

    def test_options_to_dict(self):
        options = ChartOptions(responsive=False)
        options_dict = options.to_dict()
        self.assertFalse(options_dict["responsive"])
        self.assertIn("legend", options_dict)
        self.assertIn("tooltip", options_dict)
        self.assertIn("title", options_dict)
        self.assertIn("animation", options_dict)
        self.assertIn("layout", options_dict)
        self.assertIn("interaction", options_dict)


if __name__ == "__main__":
    unittest.main()
