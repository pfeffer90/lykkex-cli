"""
lykkex

Usage:
  lykkex balance
  lykkex price <asset_id>
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

from inspect import getmembers, isclass

from docopt import docopt

from lykke.commands.services.config_service import ConfigService
from . import __version__ as VERSION


class LykkeCliError(BaseException):
    pass


def main():
    """Main CLI entrypoint."""
    import lykke.commands
    options = docopt(__doc__, version=VERSION)
    try:
        config_service = ConfigService()
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
    except LykkeCliError as err:
        print "Check out lykke -h"