"""The balance command."""
import services.lykkex_service as ly
from .base import Base


class Balance(Base):
    """Get lykkex balance"""

    def run(self):
        config_service = self.kwargs["config_service"]
        time_stamp, balances = ly.LykkexService.get_balance(config_service.get_api_key())
        for balance in balances:
            print('{}: {:10.4f}'.format(balance["AssetId"], balance["Balance"]))
