from connectors.mongodbconnector import MongoDbConnector
from connectors.sqliteconnector import SQLiteConnector
from connectors.restapiconnector import RESTAPIConnector
from connectors.connector import Connector
from graph import Graph
from constants import TIME_EXP


class Dashboard:
    """Contains all graphs and other configuration and data"""

    def __init__(self, title: str, layout: dict, legend: str, timespan: str, interval: str, sources: list, graphs: list):
        """Creates a dashboard object, which is the interface between the UI and data collection.

        Args:
            title (str): Title for the entire dashboard.
            layout (dict): How many graphs are stacked horizontally (x) and vertically (y).
            timespan (str): How many hours/days worth of data is fecthed and displayed.
            interval (str): How often the graphs update.
            sources (list): Databases and other sources to fetch data from.
            graphs (list): Graphs to display in the layout.
        """

        self._title = title
        self._layout = self._validate_layout(layout)
        self._legend = True if legend == 'yes' else False
        self._timespan = self._parse_time_config(timespan)
        self._interval = self._parse_time_config(interval)
        self._sources = {}
        self._graphs = []

        for source in sources:
            try:
                self._sources.update({source['name']: globals()[source['connector']](**source)})
            except KeyError:
                self._sources.update({source['name']: None})

        for graph in graphs:
            connector = self._sources[graph['connector']] if graph['connector'] in self._sources else None
            try:
                self._graphs.append(Graph(graph['title'], connector,
                                          graph['collection'], graph['fields'], graph['transformations']))
            except KeyError:
                self._graphs.append(Graph(None, None, None, None, None))

    @property
    def title(self):
        return self._title

    @property
    def layout(self):
        return self._layout

    @property
    def legend(self):
        return self._legend

    @property
    def timespan(self):
        return self._timespan

    @property
    def interval(self):
        return self._interval

    def _validate_layout(self, layout: dict):
        """Turns layout dimensions into 1 if they aren't positive integers"""
        return {k:(v if isinstance(v, int) and v>0 else 1) for k,v in layout.items()}

    def _parse_time_config(self, timestring: str):
        """Converts time strings to seconds.

        Args:
            timestring (str): An expression of an amount of time, such as "5 minutes" or "2 hours"
        """

        try:
            n, units = timestring.split(' ')
            return int(n) * TIME_EXP[units] if int(n) > 0 else None
        except KeyError:
            return None
        except ValueError:
            return None

    def load_all(self):
        """Requests all graphs in the dashboard to pull data from their connectors.

        Returns:
            list: List where each item contains data for one graph.
        """
        return [{'title': graph.title,
                 'plots': graph.load(self._timespan)} for graph in self._graphs]
