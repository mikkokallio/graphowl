import yaml
from dashboard import Dashboard


class ConfigHandler:
    """Loads yaml files and creates dashboard objects"""

    def __init__(self, filepath: str) -> None:
        """Creates a configuration handler object related to a particular dashboard configuration.

        Args:
            filepath (str): Path to the configuration file
        """

        self.filepath = filepath

    def load(self) -> Dashboard:
        """Loads configuration from a yaml file and creates a dashboard from it.

        Returns:
            Dashboard: The resulting dashboard data object.
        """

        with open(self.filepath, 'r', encoding='utf8') as file:
            config = yaml.safe_load(file)
            return Dashboard(**config)
