import finnhub
import websocket
import json
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize API key
api_key = os.getenv("FINNHUB_API_KEY")
if not api_key:
    raise ValueError("API_KEY environment variable not set")

class StockWebSocketClient:
    def __init__(self, symbols):
        self.symbols = symbols
        self.url = f"wss://ws.finnhub.io?token={api_key}"
        self.ws = None

    def on_message(self, ws, message):
        print(f"Received message: {message}")
        # Here you can add code to process the message further if needed

    def on_error(self, ws, error):
        print(f"Error occurred: {error}")

    def on_close(self, ws):
        print("### WebSocket closed ###")

    def on_open(self, ws):
        print(f"Subscribing to symbols: {', '.join(self.symbols)}")
        for symbol in self.symbols:
            subscription_message = json.dumps({"type": "subscribe", "symbol": symbol})
            ws.send(subscription_message)

    def run(self):
        websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp(
            self.url,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close
        )
        self.ws.on_open = self.on_open
        self.ws.run_forever()

# Example usage
# symbols = ["AAPL"]
# ws_client = StockWebSocketClient(symbols=symbols)
# ws_client.run()
