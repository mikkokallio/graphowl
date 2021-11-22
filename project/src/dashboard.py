from connectors.mongodbconnector import MongoDbConnector
from connectors.sqliteconnector import SQLiteConnector
from graph import Graph
from constants import TIME_EXP
from connectors.connector import Connector


class Dashboard:
    """Contains all graphs and other configuration and data"""

    def __init__(self, title: str, layout: dict, timespan: str, interval: str, sources: list, graphs: list):
        """Creates a dashboard data object, which is the interface between the UI and data collection.

        Args:
            title (str): Title for the entire dashboard.
            layout (dict): Indicates how many graphs are stacked horizontally (x) and vertically (y).
            timespan (str): How many hours/days worth of data is fecthed and displayed.
            interval (str): How often the graphs update.
            sources (list): Databases and other sources to fetch data from.
            graphs (list): Graphs to display in the layout.
        """

        self.title = title
        self.layout = self.validate_layout(layout)
        # TODO: Refactor this to only validate the time strings here and do conversion elsewhere?
        self.timestring = timespan
        self.intervalstring = interval
        self.timespan = self.parse_time_config(timespan)
        self.interval = self.parse_time_config(interval)
        self.sources = {}
        self.graphs = []
                
        for source in sources:
            self.sources.update({source['name']: globals()[source['connector']](**source)})
        
        for graph in graphs:
            self.graphs.append(Graph(graph['title'], self.sources[graph['connector']], graph['collection'], graph['fields']))

    def asdict(self):
        """Generate a dict that can be saved as yaml
        """

        # TODO: Refactor away name vs title disparity
        return {'name':self.title, 'timespan':self.timestring, 'interval':self.intervalstring, 'layout':self.layout,
                'sources':[source.asdict() for source in self.sources.values()], 'graphs':[graph.asdict() for graph in self.graphs]}
    
    def validate_layout(self, layout: dict):
        """Turns layout dimensions into 1 if they aren't positive integers"""
        return {k:(v if type(v) is int and v>0 else 1) for k,v in layout.items()}
    
    def parse_time_config(self, timestring: str):
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
        return [{'title': graph.title, 'plots': graph.load(self.timespan)} for graph in self.graphs]
