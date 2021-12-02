from connectors.connector import Connector


class Graph:
    """A data handling object representing a graph widget in the dashboard"""

    def __init__(self, title: str, connector: Connector, collection: str, fields: dict):
        """Creates an object capable of pulling data to display in a graph.

        Args:
            title (str): Name of the graph widget.
            connector (Connector): Connector object for pulling data.
            collection (str): Name of collection in a database.
            fields (dict): Names of the time, value, and name columns in the collection.
        """
        self._title = title
        self._connector = connector
        self._collection = collection
        self._fields = fields

    @property
    def title(self):
        return self._title

    def load(self, timespan=None):
        """Uses the connector to pull data from the data source.

        Returns:
            [dict]: Data to show in the corresponding UI widget.
        """
        return self._connector.get_data(self._collection, self._fields, timespan)
