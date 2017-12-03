"""The price command."""

import services.lykkex_service as ly
from .base import Base


class Price(Base):
    """Get asset price"""

    def run(self):
        asset_id = self.options["<asset_id>"]
        _, buy_price, buy_volume = ly.LykkexService.get_price(asset_id, 'BUY')
        _, sell_price, sell_volume = ly.LykkexService.get_price(asset_id, 'SELL')
        print("{}  Price   Volume".format(asset_id))
        print("BUY:  {:10.4f} {:10.2f}".format(buy_price, buy_volume))
        print("SELL: {:10.4f} {:10.2f}".format(sell_price, -sell_volume))
