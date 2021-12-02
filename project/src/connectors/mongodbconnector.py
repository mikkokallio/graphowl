import pymongo
from connectors.connector import Connector


class MongoDbConnector(Connector):
    """Establishes connection to MongoDb and loads data into appropriate format"""

    def __init__(self, uri: str, cert: str, database: str, **kwargs) -> None:
        """Creates a connection to a particular database in a MongoDb instance.

        Args:
            uri (str): Connection string for the database.
            cert (str): Path to authentication certificate.
            database (str): Database name.
        """

        super().__init__(uri)
        self._config = kwargs
        if cert is None:
            client = pymongo.MongoClient(uri, tls=False)
        else:
            client = pymongo.MongoClient(uri, tls=True, tlsCertificateKeyFile=f'certs/{cert}')
        self._db = client[database]

    def get_data(self, collname: str, fields: dict, timespan: int) -> dict:
        """Fetches data from the database.

        Args:
            collname (str): Collection from where data is fetched.
            fields (dict): Names of the columns (e.g. timestamp, measurement, sensor_name).

        Returns:
            dict: Data in a format suitable for matplotlib.
        """

        coll = self._db[collname]
        start_time = self._get_start_time(timespan)
        result = coll.find({fields['time']:{'$gt':start_time}},{ '_id': 0, fields['time']: 1, fields['value']: 1, fields['name']: 1 })
        data = [{fields['time']: row[fields['time']], 'value': row[fields['value']], 'name': row[fields['name']]} for row in result]
        return self._transform(data)
