# Requirement spec

## Description

GraphOwl is a dashboard application for displaying time series data, such as temperature measurements, as graphs. The app has two modes: view mode, in which the UI offers , and edit mode, in which the user can change the configuration.

Initially, the goal is to create a minimum viable product (MVP) as outlined below, and expand from there, adding as many additional features as possible before time runs out.

## Minimal viable product (MVP)

The MVP consists of:
* [X] The UI has a simple but professional look with light colors against a dark background. The UI is created with tkinter and it uses matplotlib to draw graphs.
* [X] Initially, there is only one view: the dashboard view. The UI has a narrow top bar and left pane, but the majority of the view is dedicated to displaying graphs. The top bar and left pane are initially empty.
* [X] The app has a single connector for fetching data from any MongoDb database. A connector is a Python class that can fetch row-based data with time and value columns (for single-plot graphs), or time, value, and name columns (for multi-plot graphs). The connector can apply small transformations to the source data, such as mapping column names.
* [ ] The app automatically updates the graph data every n minutes.
* [X] User can configure the dashboard using a YAML file. This includes:
- [X] A title for the dashboard.
- [X] Grid layout using x (rows) and y (columns). 
- [ ] Time span, i.e. how many hours or days worth of data is queried and displayed.
- [ ] Update interval in minutes.
- [X] Database connector configuration, such as name, data source type, and connection string. 
- [X] Graph configuration, such as graph titles, table names to fetch the data from, and column name mappings.

## Additional features

After the MVP, more features will be added, focusing mainly on those that are feasible to implement, possible to test, and contribute toward a higher score / grade. Ideas for additional features include:

### Integrations
* [ ] The app has connectors for multiple types of databases and can also fetch JSON data from REST APIs. All connectors inherit the same generic parent class, so that higher-level components can use the same API to fetch data while remaining agnostic of the data sources.
* [ ] Connectors can also use columnar data. Transformation algorithms can handle more variance in data models.
* [ ] Connectors can cache data so that they don't need to fetch the same rows again.

### View mode
* [ ] In view mode, user can click buttons to aggregate the data in different ways, e.g. displaying average, max, min, or sum values based on a selected time window.
* [ ] In view mode, UI has a timespan drop-down selector (e.g. show last 30 mins, show last 7 days). In edit mode, the same control sets the default timespan.
* [ ] In view mode, user can click a graph to enter a detail view: the app zooms in on the graph, filling much of the main area. Clicking on the graph again zooms out to normal dashboard view. While zoomed in, the user can see more information, e.g. some statistical data, such as mean, median, variance, min, max within the given time span.
* [ ] In view mode, if user hovers on graph, it shows a tooltip with numeric values from that point in time. While hovering, other graphs in the same dashboard show what their values were at the same point in time.
* [ ] In view mode, user can "paint" horizontally on a graph to change the timespan to the selected interval. All other graphs in the dashboard also change to that time window.

### Edit mode
* [ ] The user can enter an edit mode, where controls for editing the dashboard are shown (e.g. change title, adjust layout, add connector). Upon exiting the user mode, user has to Save or Cancel all edits. If saved, the yaml is updated accordingly.
* [ ] In edit mode, user can drag-and-drop graphs to change their position.
* [ ] In edit mode, user can grab the bottom-right corner of a graph to change its size.
* [ ] In edit mode, user can set thresholds and alerts. The graph can show the threshold as a horizontal line, and if an alert is triggered, the borders of the graph flash angrily red every few seconds.
* [ ] In edit mode, clicking on a graph opens a detail view, where user can set title, connection string, etc. for the graph.
* [ ] In edit mode, user can customize the color scheme of the dashboard, or even that of the individual graphs.
* [ ] In edit mode, user can save dashboards in the cloud. The destination may be a file share or a database. Secure handling of credentials is a key consideration.
* [ ] In edit mode, user can create more dashboards, which are shown as tabs in the top bar.

### Look and feel
* [ ] There is a stylish owl logo in the top-left corner.
* [ ] UI has a more polished look with some pizzazz. User can click a light bulb button to make the plots glow like neon lights. When the view is refreshed or user changes to a different view, graphs "pop up" using a simple animation.
