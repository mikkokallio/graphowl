# User instructions

## Getting started

Using the dashboard is easy: when you start up the app, the app loads a dashboard and shows it. The app comes with a demo dashboard, so you don't have to do anything else to enjoy spectacular-looking graphs. But of course, you may want to configure a dashboard of your own.

## Configuring a dashboard

See the instructions below on how to make changes to an existing dashboard, or create a wholly new dashboard altogether.

### Adjusting layout

1. Click the **cog** symbol on the left. A config view opens.
2. Change the x and y dimensions to e.g. 2 and 2.
3. Change the title and timespan if you like.
4. Click **save**.
5. Click the **owl** symbol on the left. The dashboard reloads and shows the new layout and other changes.

### Creating new graphs

Creating new graphs is quite error-prone. It is strongly recommended to use an existing graph and then make small changes rather than trying to build from scratch.

1. Click the **graph** icon on the left. Graph configuration view opens.
2. Use the `<` and `>` buttons to find the graph *after* which you'd like to place the new graph.
**Note:** The graphs are laid out in the dashboard view left-right and top-down. So if you are using a 2x2 layout, the first two graphs in order will be on top, and the other two will be below. If you have 5 graphs in a 2x2 layout, the fifth one won't be shown until you change the layout. Conversely, if you have only 3 graphs in a 2x2 layout, the bottom-right one will be empty.
3. Fill in all the fields in the new graph. If you don't know what you're doing (very likely!), use existing graphs from the demo as examples and try changing only small things first.
4. Click **save** and go back to the dashboard view to see if it works. If you get an error, view the message and then your configuration again, and try to figure out what part of the configuration went wrong.

### Configuring a data source

The for the graphs shown in the dashboard comes from different kinds of data sources, which can be databases or REST APIs, among other things. For connecting to data sources, GraphOwl has a few different connectors, currently supporting MongoDb, SQLite, and REST APIs.

To create a new data source or configure an existing one, click the [plug] button to enter the data source configuration view. In that view, you can edit the parameters of a data source, as listed below.

|Parameter|Values|Purpose|
|---|---|---|
|Source name|any|This is the name that your graphs use to identify which data source to use for pulling their data.|
|Connector type|`RESTAPIConnector`, `MongoDbConnector`, `SQLiteConnector`|This value identifies whether the data comes from a REST API or a database of a particular type.|
||||
||||
||||
||||
||||
||||
||||
||||
||||
||||
||||
