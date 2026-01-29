import logging

log = logging.getLogger("bot.orders")

def place_order(client, symbol, side, order_type, quantity, price=None):
    mark_price = client.get_mark_price(symbol)
    notional = mark_price * quantity

    print("\nOrder Preview")
    print("--------------")
    print(f"Symbol: {symbol}")
    print(f"Side: {side}")
    print(f"Type: {order_type}")
    print(f"Quantity: {quantity}")
    print(f"Current Mark Price: {mark_price:.2f}")
    print(f"Notional Value: {notional:.2f} USDT")

    if order_type == "LIMIT":
        deviation = ((price - mark_price) / mark_price) * 100
        print(f"Limit Price: {price}")
        print(f"Price Deviation: {deviation:.2f}%")

        if abs(deviation) > 20:
            print("⚠️ Warning: Limit price is more than 20% away from market.")

    if notional < 100:
        print("⚠️ Warning: Notional value below 100 USDT.")

    confirm = input("\nProceed with order? (y/N): ").strip().lower()
    if confirm != "y":
        raise RuntimeError("Order aborted by user")

    payload = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "quantity": quantity,
    }

    if order_type == "LIMIT":
        payload["price"] = price
        payload["timeInForce"] = "GTC"

    resp = client.create_order(**payload)

    summary = {
        "orderId": resp.get("orderId"),
        "status": resp.get("status"),
        "executedQty": resp.get("executedQty"),
        "avgPrice": resp.get("avgPrice"),
    }

    log.info(f"Order summary: {summary}")
    return summary
