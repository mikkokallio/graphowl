import pymongo


class MongoDbConnector:
    """Establishes connection to a particular database of a particular MongoDb instance and loads data into appropriate format"""

    def __init__(self, uri, cert, db) -> None:
        self.client = pymongo.MongoClient(uri, tls=True, tlsCertificateKeyFile=cert)
        self.db = self.client[db]

    def transform(self, data):
        plots = {row['name']:([],[]) for row in data}
        for row in data:
            plots[row['name']][0].append(row['time'])
            plots[row['name']][1].append(row['value'])
        return plots
        
    def get_data(self, colname: str, time: str, value: str, name: str) -> str:
        coll = self.db[colname]
        result = coll.find({},{ '_id': 0, time: 1, value: 1, name: 1 })
        rawdata = [{time: row[time], 'value': row[value], name: row[name]} for row in result]
        pre_processed = sorted(rawdata, key=lambda row: row['name'])
        return self.transform(pre_processed)

    def get_names(self) -> list:
        """Get the names of all time series in the graph"""
        return [series['name'] for series in self.series]

    def inith(self, jsn) -> None:
        """Instantiate a time series from json"""
        self.series = []
