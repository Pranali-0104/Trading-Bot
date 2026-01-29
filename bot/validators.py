def validate(symbol, side, order_type, quantity, price):
    if not symbol or not symbol.endswith("USDT"):
        raise ValueError("Symbol must be like BTCUSDT")

    side = side.upper()
    if side not in {"BUY", "SELL"}:
        raise ValueError("Side must be BUY or SELL")

    order_type = order_type.upper()
    if order_type not in {"MARKET", "LIMIT"}:
        raise ValueError("Order type must be MARKET or LIMIT")

    if quantity <= 0:
        raise ValueError("Quantity must be > 0")

    if order_type == "LIMIT" and price is None:
        raise ValueError("Price is required for LIMIT orders")

    return side, order_type
