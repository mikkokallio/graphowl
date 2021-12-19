import io
import json
from datetime import datetime as dt
import requests
import pandas as pd
import xmltodict
from requests.exceptions import ConnectionError, MissingSchema
from connectors.connector import Connector, ConnectorConfigurationError
from services import resolve_path


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
        try:
            url = self._uri.replace('$TIME', start_dt)
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
            data = requests.get(url=url, headers=headers).text
            if 'parse' in self._trans:
                data = self._parse_xml_or_json(data, self._trans['parse'])
            if 'traverse' in self._trans:
                data = resolve_path(self._trans['traverse'].split(','), data)
            if 'format' in self._trans:
                data = self._parse_tabular_csv(data, fields, transformations)
            if 'pivot' in self._trans:
                data = data.pivot(index=fields['time'], columns=fields['name'], values=fields['value'])
            if 'timestep' in self._trans:
                n = data.shape[0]
                data.insert(0, 'time', [dt.fromtimestamp(start_time/1000 + i * self._trans['timestep']) for i in range(n)])
                data = data.set_index('time')
            return data
        except MissingSchema as error:
            raise ConnectorConfigurationError('URL missing http(s)') from error
        except ConnectionError as error:
            raise ConnectorConfigurationError('cannot connect to URL') from error
        except pd.errors.EmptyDataError as error:
            raise ConnectorConfigurationError('no columns to parse') from error
        except ValueError as error:
            raise ConnectorConfigurationError('column name(s) not found') from error
        except TypeError as error:
            raise ConnectorConfigurationError('cannot traverse path') from error

    def _parse_xml_or_json(self, data, parse):
        """Tries to parse as xml, then json"""
        if parse == 'xml':
            return xmltodict.parse(data)
        if parse == 'json':
            return json.loads(data)
        return data

    def _parse_tabular_csv(self, data, fields, tr):
        """Parse csv into a dataframe"""
        buffer = io.StringIO(data)
        if 'header' in self._trans and self._trans['header'] == 'add names':
            header = None
            names = self._trans['names'].split(',')
        else:
            header = 0
            names = None
        usecols = None if tr is None or 'keep_cols' not in tr else tr['keep_cols'].split(',')
        df = pd.read_csv(filepath_or_buffer = buffer, skipinitialspace=True, usecols=usecols,
                         sep=self._trans['delimiter'], names=names, header=header)
        return df
