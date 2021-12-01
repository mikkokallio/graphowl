import yaml
from dashboard import Dashboard


class ConfigHandler:
    """Handles loading from and saving to yaml files"""

    def __init__(self, filepath: str) -> None:
        """Creates a configuration handler object related to a particular dashboard configuration.

        Args:
            filepath (str): Path to the configuration file
        """

        # TODO: Validate path and throw error if invalid
        self._filepath = filepath

    def load(self) -> dict:
        """Loads configuration from a yaml file and creates a dashboard from it.

        Returns:
            dict: The resulting dashboard data object.
        """

        with open(self._filepath, 'r', encoding='utf8') as file:
            return yaml.safe_load(file)
