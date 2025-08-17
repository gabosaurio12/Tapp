from jproperties import Properties
import os

class DatabaseConfig:

    def __init__(self):
        self.configs = Properties()
        src_dir = os.path.dirname(os.path.dirname(__file__))
        self.file_path = os.path.join(src_dir, 'resources', 'database_config.properties')

    def load_properties(self):
        with open(self.file_path, 'rb') as config_file:
            self.configs.load(config_file)
        return self.configs