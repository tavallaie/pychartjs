from dataclasses import dataclass
from typing import List


@dataclass
class ColorScheme:
    backgroundColors: List[str]
    borderColors: List[str]

    def apply_to_datasets(self, datasets: List):
        num_colors = len(self.backgroundColors)
        for i, dataset in enumerate(datasets):
            # Rotate the color scheme if there are more datasets than colors
            dataset.backgroundColor = self.backgroundColors[i % num_colors]
            dataset.borderColor = self.borderColors[i % num_colors]


# Example color scheme with at least seven colors
basic_color_scheme = ColorScheme(
    backgroundColors=[
        "rgba(255, 99, 132, 0.2)",  # Red
        "rgba(54, 162, 235, 0.2)",  # Blue
        "rgba(255, 206, 86, 0.2)",  # Yellow
        "rgba(75, 192, 192, 0.2)",  # Green
        "rgba(153, 102, 255, 0.2)",  # Purple
        "rgba(255, 159, 64, 0.2)",  # Orange
        "rgba(199, 199, 199, 0.2)",  # Grey
    ],
    borderColors=[
        "rgba(255, 99, 132, 1)",  # Red
        "rgba(54, 162, 235, 1)",  # Blue
        "rgba(255, 206, 86, 1)",  # Yellow
        "rgba(75, 192, 192, 1)",  # Green
        "rgba(153, 102, 255, 1)",  # Purple
        "rgba(255, 159, 64, 1)",  # Orange
        "rgba(199, 199, 199, 1)",  # Grey
    ],
)
