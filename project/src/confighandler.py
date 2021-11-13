import yaml
from dashboard import Dashboard


class ConfigHandler:
    """Loads yaml files and creates dashboard objects"""

    def __init__(self, filepath) -> None:
        self.filepath = filepath
    
    def load(self) -> Dashboard:
        file = open(self.filepath, 'r')
        config = yaml.safe_load(file)

        return Dashboard(config['name'], config['timespan'], config['interval'], config['sources'], config['graphs'])
