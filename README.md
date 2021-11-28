# GraphOwl

GraphOwl displays time series data as graphs in a dashboard.

You can configure the app to connect to various data sources (such as MongoDb or SQLite) and show the data as multi-plot graphs. The data should contain *time* and *value* columns, which are used as the x and y coordinates on the graphs, and a *name* column, which determines which data points belong to the same plot. This column could contain, for example, the names of sensors that were used to collect the data.

![Dashboard example](https://github.com/mikkokallio/ot-harkka/blob/master/project/docs/Screenshot.png "Sensor readings")

## Test database

The repo contains a demo configuration and database, which allow you to test the dashboard after installing the app. The data is copied from a live MongoDb instance, but the copy is stale, so time span is disabled in the configuration. Right now, you won't be able to do much; the UI has no controls yet, but you can try and adjust the yaml in the `config` folder and see how it affects the dashboard.

## Documentation

The following docs describe the app further:
* User instructions (TO BE ADDED)
* [Requirement specification](https://github.com/mikkokallio/ot-harkka/blob/master/project/docs/reqs.md)
* Architecture (TO BE ADDED)
* Testing documentation (TO BE ADDED)
* [UML class diagram](https://github.com/mikkokallio/ot-harkka/blob/master/project/docs/classes.yuml)
* [Work tracking sheet](https://github.com/mikkokallio/ot-harkka/blob/master/project/docs/hours.md)

## Usage

**Note:** The app has been tested with Python `3.8`.

Run the following commands in the `project` folder.

* To install, run `poetry install`.
* To start the app, run `poetry run invoke start`.
* To run tests, run `poetry run invoke test`.
* For test coverage report, run `poetry run invoke coverage-report`.
* To run the linter, run `poetry run invoke lint`.

TO BE ADDED: Build phase
