import logging
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException

log = logging.getLogger("bot.client")

class BinanceFuturesClient:
    def __init__(self, api_key: str, api_secret: str):
        self.client = Client(api_key, api_secret, testnet=True)
        self.client.FUTURES_URL = "https://testnet.binancefuture.com"
        log.info("Initialized Binance Futures Testnet client")

    def create_order(self, **kwargs):
        try:
            log.info(f"Order request: {kwargs}")
            resp = self.client.futures_create_order(**kwargs)
            log.info(f"Order response: {resp}")
            return resp
        except (BinanceAPIException, BinanceRequestException) as e:
            log.error(f"Binance error: {e}")
            raise
        except Exception as e:
            log.exception("Unexpected error")
            raise

    def get_mark_price(self, symbol: str) -> float:
        data = self.client.futures_mark_price(symbol=symbol)
        return float(data["markPrice"])

