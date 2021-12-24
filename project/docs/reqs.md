# Requirement spec

## Description

GraphOwl is a dashboard application for displaying time series data, such as temperature measurements, as graphs. The app has a dashboard view, and three configuration views: one for settings that affect the whole dashboard, and additional ones for configuring graphs and data sources that can pull data for the graphs.

Initially, the goal is to create a minimum viable product (MVP) as outlined below, and expand from there, adding as many additional features as possible before time runs out.

## Minimal viable product (MVP)

The MVP consists of:
* [X] The UI has a simple but professional look with light colors against a dark background. The UI is created with tkinter and it uses matplotlib to draw graphs.
* [X] Initially, there is only one view: the dashboard view. The UI has a left pane for navigation, but the majority of the view is dedicated to displaying graphs.
* [X] The app has a single connector for fetching data from any MongoDb database. A connector is a Python class that can fetch row-based data with time, value, and name columns (for multi-plot graphs). The connector can apply small transformations to the source data, such as mapping column names.
* [X] The app has a refresh button for fetching up-to-date data.
* [X] User can configure the dashboard using a YAML file. This includes:
- [X] A title for the dashboard.
- [X] Switch legends on/off.
- [X] Grid layout using x (rows) and y (columns). 
- [X] Time span, i.e. how many hours or days worth of data is queried and displayed.
- [X] Database connector configuration, such as name, data source type, and connection string. 
- [X] Graph configuration, such as graph titles, table names to fetch the data from, and column name mappings.

## Additional features

After the MVP, more features will be added, focusing mainly on those that are feasible to implement, possible to test, and contribute toward a higher score / grade. Ideas for additional features include:

### Integrations
* [X] The app has a SQLite connector.
* [X] The app has a REST API connector.
* [X] The connectors can handle XML, JSON, and CSV.
* [X] The connectors can traverse structured data to find the payload.
* [X] The connectors can pivot data, rename columns, and apply other transformations.
* [X] The connectors and transformations are easily extensible so that whenever the current implementation can't handle something, a new feature can be easily added.

### General UI look and feel
* [X] The UI has stylish buttons.
* [X] UI has a polished look with some pizzazz: neat color scheme and plots have a faint glow so they look a bit like neon lights.
* [X] Configuration views have configurable, reusable forms.
* [X] In graph and data source views, the user can navigate the graph or source entries with buttons. There's a carousel indicator squares showing the current position, which also function as buttons to go directly to that entry.

### Dashboard view
* [X] The view refreshes whenever edits are made through the UI.
* [X] The view shows meaningful error messages if something is misconfigured.

### Edit dashboard view
* [X] The user can enter an edit mode, where controls for editing the dashboard are shown (e.g. change title, adjust layout). User can save changes, and the yaml is updated accordingly.
* [X] User can change timespan using a drop-down selector (e.g. show last 30 mins, show last 7 days).

### Edit graphs view
* [X] A separate view for editing graphs exists.
* [X] User can set the title, connection string, etc. of a graph.
* [X] User can add and delete graphs through UI.

### Edit connectors view
* [X] A separate view for editing connectors exists.
* [X] User can configure a connector's name, connector class, database name, and a long list of transformations.
* [X] User can add and delete connectors through UI.

### Possible later additions

* [ ] Connectors can cache data so that they don't need to fetch the same rows again.
* [ ] User can click buttons to aggregate the data in different ways, e.g. displaying average, max, min, or sum values based on a selected time window.
* [ ] In view mode, user can click a graph to enter a detail view: the app zooms in on the graph, filling much of the main area. Clicking on the graph again zooms out to normal dashboard view. While zoomed in, the user can see more information, e.g. some statistical data, such as mean, median, variance, min, max within the given time span.
* [ ] If user hovers on graph, it shows a tooltip with numeric values from that point in time. While hovering, other graphs in the same dashboard show what their values were at the same point in time.
* [ ] User can "paint" horizontally on a graph to change the timespan to the selected interval. All other graphs in the dashboard also change to that time window.
* [ ] User can customize the color scheme of the dashboard.
* [ ] User can save dashboards in the cloud. The destination may be a file share or a database. Secure handling of credentials is a key consideration.
* [ ] User can adjust the graphs' position (drag and drop, or arrows).
* [ ] User can adjust a graph's size (e.g. grab the bottom-right corner).
* [ ] User can set thresholds and alerts. The graph can show the threshold as a horizontal line, and if an alert is triggered, the borders of the graph flash angrily red every few seconds.
* [ ] User can adjust the colors and other visual elements of the graph.
* [ ] Carousel indicator shaped like the dashboard, e.g. 2x2
* [ ] User can select a dashboard file from list
* [ ] User can see tooltops when viewing config forms
* [ ] User sees a loader / splash screen whenever loading takes a while
* [ ] Loading the graphs uses threading / async to make it faster
* [ ] Configure colors centrally