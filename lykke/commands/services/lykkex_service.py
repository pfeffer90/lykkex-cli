import datetime
import logging as log

import lykkex

from lykke.commands.services.time_service import get_current_time


class LykkexService(object):
    @staticmethod
    def get_balance(api_key):
        log.info("Retrieve current balance.")
        time_stamp = get_current_time()
        balance = lykkex.get_balance(api_key)
        log.info("Number of assets: {}".format(len(balance)))
        for x in range(0, len(balance)):
            log.info(format('Current wealth ' + balance[x]['AssetId'].encode() + ': ' + str(balance[x]['Balance'])))
        return time_stamp, balance

    @staticmethod
    def get_pending_orders(api_key):
        log.info("Get pending orders.")
        time_stamp = get_current_time()
        pending_orders = lykkex.get_pending_orders(api_key)
        if not pending_orders:
            log.info("No pending orders")
        return time_stamp, pending_orders

    @staticmethod
    def send_market_order(api_key, asset_pair, asset, order_action, volume):
        log.info("Send market order - {}".format(asset))
        time_stamp = get_current_time()
        response = lykkex.send_market_order(api_key, asset_pair, asset, order_action, volume)
        if response['Error']:
            log.info("Error: Market order not successful")
            raise RuntimeError("Error in sending market order. Check response {}".format(response))
        final_price = response['Result']
        log.info("Trade successful at price {}".format(final_price))
        return time_stamp, final_price

    @staticmethod
    def send_limit_order(api_key, asset_pair, asset, price, order_action='BUY', volume='0.1'):
        log.info("Send market order - {}".format(asset))
        time_stamp = get_current_time()
        response = lykkex.send_limit_order(api_key, asset_pair, asset, price, order_action, volume)
        log.info("Limit order placed")
        order_id = str(response)
        return time_stamp, order_id

    @staticmethod
    def control_limit_order(api_key, order_id):
        log.info("Check status of limit order {}", order_id)
        time_stamp = get_current_time()
        content = lykkex.get_order_status(api_key, order_id)
        status = content['Status']
        return time_stamp, status

    @staticmethod
    def get_price(asset_pair_id, side='BUY'):
        log.info("Retrieve price: {}".format(side))
        time_stamp = get_current_time()
        order_book = lykkex.get_order_book(asset_pair_id)
        price = LykkexService.get_asset_price(order_book, side)
        volume = LykkexService.get_asset_trading_volume(order_book, side)

        log.info("Timestamp: {}".format(time_stamp))
        log.info("Price: {}".format(price))
        return time_stamp, price, volume

    def get_latency(self, asset_pair_id):
        time_stamp = get_current_time()
        order_book = lykkex.get_order_book(asset_pair_id)
        time_ob = self.get_time_stamp_from_order_books(order_book)
        time_delta = (time_stamp - time_ob).total_seconds()
        log.info("System latency: {} secs".format(time_delta))

    @staticmethod
    def get_asset_trading_volume(order_books, side):
        if side == 'BUY':
            return order_books[1]['Prices'][0]['Volume']
        elif side == 'SELL':
            return order_books[0]['Prices'][0]['Volume']
        else:
            return log.error('No valid input')

    @staticmethod
    def get_time_stamp_from_order_books(order_books):
        time_stamp_ob = order_books[1]['Timestamp']
        val = datetime.datetime.strptime(time_stamp_ob, '%Y-%m-%dT%H:%M:%S.%f')
        return val

    @staticmethod
    def get_asset_price(order_books, side):
        try:
            if side == 'BUY':
                price = order_books[1]['Prices'][-1]['Price']
            elif side == 'SELL':
                price = order_books[0]['Prices'][0]['Price']
        except IndexError as e:
            log.error("Could not extract price from order books.")
            log.error("{}".format(order_books))
            raise RuntimeError(e.message)
        return price

    def __init__(self):
        log.info("Initialize Lykkex connector.")
