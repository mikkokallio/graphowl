# GraphOwl

GraphOwl displays time series data as graphs in a dashboard.

You can configure the app to connect to various data sources (such as MongoDb or SQLite) and show the data as multi-plot graphs. The data should contain *time* and *value* columns, which are used as the x and y coordinates on the graphs, and a *name* column, which determines which data points belong to the same plot. This column could contain, for example, the names of sensors that were used to collect the data. In the screenshot below, `hallway`, `living-room`, `kitchen`, and `bathroom` are *name* values.

![Dashboard example](https://github.com/mikkokallio/ot-harkka/blob/master/project/docs/Screenshot.png "Sensor readings")

## Current features of the app

The main functionality -- showing graphs -- already works fine. You can also try and edit `config/dashboard.py`, especially the `title` fields and `layout` dimensions `x` and `y` to see how the dashboard view changes. The demo dashboard uses a snapshot from a live database, but that snapshot doesn't get updated, so changing `timespan` should be `none` because otherwise you'll get just a warning: "no data".

You can also try out the different views on the left: The three icons below the owl logo take you to configuration views. Changing values and hitting the `save` button actually works, but the dashboard *is not* updated until you run the app again. (I'll fix that later.) Also, the `+` button (for adding new stuff) doesn't work yet.

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
