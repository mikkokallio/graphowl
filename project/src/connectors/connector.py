import io
import time
import json
from datetime import datetime as dt
import pandas as pd
import xmltodict
from services import resolve_path


class Connector:
    """Abstract connector class for actual connectors to inherit"""

    def __init__(self, uri: str, transformations: dict, **kwargs):
        self._uri = uri
        self._trans = transformations
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

    def _parse_tabular_csv(self, data, usecols, names, header):
        """Parse csv into a dataframe"""
        buffer = io.StringIO(data)
        usecols = None if 'pivot' in self._trans and self._trans['pivot'] == 'yes' else usecols
        return pd.read_csv(filepath_or_buffer = buffer, skipinitialspace=True, usecols=usecols,
                           sep=self._trans['delimiter'], names=names, header=header)

    def _apply_transformations(self, data, trans, fields, start_time):
        present = lambda key : key in self._trans and self._trans[key] is not None and len(str(self._trans[key])) > 0
        try:
            if trans is not None and 'keep_cols' in trans and trans['keep_cols'] is not None and len(str(trans['keep_cols'])) > 0:
                usecols = trans['keep_cols'].split(',')
            else:
                usecols = None
            if present('parse'):
                data = self._parse_xml_or_json(data, self._trans['parse'])
            if present('traverse'):
                data = resolve_path(self._trans['traverse'].split(','), data)
            if 'header' in self._trans and self._trans['header'] == 'add names':
                names = self._trans['names'].replace('$VALUE', fields['value']).split(',')
                header = None
            else:
                header = 0
                names = None
            if present('format') and self._trans['format'] == 'csv':
                data = self._parse_tabular_csv(data, usecols, names, header)
            else:
                data = pd.DataFrame.from_records(data, columns=names)
            if present('time_format'):
                if self._trans['time_format'] == 'milliseconds':
                    data[fields['time']] = data[fields['time']].div(1000000)
            if present('pivot') and self._trans['pivot'] == 'yes':
                data = data.pivot(index=fields['time'],
                                  columns=fields['name'],
                                  values=fields['value'])
                if usecols:
                    data = data[usecols]
            if present('timestep'):
                n = data.shape[0]
                dtime = lambda i : dt.fromtimestamp(start_time/1000 + i * self._trans['timestep'])
                data.insert(0, 'time', [dtime(i) for i in range(n)])
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

    def get_data(self, *args):
        """A dummy implementation of the method for testing.

        Returns:
            DataFrame: An empty pandas dataframe, can be used for testing.
        """
        return pd.DataFrame()

class ConnectorConfigurationError(Exception):
    """Connector uri or other attributes are misconfigured"""
