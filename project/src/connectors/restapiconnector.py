from datetime import datetime as dt
import requests
from requests.exceptions import ConnectionError, MissingSchema
from connectors.connector import Connector, ConnectorConfigurationError


class RESTAPIConnector(Connector):
    """Fetches JSON data from a REST API"""

    def __init__(self, uri: str, transformations: dict, **kwargs) -> None:
        """Stores information for fetching data from the API.

        Args:
            uri (str): REST API's address.
        """

        super().__init__(uri)
        self._trans = transformations
        self._config = kwargs
    
    def get_data(self, path: str, fields: dict, transformations: dict, timespan: int) -> dict:
        """Fetches data from the REST API.

        Args:
            path (str): Comma-separated list to traverse to find the payload data.
            fields (dict): Additional configuration to find the data.

        Returns:
            dict: Data in a format suitable for matplotlib.
        """
        start_time = self._get_start_time(timespan)
        start_dt = str(dt.fromtimestamp(start_time/1000)).replace(' ', 'T').split('.')[0]
        cols = transformations['keep_cols']
        usecols = cols.split(',') if len(cols)>0 else None
        try:
            url = self._uri.replace('$TIME', start_dt)
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
            data = requests.get(url=url, headers=headers).text
            return self._apply_transformations(data, usecols, fields, start_time)
        except MissingSchema as error:
            raise ConnectorConfigurationError('URL missing http(s)') from error
        except ConnectionError as error:
            raise ConnectorConfigurationError('cannot connect to URL') from error
