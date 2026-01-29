import argparse
import os
import sys
from bot.logging_config import setup_logging
from bot.client import BinanceFuturesClient
from bot.validators import validate
from bot.orders import place_order

def main():
    setup_logging()

    parser = argparse.ArgumentParser(description="Binance Futures Testnet Bot")
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True, dest="order_type")
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        side, order_type = validate(
            args.symbol, args.side, args.order_type, args.quantity, args.price
        )
    except Exception as e:
        print(f"Validation error: {e}")
        sys.exit(1)

    key = os.getenv("BINANCE_API_KEY")
    secret = os.getenv("BINANCE_API_SECRET")
    if not key or not secret:
        print("Set BINANCE_API_KEY and BINANCE_API_SECRET")
        sys.exit(1)

    client = BinanceFuturesClient(key, secret)

    try:
        summary = place_order(
            client,
            args.symbol,
            side,
            order_type,
            args.quantity,
            args.price,
        )
        print("\nOrder Placed Successfully")
        print(summary)
    except Exception as e:
        print(f"Order failed: {e}")
        sys.exit(2)

if __name__ == "__main__":
    main()
