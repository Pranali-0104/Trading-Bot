# Binance Futures Testnet Trading Bot
This project is a simplified but production-minded trading bot for Binance Futures Testnet (USDT-M).

It supports placing MARKET and LIMIT orders via a clean CLI, with:
- strict input validation
- structured logging of all API requests and responses
- robust error handling
- separation of concerns (CLI, client, validation, order logic)

**Bonus – Safety Layer**
Before any order is sent, the bot performs a pre-flight analysis using the live mark price:
- computes notional value (price × quantity)
- calculates price deviation for LIMIT orders
- warns about risky or abnormal orders
- requires explicit user confirmation before execution

This mimics real-world trading systems that protect against fat-finger errors and unsafe trades.

## Setup
python -m venv venv
source venv/bin/activate  # windows: venv\Scripts\activate
pip install -r requirements.txt


