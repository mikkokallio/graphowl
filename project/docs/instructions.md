# User instructions

## Getting started

Using the dashboard is easy: when you start up the app, the app loads a dashboard and shows it. The app comes with a demo dashboard, so you don't have to do anything else to enjoy spectacular-looking graphs. But of course, you may want to configure a dashboard of your own.

## Configuring a dashboard

See the instructions below on how to make changes to an existing dashboard, or create a wholly new dashboard altogether.

### Adjusting layout

1. Click <img src="https://github.com/mikkokallio/ot-harkka/blob/master/project/src/ui/icons/cog.png" width="3%" /> on the left. A config view opens.
2. Change the x and y dimensions to e.g. 2 and 2.
3. Change the title and timespan if you like.
4. Click **save**.
5. Click the <img src="https://github.com/mikkokallio/ot-harkka/blob/master/project/src/ui/icons/owl.png" width="3%" /> symbol on the left. The dashboard reloads and shows the new layout and other changes.

### Configuring graphs and data sources

To configure graphs or data sources, click the <img src="https://github.com/mikkokallio/ot-harkka/blob/master/project/src/ui/icons/graph.png" width="3%" /> or <img src="https://github.com/mikkokallio/ot-harkka/blob/master/project/src/ui/icons/plug.png" width="3%" />, respectively. **Note:** Creating new graphs or data sources is quite error-prone. It is strongly recommended to use an existing graph or data source and then make small changes rather than trying to build from scratch.

* Use <img src="https://github.com/mikkokallio/ot-harkka/blob/master/project/src/ui/icons/left.png" width="3%" /> and <img src="https://github.com/mikkokallio/ot-harkka/blob/master/project/src/ui/icons/right.png" width="3%" /> to browse graphs or data sources.
* Use <img src="https://github.com/mikkokallio/ot-harkka/blob/master/project/src/ui/icons/cross.png" width="3%" /> to delete a graph or data source.
* Use <img src="https://github.com/mikkokallio/ot-harkka/blob/master/project/src/ui/icons/plus.png" width="3%" /> to create a new graph or data source.
* Enter values (see Configuring a graph and Configuring a data source for details).
* Click `Save` to save the changes.

Once you have saved the changes, go back to the dashboard view to see if the changes worked as intended.  If you get an error, view the message and then your configuration again, and try to figure out what part of the configuration went wrong.

**Note:** The graphs are laid out in the dashboard view left-right and top-down. So if you are using a 2x2 layout, the first two graphs in order will be on top, and the other two will be below. If you have 5 graphs in a 2x2 layout, the fifth one won't be shown until you change the layout. Conversely, if you have only 3 graphs in a 2x2 layout, the bottom-right one will be empty.

### Configuring a graph

The dashboard consists of various graphs, which may have different data sources. To create a new graph or configure and existing one, click <img src="https://github.com/mikkokallio/ot-harkka/blob/master/project/src/ui/icons/graph.png" width="3%" /> to enter the graph configuration view. In that view, you can edit the parameters of a graph, as listed below.

|Parameter|Values|Purpose|
|---|---|---|
|Graph title|string|Title to be shown in the dashboard view above the graph.|
|Source name|string|Source name as it's written in the data source's `Source name` parameter.|
|Table / collection / endpoint|string|In a database data source, this identifies the table or collection within the database.|
|Field: name|string|If pivoting, this column has the names of the plots.|
|Field: time|string|If pivoting, this column has the timestamp.|
|Field: value|string|If pivoting, this column has the data point values.|
|Keep plots|comma-separated string|If empty, all plots are shown in the graph. Otherwise, only the listed plots are shown.|

### Configuring a data source

The data for the graphs shown in the dashboard comes from different kinds of data sources, which can be databases or REST APIs, among other things. For connecting to data sources, GraphOwl has a few different connectors, currently supporting MongoDb, SQLite, and REST APIs.

To create a new data source or configure an existing one, click <img src="https://github.com/mikkokallio/ot-harkka/blob/master/project/src/ui/icons/plug.png" width="3%" /> to enter the data source configuration view. In that view, you can edit the parameters of a data source, as listed below.

|Parameter|Values|Purpose|
|---|---|---|
|Source name|string|This is the name that your graphs use to identify which data source to use for pulling their data.|
|Connector type|`RESTAPIConnector`, `MongoDbConnector`, `SQLiteConnector`|This value identifies whether the data comes from a REST API or a database of a particular type.|
|URI|string|A string that uniquely identifies the data source you are connecting to. For a REST API, this is the http(s) address (URL) of the endpoint to get data from. For MongoDb, this is the connection string to a database instance. For SQLite, this is the path and filename of the database file.|
|Database name|string|For MongoDb, this identifies the database within the MongoDb instance. For REST API or SQLite, leave this value empty.|
|Certificate filename|string|For MongoDb, this is the filename of a certificate created for authentication. If your connection string includes your credentials, you don't need a certificate. For REST API or SQLite, leave this value empty.|
|Parse result from format|`no parsing`, `xml`, `json`|This indicates what format the data source's response uses. REST APIs often use either XML or JSON, but also CSV is possible. If it's CSV, the parsing actually happens at the `Payload format` stage (see below), so no parsing is needed at this stage. Also, databases usually respond in a format that doesn't need XML or JSON parsing.|
|Path to traverse|comma-separated string|If the result required parsing from XML or JSON, the response usually has a nested structure, and the payload data (the actual time series data) may be buried somewhere deeper in the structure. In this case, it's necessary to traverse the structure to get to the payload. In (ADD example), the first level in the structure is `dataset`, and under that there are several child levels, of which the correct one is `value`. So in this case, the path to traverse would be `dataset,value`. If the payload is at the root level of the structure, leave this value empty.|
|Payload format|`records`,`csv`|Data from a database, or an XML  or JSON structure is often in a structured format, but it's also possible that it's CSV embedded into XML or JSON, or the whole response is just a CSV file. In that case, choose `csv`. Otherwise, choose `records`.|
|CSV delimiter|character|A character (comma, semicolon, space, etc.) with which to split the CSV into columns.|
|Pivot rows|`yes`, `no`|If the data has the data points for different plots on different rows rather than having the plots as different columns, you need to pivot the data. Pivoting uses the three `field` values from graph configuration, so check that those are correct for each graph.|
|Header from|`already exists`, `add names`, `first row`|Determines whether column names already exist or need to be added manually, or taken from the first row in CSV data.|
|Header names|comma-separated string|If column names are added by selecting `add names` in the selection above, list the column names here as a comma-separated list.|
|Timestamp type|`milliseconds`, `datetime`|Determines what format timestamps use in the data. If the data already uses valid datetime, no conversion is needed. Otherwise, the app converts the timestamps from milliseconds or another format.|
|Time step|number|If there is not time information in the data, the timestamps have to be generated. The first timestamp is based on the `timespan` in the dashboard configuration. All subsequent timestamps increase by the time step value from the previous timestamp, which is measured in seconds.|
