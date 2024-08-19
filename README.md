 # Pychartjs

 Pychartjs is a Python library for generating dynamic charts using Chart.js and integrating them into web applications. The library is built on top of the [Trunco](https://github.com/tavallaie/trunco) framework, which provides a component-based architecture to make it easy to create and manage various chart types.

 ## Features

 - Support for all major chart types: Line, Bar, Pie, Doughnut, Radar, PolarArea, Bubble, and Scatter.
 - Integration with various web frameworks including Robyn, Django, FastAPI, and other Python web frameworks.
 - Dynamic chart rendering with context variables.
 - Flexible and customizable chart options.

 ## Project Structure

 ```
 pychartjs/
 ├── pychartjs/
 │   ├── __init__.py
 │   ├── charts.py
 │   ├── datasets.py
 │   ├── enums.py
 │   ├── options.py
 │   ├── scales.py
 │   ├── plugins.py
 │   ├── colors.py
 ├── tests/
 │   ├── test_charts.py
 │   ├── test_datasets.py
 │   ├── test_options.py
 │   ├── test_scales.py
 │   ├── test_plugins.py
 │   ├── test_colors.py
 ├── integration_tests/
 │   ├── app.py
 │   └── templates/
 │       └── index.html
 ├── LICENSE
 ├── README.md
 ├── poetry.lock
 └── pyproject.toml
 ```

 - **`pychartjs/`**: Contains the core library code, including charts, datasets, enums, options, and scales.
 - **`tests/`**: Unit tests for the various components of the library.
 - **`integration_tests/`**: A sample application that demonstrates how to integrate `pychartjs` with a web framework like Robyn.

 ## Installation

 1. **Install with Poetry:**

    If you are using Poetry for dependency management, you can add `pychartjs` to your project with:

    ```bash
    poetry add pychartjs
    ```

 2. **Alternatively, install with pip:**

    If you're using pip, you can install `pychartjs` with:

    ```bash
    pip install pychartjs
    ```


 ## Table of Contents
 1. [Installation](#installation)
 2. [Basic Usage](#basic-usage)
 3. [Integration with Web Frameworks](#integration-with-web-frameworks)
    - [Robyn](#robyn)
    - [Django](#django)
    - [FastAPI](#fastapi)
    - [Flask](#flask)
 4. [Customizing Your Charts](#customizing-your-charts)
 5. [Working with Options](#working-with-options)
 6. [Using Plugins](#using-plugins)
 7. [Color Schemes and Palettes](#color-schemes-and-palettes)
 8. [Rendering Options](#rendering-options)
 9. [Advanced Features](#advanced-features)
 10. [Contributing](#contributing)

 ## Installation

 ### Poetry

 To install `pychartjs` using Poetry, run the following command:

 ```bash
 poetry add pychartjs
 ```

 ### Pip

 Alternatively, if you're using pip, you can install `pychartjs` with:

 ```bash
 pip install pychartjs
 ```

 ## Basic Usage

 Here’s a simple example of how to create a line chart using `pychartjs`:

 ```python
 from pychartjs.charts import Chart
 from pychartjs.datasets import Dataset
 from pychartjs.enums import ChartType

 dataset = Dataset(
     label="Sales Data",
     data=[10, 20, 30, 40, 50],
     backgroundColor="rgba(75, 192, 192, 0.2)",
     borderColor="rgba(75, 192, 192, 1)",
     borderWidth=1,
 )

 chart = Chart(
     chart_type=ChartType.LINE,
     datasets=[dataset],
     labels=["January", "February", "March", "April", "May"]
 )

 # Render the chart as HTML
 chart_html = chart.render()
 print(chart_html)
 ```

 ## Integration with Web Frameworks

 ### Robyn

 Here’s how you can use `pychartjs` with the Robyn framework:

 ```python
 from robyn import Robyn
 from pychartjs.charts import Chart
 from pychartjs.datasets import Dataset
 from pychartjs.enums import ChartType
 from robyn.templating import JinjaTemplate

 app = Robyn(__file__)

 template = JinjaTemplate("templates")

 @app.get("/")
 async def get_chart(request):
     dataset = Dataset(
         label="Sales Data",
         data=[10, 20, 30, 40, 50],
         backgroundColor="rgba(75, 192, 192, 0.2)",
         borderColor="rgba(75, 192, 192, 1)",
         borderWidth=1,
     )
     chart = Chart(
         chart_type=ChartType.LINE,
         datasets=[dataset],
         labels=["January", "February", "March", "April", "May"]
     )
     charts_html = chart.render()
     return template.render_template("index.html", charts_html=charts_html)

 if __name__ == "__main__":
     app.start(port=8080)
 ```

 ### Django

 To integrate `pychartjs` with Django, follow these steps:

 1. **Install Django if you haven't already:**

    ```bash
    pip install django
    ```

 2. **Create a Django view and template:**

    ```python
    # views.py
    from django.shortcuts import render
    from pychartjs.charts import Chart
    from pychartjs.datasets import Dataset
    from pychartjs.enums import ChartType

    def chart_view(request):
        dataset = Dataset(
            label="Sales Data",
            data=[10, 20, 30, 40, 50],
            backgroundColor="rgba(75, 192, 192, 0.2)",
            borderColor="rgba(75, 192, 192, 1)",
            borderWidth=1,
        )
        chart = Chart(
            chart_type=ChartType.LINE,
            datasets=[dataset],
            labels=["January", "February", "March", "April", "May"]
        )
        charts_html = chart.render()
        return render(request, "chart.html", {"charts_html": charts_html})
    ```

 3. **Create the template:**

    ```html
    <!-- chart.html -->
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Chart Page</title>
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    </head>
    <body>
        <h1>My Sales Chart</h1>
        <div id="chart-container">
            {{ charts_html|safe }}
        </div>
    </body>
    </html>
    ```

 4. **Add the view to your `urls.py`:**

    ```python
    # urls.py
    from django.urls import path
    from .views import chart_view

    urlpatterns = [
        path('chart/', chart_view, name='chart-view'),
    ]
    ```

 ### FastAPI

 Here’s how to set up `pychartjs` with FastAPI:

 ```python
 from fastapi import FastAPI
 from fastapi.responses import HTMLResponse
 from pychartjs.charts import Chart
 from pychartjs.datasets import Dataset
 from pychartjs.enums import ChartType

 app = FastAPI()

 @app.get("/", response_class=HTMLResponse)
 async def get_chart():
     dataset = Dataset(
         label="Sales Data",
         data=[10, 20, 30, 40, 50],
         backgroundColor="rgba(75, 192, 192, 0.2)",
         borderColor="rgba(75, 192, 192, 1)",
         borderWidth=1,
     )
     chart = Chart(
         chart_type=ChartType.LINE,
         datasets=[dataset],
         labels=["January", "February", "March", "April", "May"]
     )
     charts_html = chart.render()
     return f"""
     <!DOCTYPE html>
     <html lang="en">
     <head>
         <meta charset="UTF-8">
         <meta name="viewport" content="width=device-width, initial-scale=1.0">
         <title>Chart Page</title>
         <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
     </head>
     <body>
         <h1>My Sales Chart</h1>
         <div id="chart-container">
             {charts_html}
         </div>
     </body>
     </html>
     """

 if __name__ == "__main__":
     import uvicorn
     uvicorn.run(app, host="0.0.0.0", port=8000)
 ```

 ### Flask

 To integrate `pychartjs` with Flask:

 1. **Install Flask if you haven't already:**

    ```bash
    pip install flask
    ```

 2. **Create a Flask app:**

    ```python
    from flask import Flask, render_template


    from pychartjs.charts import Chart
    from pychartjs.datasets import Dataset
    from pychartjs.enums import ChartType

    app = Flask(__name__)

    @app.route("/")
    def get_chart():
        dataset = Dataset(
            label="Sales Data",
            data=[10, 20, 30, 40, 50],
            backgroundColor="rgba(75, 192, 192, 0.2)",
            borderColor="rgba(75, 192, 192, 1)",
            borderWidth=1,
        )
        chart = Chart(
            chart_type=ChartType.LINE,
            datasets=[dataset],
            labels=["January", "February", "March", "April", "May"]
        )
        charts_html = chart.render()
        return render_template("chart.html", charts_html=charts_html)

    if __name__ == "__main__":
        app.run(debug=True)
    ```

 3. **Create the template:**

    ```html
    <!-- templates/chart.html -->
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Chart Page</title>
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    </head>
    <body>
        <h1>My Sales Chart</h1>
        <div id="chart-container">
            {{ charts_html|safe }}
        </div>
    </body>
    </html>
    ```

 ## Customizing Your Charts

 `pychartjs` allows you to customize various aspects of your charts, including colors, labels, tooltips, and more. For example, you can modify the background color and border color of your datasets or adjust the chart's options to change its appearance.

 ### Example: Customizing a Bar Chart

 ```python
 dataset = Dataset(
     label="Revenue",
     data=[15, 25, 35, 45, 55],
     backgroundColor="rgba(153, 102, 255, 0.2)",
     borderColor="rgba(153, 102, 255, 1)",
     borderWidth=1,
 )

 chart = Chart(
     chart_type=ChartType.BAR,
     datasets=[dataset],
     labels=["January", "February", "March", "April", "May"]
 )
 ```

 ## Working with Options

 `pychartjs` allows you to define and customize chart options to control various aspects of your chart’s appearance and behavior.

 ### Example: Setting Chart Options

 ```python
 from pychartjs.options import ChartOptions, Legend, Title

 options = ChartOptions(
     responsive=True,
     maintainAspectRatio=False,
     legend=Legend(display=True, position="top"),
     title=Title(display=True, text="Monthly Sales Data")
 )

 chart = Chart(
     chart_type=ChartType.BAR,
     datasets=[dataset],
     labels=["January", "February", "March", "April", "May"],
     options=options
 )
 ```

 ## Using Plugins

 `pychartjs` supports adding and configuring Chart.js plugins to extend the functionality of your charts.

 ### Example: Using a Plugin

 ```python
 from pychartjs.plugins import Plugin

 plugin = Plugin(name="custom-plugin", options={"option1": "value1"})

 chart = Chart(
     chart_type=ChartType.BAR,
     datasets=[dataset],
     labels=["January", "February", "March", "April", "May"],
     plugins=[plugin]
 )
 ```

 ## Color Schemes and Palettes

 `pychartjs` provides support for color schemes and palettes to enhance the visual appeal of your charts. You can define custom colors or use pre-defined color schemes.

 ### Example: Applying a Color Palette

 ```python
 from pychartjs.colors import ColorPalette

 palette = ColorPalette(
     backgroundColors=[
         "rgba(255, 99, 132, 0.2)",
         "rgba(54, 162, 235, 0.2)",
         "rgba(255, 206, 86, 0.2)",
         "rgba(75, 192, 192, 0.2)",
         "rgba(153, 102, 255, 0.2)",
         "rgba(255, 159, 64, 0.2)"
     ],
     borderColors=[
         "rgba(255, 99, 132, 1)",
         "rgba(54, 162, 235, 1)",
         "rgba(255, 206, 86, 1)",
         "rgba(75, 192, 192, 1)",
         "rgba(153, 102, 255, 1)",
         "rgba(255, 159, 64, 1)"
     ]
 )

 dataset = Dataset(
     label="Revenue",
     data=[15, 25, 35, 45, 55],
     backgroundColor=palette.backgroundColors,
     borderColor=palette.borderColors,
     borderWidth=1,
 )

 chart = Chart(
     chart_type=ChartType.BAR,
     datasets=[dataset],
     labels=["January", "February", "March", "April", "May"]
 )
 ```

 ## Rendering Options

 `pychartjs` allows you to control how your charts are rendered in your web application, including dynamic rendering based on context variables.

 ### Example: Rendering with Context Variables

 ```python
 context = {"year": 2023, "data": [10, 20, 30, 40, 50]}

 chart = Chart(
     chart_type=ChartType.LINE,
     datasets=[Dataset(label=f"Sales Data {context['year']}", data=context['data'])],
     labels=["January", "February", "March", "April", "May"]
 )

 chart_html = chart.render(context=context)
 ```

 ## Advanced Features

 `pychartjs` also supports advanced features like mixed charts, custom scales, and event-driven interactions. You can extend the capabilities of your charts by leveraging these advanced features.

 ### Example: Creating a Mixed Chart

 ```python
 from pychartjs.enums import ChartType

 datasets = [
     Dataset(type=ChartType.BAR, label="Bar Dataset", data=[10, 20, 30]),
     Dataset(type=ChartType.LINE, label="Line Dataset", data=[15, 25, 35])
 ]

 chart = Chart(
     chart_type=ChartType.MIXED,
     datasets=datasets,
     labels=["January", "February", "March"]
 )