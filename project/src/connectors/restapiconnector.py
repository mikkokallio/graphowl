import requests
from datetime import datetime as dt
import xmltodict
from requests.exceptions import ConnectionError, MissingSchema
from connectors.connector import Connector, ConnectorConfigurationError
from services import resolve_path


class RESTAPIConnector(Connector):
    """Fetches JSON data from a REST API"""

    def __init__(self, uri: str, **kwargs) -> None:
        """Stores information for fetching data from the API.

        Args:
            uri (str): REST API's address.
        """

        super().__init__(uri)
        self._config = kwargs
    
    def get_data(self, path: str, fields: dict, timespan: int) -> dict:
        """Fetches data from the REST API.

        Args:
            path (str): Comma-separated list to traverse to find the payload data.
            fields (dict): Additional configuration to find the data.

        Returns:
            dict: Data in a format suitable for matplotlib.
        """
        start_time = self._get_start_time(timespan)
        start_dt = str(dt.fromtimestamp(start_time/1000)).replace(' ', 'T').split('.')[0]
        try:
            res = requests.get(url=self._uri.replace('$TIME', start_dt)).text
            parsed = xmltodict.parse(res)
            timeseries = resolve_path(path.split(','), parsed)
            rows = [row.strip() for row in timeseries.split('\n')]
            result = [col.split(' ') for col in rows]
            data = []
            for i, row in enumerate(result):
                values = [int(value) for value in str(fields['value']).split(',')]
                names = fields['name'].split(',')
                for j in range(len(values)):
                    data.append({'time': start_time + i * int(fields['time']) * 1000,
                                 'value': float(row[values[j]]),
                                 'name': names[j]})
            return self._transform(data)
        except MissingSchema:
            raise ConnectorConfigurationError('URL missing http(s)')
        except ConnectionError:
            raise ConnectorConfigurationError('cannot connect to URL')
