import io
import time
import json
from datetime import datetime as dt
import pandas as pd
import xmltodict
from services import resolve_path


class Connector:
    """Abstract connector class for actual connectors to inherit"""

    def __init__(self, uri: str, **kwargs):
        self._uri = uri
        self._config = kwargs

    def _get_start_time(self, timespan: int) -> int:
        return 1000 * (time.time()-timespan) if timespan is not None else 0

    def _parse_xml_or_json(self, data, parse):
        """Tries to parse as xml, then json"""
        if parse == 'xml':
            return xmltodict.parse(data)
        if parse == 'json':
            return json.loads(data)
        return data

    def _parse_tabular_csv(self, data, usecols):
        """Parse csv into a dataframe"""
        buffer = io.StringIO(data)
        if 'header' in self._trans and self._trans['header'] == 'add names':
            header = None
            names = self._trans['names'].split(',')
        else:
            header = 0
            names = None
        usecols = None if 'pivot' in self._trans else usecols
        df = pd.read_csv(filepath_or_buffer = buffer, skipinitialspace=True, usecols=usecols,
                         sep=self._trans['delimiter'], names=names, header=header)
        return df

    def _apply_transformations(self, data, usecols, fields, start_time):
        try:
            if 'parse' in self._trans:
                data = self._parse_xml_or_json(data, self._trans['parse'])
            if 'traverse' in self._trans:
                data = resolve_path(self._trans['traverse'].split(','), data)
            if 'format' in self._trans:
                data = self._parse_tabular_csv(data, usecols)
            if 'pivot' in self._trans:
                data = data.pivot(index=fields['time'], columns=fields['name'], values=fields['value'])
                if usecols:
                    data = data[usecols]
            if 'timestep' in self._trans:
                n = data.shape[0]
                data.insert(0, 'time', [dt.fromtimestamp(start_time/1000 + i * self._trans['timestep']) for i in range(n)])
                data = data.set_index('time')
            return data
        except pd.errors.EmptyDataError as error:
            raise ConnectorConfigurationError('no columns to parse') from error
        except ValueError as error:
            raise ConnectorConfigurationError('column name(s) not found') from error
        except TypeError as error:
            raise ConnectorConfigurationError('cannot traverse path') from error
        except KeyError as error:
            raise ConnectorConfigurationError('invalid plot names') from error

    def _transform(self, data: dict) -> dict:
        """Transforms raw data into a dict to show in a graph.

        Args:
            data (dict): Raw data fetched from data source.

        Returns:
            dict[str, tuple[list, list]]: A dictionary with a tuple for each plot,
            which in turn contains an array for x and y coordinates each.
        """

        plots = {row['name']:([],[]) for row in data}
        for row in data:
            plots[row['name']][0].append(dt.fromtimestamp(row['time']/1000))
            plots[row['name']][1].append(row['value'])
        return plots

    def get_data(self, *args):
        return {'plot1': ([1,2,3,4],[1,2,3,4]), 'plot2': ([1,2,3,4],[4,3,2,1])}

class ConnectorConfigurationError(Exception):
    """Connector uri or other attributes are misconfigured"""
