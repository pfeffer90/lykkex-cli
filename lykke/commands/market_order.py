"""The market_order command."""
import logging

import services.lykkex_service as ly
from services.validator_service import validate_order_action
from services.logging_service import log_and_print
from .base import Base


class MarketOrder(Base):
    """Send a market order"""

    def run(self):
        config_service = self.kwargs["config_service"]

        action = self.options["<action>"]
        validate_order_action(action)

        asset_pair_id = self.options["<asset_pair_id>"]
        asset = self.options["<asset>"]
        volume = self.options["<volume>"]

        logging.info("lykkex market_order {} {} {} {}".format(asset_pair_id, asset, action, volume))

        time_stamp, final_price = ly.LykkexService.send_market_order(config_service.get_api_key(), asset_pair_id, asset, action, volume)
        log_and_print("Market order settled at price {}.".format(final_price))
