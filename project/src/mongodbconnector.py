import pymongo


class MongoDbConnector:
    """Establishes connection to a particular database of a particular MongoDb instance"""

    def __init__(self, uri, cert, db) -> None:
        self.client = pymongo.MongoClient(uri, tls=True, tlsCertificateKeyFile=cert)
        self.db = self.client[db]
        
    def get_data(self, colname) -> str:
        col = self.db[colname]

        return col.find()
