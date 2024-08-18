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
        """Render the Chart.js component as an HTML string."""
        chart_data = {
            "type": self.chart_type.value if self.chart_type else None,
            "data": {
                "labels": self.labels,
                "datasets": [dataset.to_dict() for dataset in self.datasets],
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
        <script>
        var ctx = document.getElementById('{self.id}').getContext('2d');
        new Chart(ctx, {chart_data_json});
        </script>
        """
        self.add_custom_script(chart_script)

        return f'<canvas id="{self.id}"></canvas>' + self.render_custom_scripts()
