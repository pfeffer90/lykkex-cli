"""The limit_order command."""
import services.lykkex_service as ly
from lykke.commands import log_and_print
from lykke.commands import validate_order_action, logging
from .base import Base


class LimitOrder(Base):
    """Send a limit order"""

    def run(self):
        config_service = self.kwargs["config_service"]

        action = self.options["<action>"]
        validate_order_action(action)

        asset_pair_id = self.options["<asset_pair_id>"]
        asset = self.options["<asset>"]
        price = self.options["<price>"]
        volume = self.options["<volume>"]
        logging.info("lykkex limit_order {} {} {} {} {}".format(asset_pair_id, asset, action, price, volume))

        time_stamp, order_id = ly.LykkexService.send_limit_order(config_service.get_api_key(), asset_pair_id, asset,
                                                                    price, action, volume)
        log_and_print("Limit order placed with order id {}.".format(order_id))
