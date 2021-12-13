# GraphOwl

GraphOwl displays time series data as graphs in a dashboard.

You can configure the app to connect to various data sources (such as MongoDb or SQLite) and show the data as multi-plot graphs. The data should contain *time* and *value* columns, which are used as the x and y coordinates on the graphs, and a *name* column, which determines which data points belong to the same plot. This column could contain, for example, the names of sensors that were used to collect the data. In the screenshot below, `hallway`, `living-room`, `kitchen`, and `bathroom` are *name* values.

![Dashboard example](https://github.com/mikkokallio/ot-harkka/blob/master/project/docs/Screenshot.png "Sensor readings")

## Current features of the app

The main functionality (showing graphs) works fine and now you can also configure the dashboard through the UI. Try to edit and save some attributes, especially the `title` fields and `layout` dimensions `x` and `y` and go back to the dashboard view to see how it changes. You can also add new graphs and data sources using the `+` button in those views. Instructions on how to configure those will be added later! Note that changes to data sources and such may break the graphs, but feel free to try that too, to see different UI messages. See also how your changes affect the `config/dashboard.yaml` file. The demo dashboard uses a snapshot from a live database, but that snapshot doesn't get updated, so `timespan` should be `none` because otherwise you'll probably just get a warning: "no data".

## Documentation

The following docs describe the app further:
* User instructions (TO BE ADDED)
* [Requirement specification](https://github.com/mikkokallio/ot-harkka/blob/master/project/docs/reqs.md)
* [Architecture](https://github.com/mikkokallio/ot-harkka/blob/master/project/docs/architecture.md)
* Testing documentation (TO BE ADDED)
* [Work tracking sheet](https://github.com/mikkokallio/ot-harkka/blob/master/project/docs/hours.md)

## Usage

**Note:** The app has been tested with Python `3.8`.

Clone the latest version, or a release: [viikko5](https://github.com/mikkokallio/ot-harkka/releases/tag/viikko5)

Run the following commands in the `project` folder.

* To install, run `poetry install`.
* To start the app, run `poetry run invoke start`.
* To run tests, run `poetry run invoke test`.
* For test coverage report, run `poetry run invoke coverage-report`.
* To run the linter, run `poetry run invoke lint`.

TO BE ADDED: Build phase
