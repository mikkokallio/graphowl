from mongodbconnector import MongoDbConnector
from graph import Graph


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
        self.layout = layout
        self.timespan = timespan
        self.interval = interval
        self.sources = {}
        self.graphs = []

        for source in sources:
            self.sources.update({source['name']: MongoDbConnector(source['uri'], f'certs/{source["cert"]}', source['database'])})
        
        for graph in graphs:
            self.graphs.append(Graph(graph['title'], self.sources[graph['connector']], graph['collection'], graph['fields']))

    def load_all(self):
        """Requests all graphs in the dashboard to pull data from their connectors.

        Returns:
            list: List where each item contains data for one graph.
        """
        return [{'title': graph.title, 'plots': graph.load()} for graph in self.graphs]
