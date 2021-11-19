import sqlite3
from connectors.connector import Connector


class SQLiteConnector(Connector):
    """Establishes connection to SQLite and loads data into appropriate format"""

    def __init__(self, name: str, uri: str, cert: str, db: str) -> None:
        """Creates a connection to a particular database in a SQLite instance.

        Args:
            uri (str): Connection string for the database.
            cert (str): Path to authentication certificate.
            db (str): Database name.
        """
        
        super().__init__(name, uri)
        
    def get_data(self, table: str, fields: dict, timespan: int) -> dict:
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
        cur.execute('select :time, :value, :name from :table where :time>:start', 
                    {'time': fields['time'], 'value': fields['value'], 'name': fields['name'], 'table': table, 'start': start_time})
        result = cur.fetchall()
        con.close()

        print(result)
        data = [{fields['time']: row[fields['time']], 'value': row[fields['value']], 'name': row[fields['name']]} for row in result]
        return self._transform(data)
