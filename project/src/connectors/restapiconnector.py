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

    def _resolve_path(self, path, data):
        if len(path) == 1:
            return data[path[0]]
        else:
            return self._resolve_path(path[1:], data[path[0]])
    
    def get_data(self, path: str, fields: dict, timespan: int) -> dict:
        """Fetches data from the REST API.

        Args:
            endpoint (str): Endpoint appended to the address.
            fields (dict): Names of the columns (e.g. timestamp, measurement, sensor_name).

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
                    data.append({'time': start_time + i * fields['time'] * 1000,
                                 'value': float(row[values[j]]),
                                 'name': names[j]})
            return self._transform(data)
        except MissingSchema:
            raise ConnectorConfigurationError('URL missing http(s)')
        except ConnectionError:
            raise ConnectorConfigurationError('cannot connect to URL')
