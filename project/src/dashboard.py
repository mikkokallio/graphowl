from mongodbconnector import MongoDbConnector
from graph import Graph


class Dashboard:
    """Contains all graphs and other configuration and data"""

    def __init__(self, title, layout, timespan, interval, sources, graphs):
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
        return [{'title': graph.title, 'plots': graph.load()} for graph in self.graphs]
