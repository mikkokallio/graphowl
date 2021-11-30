import sqlite3
from connectors.connector import Connector


class SQLiteConnector(Connector):
    """Establishes connection to SQLite and loads data into appropriate format"""

    def __init__(self, name: str, uri: str, **kwargs) -> None:
        """Creates a connection to a particular database in a SQLite instance.

        Args:
            uri (str): Connection string for the database.
        """

        super().__init__(name, uri)
        self.config = kwargs

    def asdict(self):
        return {'name': self.name, 'uri': self.uri, **self.config}

    def get_data(self, collname: str, fields: dict, timespan: int) -> dict:
        """Fetches data from the database.

        Args:
            table (str): Table from where data is fetched.
            fields (dict): Names of the columns (e.g. timestamp, measurement, sensor_name).

        Returns:
            dict: Data in a format suitable for matplotlib.
        """

        start_time = self._get_start_time(timespan)
        con = sqlite3.connect(self.uri)
        cur = con.cursor()
        # TODO: sanitize fields - parametrized query not possible
        if timespan is None:
            cur.execute(f'SELECT {fields["time"]}, {fields["value"]}, {fields["name"]} FROM {collname}')
        else:
            cur.execute(f'SELECT {fields["time"]}, {fields["value"]}, {fields["name"]} FROM {collname} WHERE {fields["time"]} > {start_time}')

        result = cur.fetchall()
        con.close()

        data = [{fields['time']: row[0], 'value': row[1], 'name': row[2]} for row in result]
        return self._transform(data)
