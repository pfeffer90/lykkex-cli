import lykke.cli
from lykke.commands import log_and_print


def validate_order_action(action):
    valid_order_actions = ["buy", "sell"]
    if action not in valid_order_actions:
        log_and_print("{} is not a valid order action. Choose from {}.".format(action, valid_order_actions))
        raise lykke.cli.LykkeCliError
