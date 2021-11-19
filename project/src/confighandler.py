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
        
        file = open(self.filepath, 'r')
        config = yaml.safe_load(file)

        return Dashboard(config['name'], config['layout'], config['timespan'], config['interval'], config['sources'], config['graphs'])
