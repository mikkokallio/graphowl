# GraphOwl

GraphOwl displays time series data as graphs in a dashboard.

You can configure the app to connect to various data sources (currently REST APIs, MongoDb, and SQLite) and show the data as multi-plot graphs. The data should contain timestamps and values for data points on one or multiple plots. This can be a tabular format, where one of the columns is the timestamp and other columns represent the plots, containing the values. Other source data formats can be used, and transformations can be applied to the data to convert it into format suitable for the graphs. 

![Dashboard example](https://github.com/mikkokallio/ot-harkka/blob/master/project/docs/Screenshot.png "Sensor readings")

## Demo dashboard

The app comes with a demo dashboard, `dashboard_weather.yaml`, which contains some weather data from Helsinki but also one graph about Covid vaccinations. Other demo dashboards also exist in the `project/config` folder.

## Documentation

The following docs describe the app further:
* [User instructions](https://github.com/mikkokallio/ot-harkka/blob/master/project/docs/instructions.md)
* [Requirement specification](https://github.com/mikkokallio/ot-harkka/blob/master/project/docs/reqs.md)
* [Architecture](https://github.com/mikkokallio/ot-harkka/blob/master/project/docs/architecture.md)
* [Testing document](https://github.com/mikkokallio/ot-harkka/blob/master/project/docs/testing.md)
* [Work tracking sheet](https://github.com/mikkokallio/ot-harkka/blob/master/project/docs/hours.md)

## Usage

**Note:** The app has been tested with Python `3.8`.

Run the following commands in the `project` folder.

* To install, run `poetry install`.
* To start the app, run `poetry run invoke start`.
* To run tests, run `poetry run invoke test`.
* For test coverage report, run `poetry run invoke coverage-report`.
* To run the linter, run `poetry run invoke lint`.
