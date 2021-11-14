class Graph:
    """A data handling object representing a graph widget in the dashboard"""

    def __init__(self, title: str, connector: str, collection: str, time: str, value: str, name: str):
        """Creates a graph data object with all metadata necessary for pulling data and displaying it in a graph widget.

        Args:
            title (str): Name of the graph widget.
            connector (str): Name of connector for pulling data.
            collection (str): Name of collection in a database.
            time (str): Name of the time column in the collection.
            value (str): Name of the value column in the collection.
            name (str): Name of the name column in the collection.
        """
        self.title = title
        self.connector = connector
        self.collection = collection
        self.time = time
        self.value = value
        self.name = name
    
    def load(self):
        """Uses the connector to pull data from the data source.

        Returns:
            [dict]: Data to show in the corresponding UI widget.
        """
        return self.connector.get_data(self.collection, time=self.time, value=self.value, name=self.name)
