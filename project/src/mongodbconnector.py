import pymongo


class MongoDbConnector:
    """Establishes connection to MongoDb and loads data into appropriate format"""

    def __init__(self, uri: str, cert: str, db: str) -> None:
        """Creates a connection to a particular database in a MongoDb instance.

        Args:
            uri (str): Connection string for the database.
            cert (str): Path to authentication certificate.
            db (str): Database name.
        """

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
        
    def get_data(self, collname: str, time: str, value: str, name: str) -> dict:
        """Fetches data from the database.

        Args:
            collname (str): Collection from where data is fetched.
            time (str): Name of the timestamp (x) column.
            value (str): Name of the value (y) column.
            name (str): Name of the column plot name column.

        Returns:
            dict: Data in a format suitable for matplotlib.
        """

        coll = self._db[collname]
        result = coll.find({},{ '_id': 0, time: 1, value: 1, name: 1 })
        data = [{time: row[time], 'value': row[value], 'name': row[name]} for row in result]
        return self._transform(data)
