from dataclasses import dataclass, field
from typing import List, Dict, Optional
from pychartjs.datasets import Dataset
from pychartjs.scales import Scale
from pychartjs.options import ChartOptions
from pychartjs.plugins import Plugin
from pychartjs.enums import ChartType
from trunco import Component


@dataclass
class Chart(Component):
    chart_type: Optional[ChartType] = None  # Allow None for mixed types
    datasets: List[Dataset] = field(default_factory=list)
    options: Optional[ChartOptions] = field(default_factory=ChartOptions)
    labels: List[str] = field(default_factory=list)
    scales: List[Scale] = field(default_factory=list)
    plugins: List[Plugin] = field(default_factory=list)

    def render(self, context: Optional[Dict] = None) -> str:
        """Render the Chart.js component as an HTML string, with context substitution."""
        # Apply context substitution to labels and datasets
        if context:
            rendered_labels = [label.format(**context) for label in self.labels]
            rendered_datasets = [
                Dataset(
                    label=dataset.label.format(**context),
                    data=dataset.data,
                    backgroundColor=dataset.backgroundColor,
                    borderColor=dataset.borderColor,
                    borderWidth=dataset.borderWidth,
                    fill=dataset.fill,
                    order=dataset.order,
                    tension=dataset.tension,
                    pointStyle=dataset.pointStyle,
                    hoverBackgroundColor=dataset.hoverBackgroundColor,
                    steppedLine=dataset.steppedLine,
                    pointRadius=dataset.pointRadius,
                    pointHoverRadius=dataset.pointHoverRadius,
                    pointHoverBackgroundColor=dataset.pointHoverBackgroundColor,
                ).to_dict()
                for dataset in self.datasets
            ]
        else:
            rendered_labels = self.labels
            rendered_datasets = [dataset.to_dict() for dataset in self.datasets]

        chart_data = {
            "type": self.chart_type.value if self.chart_type else None,
            "data": {
                "labels": rendered_labels,
                "datasets": rendered_datasets,
            },
            "options": self.options.to_dict(),
            "plugins": [plugin.to_dict() for plugin in self.plugins],
            "scales": {
                scale.scale_type.value: scale.to_dict() for scale in self.scales
            },
        }

        import json

        chart_data_json = json.dumps(chart_data)

        chart_script = f"""
        var ctx = document.getElementById('{self.id}').getContext('2d');
        new Chart(ctx, {chart_data_json});
        """

        self.add_custom_script(chart_script)

        return f'<canvas id="{self.id}"></canvas>' + self.render_custom_scripts()
