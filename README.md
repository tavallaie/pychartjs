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

 ## Usage

 ### Running the Integration Tests

 The project includes an integration test that sets up a simple web server with Robyn to display all chart types.

 1. **Navigate to the `integration_tests` directory:**

    ```bash
    cd integration_tests
    ```

 2. **Run the Application:**

    Start the web server:

    ```bash
    python app.py
    ```

 3. **View in Browser:**

    Open your browser and go to `http://localhost:8080`. You should see a page displaying all the supported chart types.

 ### Adding New Charts

 To add a new chart type or customize an existing one, modify the `app.py` file and create new chart instances there.

 ### Context Variables

 The charts can be dynamically generated with context variables. For example, you can pass a `year` or `month` variable to customize the labels and datasets.

 ### Integration with Other Web Frameworks

 Pychartjs is flexible and can be integrated with other popular Python web frameworks such as:

 - **Django**: Easily render charts within Django views and templates.
 - **FastAPI**: Use Pychartjs to generate charts in FastAPI routes.
 - **Flask**: Integrate with Flask to display dynamic charts.
 - **Any other WSGI/ASGI framework**: Pychartjs can be adapted to work with any Python web framework that supports WSGI or ASGI.
