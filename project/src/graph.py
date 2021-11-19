from connector import Connector

class Graph:
    """A data handling object representing a graph widget in the dashboard"""

    def __init__(self, title: str, connector: Connector, collection: str, fields: dict):
        """Creates a graph data object with all metadata necessary for pulling data and displaying it in a graph widget.

        Args:
            title (str): Name of the graph widget.
            connector (Connector): Connector object for pulling data.
            collection (str): Name of collection in a database.
            fields (dict): Names of the time, value, and name columns in the collection.
        """
        self.title = title
        self.connector = connector
        self.collection = collection
        self.fields = fields
    
    def asdict(self) -> dict:
        """Converts the graph back to a saveable format.

        Returns:
            dict: A dictionary representation of the graph object.
        """
        return {'title': self.title, 'connector': self.connector.name, 'collection': self.collection, 'fields': self.fields}
    
    def load(self, timespan=None):
        """Uses the connector to pull data from the data source.

        Returns:
            [dict]: Data to show in the corresponding UI widget.
        """
        return self.connector.get_data(self.collection, self.fields, timespan)
