"""The balance command."""
import logging

import services.lykkex_service as ly
from services.logging_service import log_and_print
from .base import Base


class Balance(Base):
    """Get lykkex balance"""

    def run(self):
        config_service = self.kwargs["config_service"]
        logging.info("lykkex balance")
        time_stamp, balances = ly.LykkexService.get_balance(config_service.get_api_key())
        for balance in balances:
            log_and_print('{}: {:10.4f}'.format(balance["AssetId"], balance["Balance"]))
