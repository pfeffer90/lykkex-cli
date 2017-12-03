import json
import os

import lykke.cli


class ConfigService(object):
    CONFIG_FILENAME = '.lykkerc'
    PATH_TO_CHECK = os.path.expanduser('~')
    API_KEY = 'API_KEY'
    LOGGING_DIR = 'LOGGING_DIR'

    def get_api_key(self):
        return self.config[ConfigService.API_KEY]

    def __init__(self):
        self.path_to_config_file = os.path.join(ConfigService.PATH_TO_CHECK, ConfigService.CONFIG_FILENAME)
        try:
            with open(self.path_to_config_file) as config_file:
                self.config = json.load(config_file)
        except IOError as err:
            print "Cannot find configuration file at {}".format(self.path_to_config_file)
            raise lykke.cli.LykkeCliError

    def get_logging_dir(self):
        return self.config[ConfigService.LOGGING_DIR]
