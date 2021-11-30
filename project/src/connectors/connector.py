import time


class Connector:
    """Abstract connector class for actual connectors to inherit"""

    def __init__(self, name: str, uri: str, **kwargs):
        self.name = name
        self.uri = uri

    def _get_start_time(self, timespan: int) -> int:
        return 1000 * (time.time()-timespan) if timespan is not None else 0

    def _transform(self, data: dict) -> dict:
        """Transforms raw MongoDb data into a dict to show in a graph.

        Args:
            data (dict): Raw data fetched from MongoDb.

        Returns:
            dict[str, tuple[list, list]]: A dictionary with a tuple for each plot,
            which in turn contains an array for x and y coordinates each.
        """

        plots = {row['name']:([],[]) for row in data}
        for row in data:
            plots[row['name']][0].append(row['time'])
            plots[row['name']][1].append(row['value'])
        return plots

    def get_data(self, *args):
        return {'plot1': ([1,2,3,4],[1,2,3,4]), 'plot2': ([1,2,3,4],[4,3,2,1])}
