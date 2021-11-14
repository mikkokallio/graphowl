import pymongo


class MongoDbConnector:
    """Establishes connection to a particular database of a particular MongoDb instance and loads data into appropriate format"""

    def __init__(self, uri: str, cert: str, db: str) -> None:
        self._client = pymongo.MongoClient(uri, tls=True, tlsCertificateKeyFile=cert)
        self._db = self._client[db]

    def _transform(self, data) -> dict[str, tuple[list, list]]:
        plots = {row['name']:([],[]) for row in data}
        for row in data:
            plots[row['name']][0].append(row['time'])
            plots[row['name']][1].append(row['value'])
        return plots
        
    def get_data(self, collname: str, time: str, value: str, name: str) -> str:
        coll = self._db[collname]
        result = coll.find({},{ '_id': 0, time: 1, value: 1, name: 1 })
        data = [{time: row[time], 'value': row[value], name: row[name]} for row in result]
        return self._transform(data)
