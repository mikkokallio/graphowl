import pymongo
from connector import Connector


class MongoDbConnector(Connector):
    """Establishes connection to MongoDb and loads data into appropriate format"""

    def __init__(self, name: str, uri: str, cert: str, db: str) -> None:
        """Creates a connection to a particular database in a MongoDb instance.

        Args:
            uri (str): Connection string for the database.
            cert (str): Path to authentication certificate.
            db (str): Database name.
        """
        
        super().__init__(name)
        self._client = pymongo.MongoClient(uri, tls=True, tlsCertificateKeyFile=cert)
        self._db = self._client[db]

    def _transform(self, data: dict) -> dict[str, tuple[list, list]]:
        """Transforms raw MongoDb data into a dictionary with arrays that UI widgets can use to show graphs with matplotlib.

        Args:
            data (dict): Raw data fetched from MongoDb.

        Returns:
            dict[str, tuple[list, list]]: A dictionary with a tuple for each plot, which in turn contains an array for x and y coordinates each.
        """

        plots = {row['name']:([],[]) for row in data}
        for row in data:
            plots[row['name']][0].append(row['time'])
            plots[row['name']][1].append(row['value'])
        return plots
        
    def get_data(self, collname: str, fields: dict, timespan: int) -> dict:
        """Fetches data from the database.

        Args:
            collname (str): Collection from where data is fetched.
            fields (dict): Names of the columns (e.g. timestamp, measurement, sensor_name).

        Returns:
            dict: Data in a format suitable for matplotlib.
        """

        coll = self._db[collname]
        start_time = self.get_start_time(timespan)
        result = coll.find({fields['time']:{'$gt':start_time}},{ '_id': 0, fields['time']: 1, fields['value']: 1, fields['name']: 1 })
        data = [{fields['time']: row[fields['time']], 'value': row[fields['value']], 'name': row[fields['name']]} for row in result]
        return self._transform(data)
