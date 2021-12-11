import yaml


class ConfigHandler:
    """Handles loading from and saving to yaml files"""

    def __init__(self, filepath: str) -> None:
        """Creates a configuration handler object related to a particular dashboard configuration.

        Args:
            filepath (str): Path to the configuration file
        """

        # TODO: Validate path and throw error if invalid
        self._filepath = filepath
        self._changes = False

    @property
    def changes(self):
        return self._changes
    
    def clear_changes(self):
        self._changes = False

    def load(self) -> dict:
        """Loads configuration from a yaml file and returns it.

        Returns:
            dict: The resulting dashboard data object.
        """

        with open(self._filepath, 'r', encoding='utf8') as file:
            return yaml.safe_load(file)

    def save(self, config):
        """Saves configuration to a yaml file.
        """

        self._changes = True
        with open(self._filepath, 'w', encoding='utf8') as file:
            file.write(yaml.dump(config))
