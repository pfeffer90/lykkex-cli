"""
lykkex

Usage:
  lykkex balance
  lykkex price <asset_pair_id>
  lykkex market_order <asset_pair_id> <asset> <action> <volume>
  lykkex limit_order <asset_pair_id> <asset> <action> <price> <volume>
  lykkex check_orders
  lykkex -h | --help
  lykkex --version

Options:
  -h --help                         Show this screen.
  --version                         Show version.

Examples:
  lykkex balance

Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/pfeffer90/lykkex-cli
"""

import logging as log
import os
from inspect import getmembers, isclass
from logging import handlers as log_handlers

from docopt import docopt

from lykke.commands.services.config_service import ConfigService
from . import __version__ as VERSION


class LykkeCliError(BaseException):
    pass


def configure_logging(logging_dir):
    logging_level = log.INFO

    logging_path = os.path.abspath(logging_dir)
    if not os.path.exists(logging_path):
        os.makedirs(logging_path)
    path_to_logging_file = os.path.join(logging_path, 'lykkex-cli.log')

    logging_format = '%(asctime)s %(levelname)s: %(message)s'
    date_format = '%Y-%m-%d %H:%M:%S'
    log.basicConfig(filename=path_to_logging_file, format=logging_format, datefmt=date_format, level=logging_level)


def main():
    """Main CLI entrypoint."""
    import lykke.commands
    options = docopt(__doc__, version=VERSION)
    try:
        config_service = ConfigService()
        configure_logging(config_service.get_logging_dir())

        log.info("")
        log.info("# lykkex call start #")
        # Here we'll try to dynamically match the command the user is trying to run
        # with a pre-defined command class we've already created.
        # Note that the below procedure assumes that the command files only hold two classes the base class and the command class, so that importing other classes destroys the scheme.
        for (k, v) in options.items():
            if hasattr(lykke.commands, k) and v:
                module = getattr(lykke.commands, k)
                lykke.commands = getmembers(module, isclass)
                command = [command[1] for command in lykke.commands if command[0] != 'Base'][0]
                command = command(options, config_service=config_service)
                command.run()
        log.info("# lykkex call end #")
        log.info("")
    except LykkeCliError as err:
        print err
        print "Check out lykke -h"
