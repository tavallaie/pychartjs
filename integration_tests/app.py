import sys
import os

# Add the root directory of the project to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from dataclasses import dataclass, field
from typing import List
from robyn import Robyn
from robyn.templating import JinjaTemplate
from pychartjs.charts import Chart
from pychartjs.datasets import Dataset
from pychartjs.enums import ChartType
from pychartjs.options import ChartOptions, Legend
from trunco import Component

app = Robyn(__file__)

# Configure the template engine
template = JinjaTemplate(os.path.join(os.path.dirname(__file__), "templates"))


@dataclass
class Page(Component):
    charts: List[Chart] = field(default_factory=list)

    def __post_init__(self):
        # Add all chart types to the page
        self.charts.extend(
            [
                self.create_chart(ChartType.LINE, "Line"),
                self.create_chart(ChartType.BAR, "Bar"),
                self.create_chart(ChartType.PIE, "Pie"),
                self.create_chart(ChartType.DOUGHNUT, "Doughnut"),
                self.create_chart(ChartType.RADAR, "Radar"),
                self.create_chart(ChartType.POLAR_AREA, "PolarArea"),
                self.create_chart(ChartType.BUBBLE, "Bubble"),
                self.create_chart(ChartType.SCATTER, "Scatter"),
            ]
        )

    def create_chart(self, chart_type: ChartType, name: str) -> Chart:
        dataset = Dataset(
            label=f"{name} Sales Data {{year}}",
            data=[10, 20, 30, 40, 50],
            backgroundColor="rgba(75, 192, 192, 0.2)",
            borderColor="rgba(75, 192, 192, 1)",
            borderWidth=1,
        )

        return Chart(
            chart_type=chart_type,
            datasets=[dataset],
            labels=["January", "February", "March", "April", "May"],
            options=ChartOptions(responsive=True, legend=Legend(display=True)),
        )

    def render(self, context=None):
        # Render all charts with the provided context
        rendered_charts = [chart.render(context) for chart in self.charts]

        # Combine all rendered chart HTML into a single string
        combined_html = "\n".join(rendered_charts)

        return combined_html


@app.get("/")
async def chart_page(request):
    # Create the page with all chart types
    page = Page()

    # Render the charts HTML with context
    context = {"year": "2023"}
    charts_html = page.render(context=context)

    # Debug output to verify HTML content
    print("Generated charts_html:\n", charts_html)

    # Directly return the rendered template with charts_html
    return template.render_template("index.html", charts_html=charts_html)


# Run the app
if __name__ == "__main__":
    app.start(host="0.0.0.0", port=8080)
