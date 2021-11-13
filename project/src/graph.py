class Graph:
    """One graph data handling object in the dashboard"""

    def __init__(self, title, connector, collection, time, value, name):
        self.title = title
        self.connector = connector
        self.collection = collection
        self.time = time
        self.value = value
        self.name = name
    
    def load(self):
        return self.connector.get_data(self.collection)
