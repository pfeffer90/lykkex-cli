"""The check_orders command."""
import logging

import services.lykkex_service as ly
from lykke.commands import log_and_print
from .base import Base


class CheckOrders(Base):
    """List all pending orders."""

    def run(self):
        config_service = self.kwargs["config_service"]
        logging.info("lykkex check_orders")
        time_stamp, pending_orders = ly.LykkexService.get_pending_orders(config_service.get_api_key())
        if not pending_orders:
            log_and_print("No pending order")
        else:
            log_and_print("{} pending orders:".format(len(pending_orders)))
            for idx, pending_order in enumerate(pending_orders):
                log_and_print("")
                log_and_print("# Pending order {:d}".format(idx))
                for k, v in pending_order.items():
                    log_and_print("{}: {}".format(k, v))

