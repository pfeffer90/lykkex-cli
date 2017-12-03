"""The price command."""
import logging

import services.lykkex_service as ly
from lykke.commands.services.logging_service import log_and_print
from .base import Base


class Price(Base):
    """Get asset price"""

    def run(self):
        asset_pair_id = self.options["<asset_pair_id>"]
        logging.info("lykkex price {}".format(asset_pair_id))
        _, buy_price, buy_volume = ly.LykkexService.get_price(asset_pair_id, 'BUY')
        _, sell_price, sell_volume = ly.LykkexService.get_price(asset_pair_id, 'SELL')
        log_and_print("{}  Price   Volume".format(asset_pair_id))
        log_and_print("BUY:  {:10.4f} {:10.2f}".format(buy_price, buy_volume))
        log_and_print("SELL: {:10.4f} {:10.2f}".format(sell_price, -sell_volume))
