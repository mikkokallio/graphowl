# GraphOwl

GraphOwl displays time series data as graphs in a dashboard.

You can configure the app to connect to various data sources (such as MongoDb or SQLite) and show the data as multi-plot graphs. The data should contain *time* and *value* columns, which are used as the x and y coordinates on the graphs, and a *name* column, which determines which data points belong to the same plot. This column could contain, for example, the names of the rooms where sensors collect, such as `hallway`, `living-room`, `kitchen`, and `bathroom`.

In some data sources, the data is in a different format, such as the one below. The API returns an XML, which then is parsed and the data structure is traversed to find the payload, which is also parsed. Here individual columns have only numbers, and they are named in the dashboard's configuration file.

![Dashboard example](https://github.com/mikkokallio/ot-harkka/blob/master/project/docs/Screenshot.png "Sensor readings")

## Current features of the app: week 6

The main functionality (showing graphs) works fine and now you can also configure the dashboard through the UI. Try to edit and save some attributes, especially the `title` fields and `layout` dimensions `x` and `y` and go back to the dashboard view to see how it changes. You can also add new graphs and data sources using the `+` button in those views, or remove them with the `x` button. Instructions on how to configure those will be added later!

NEW: Live weather dashboard! I added a REST API connector (unfortunately not a generic one, actually rather specific for this data source), which gets almost real-time weather data from Finland. Some timespans may break the graphs because the API has limitations.

That one's now the default dashboard, named `config/dashboard_live.yaml`, but the old static SQLite one is also still there, named `config/dashboard.yaml`. That demo dashboard uses a snapshot from a live database, but that snapshot doesn't get updated, so `timespan` should be `none` because otherwise you'll probably just get a warning: "no data".

## Documentation

The following docs describe the app further:
* [User instructions](https://github.com/mikkokallio/ot-harkka/blob/master/project/docs/instructions.md)
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
