from os.path import exists
import sqlite3
from connectors.connector import Connector, ConnectorConfigurationError


class SQLiteConnector(Connector):
    """Establishes connection to SQLite and loads data into appropriate format"""

    def __init__(self, uri: str, transformations: dict, **kwargs) -> None:
        """Creates a connection to a particular database in a SQLite instance.

        Args:
            uri (str): Connection string for the database.
        """

        super().__init__(uri, transformations)
        self._trans = transformations
        self._config = kwargs

    def get_data(self, collname: str, fields: dict, transformations: dict, timespan: int) -> dict:
        """Fetches data from the database.

        Args:
            table (str): Table from where data is fetched.
            fields (dict): Names of the columns (e.g. timestamp, measurement, sensor_name).

        Returns:
            dict: Data in a format suitable for matplotlib.
        """
        if not exists(self._uri):
            raise ConnectorConfigurationError('database file missing')
        con = sqlite3.connect(self._uri)
        cur = con.cursor()
        start_time = self._get_start_time(timespan)
        # TODO: sanitize fields - parametrized query not possible
        query = f'SELECT {fields["time"]}, {fields["value"]}, {fields["name"]} FROM {collname}'
        condition = f' WHERE {fields["time"]} > {start_time}'
        cur.execute(query + condition)
        data = cur.fetchall()
        con.close()
        return self._apply_transformations(data, transformations, fields, start_time)
