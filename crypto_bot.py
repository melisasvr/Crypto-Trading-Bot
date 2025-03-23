from dotenv import load_dotenv
import os
import ccxt
import pandas as pd
import numpy as np
import time
from ta.trend import SMAIndicator

load_dotenv()
API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
TIMEFRAME = '1m'
LIMIT = 50
MAX_TRADES = 50

# 50 USDT trading pairs (popular and testnet-supported)
SYMBOLS = [
    'BTC/USDT', 'ETH/USDT', 'XRP/USDT', 'SOL/USDT', 'ADA/USDT', 'BNB/USDT', 'DOT/USDT', 'LINK/USDT', 'LTC/USDT', 'BCH/USDT',
    'DOGE/USDT', 'SHIB/USDT', 'AVAX/USDT', 'TRX/USDT', 'UNI/USDT', 'ALGO/USDT', 'XLM/USDT', 'VET/USDT', 'ICP/USDT', 'FIL/USDT',
    'ETC/USDT', 'ATOM/USDT', 'FTM/USDT', 'HBAR/USDT', 'EGLD/USDT', 'XTZ/USDT', 'MANA/USDT', 'SAND/USDT', 'THETA/USDT', 'GALA/USDT',
    'NEAR/USDT', 'AAVE/USDT', 'AXS/USDT', 'CRV/USDT', 'ENJ/USDT', 'CHZ/USDT', 'YFI/USDT', 'MKR/USDT', 'COMP/USDT', 'SUSHI/USDT',
    '1INCH/USDT', 'KSM/USDT', 'ZEC/USDT', 'DASH/USDT', 'WAVES/USDT', 'OMG/USDT', 'QTUM/USDT', 'BAT/USDT', 'ZIL/USDT', 'NEO/USDT'
]

# Trade amounts per coin (adjusted for value)
TRADE_AMOUNTS = {coin.split('/')[0]: 0.001 if coin.split('/')[0] in ['BTC', 'ETH', 'BNB', 'LTC', 'BCH'] else 0.1 if coin.split('/')[0] in ['SOL', 'ADA', 'DOT', 'LINK'] else 1.0 for coin in SYMBOLS}

exchange = ccxt.binance({
    'apiKey': API_KEY,
    'secret': API_SECRET,
    'enableRateLimit': True,
})
exchange.set_sandbox_mode(True)

trade_history = {symbol: [] for symbol in SYMBOLS}

def fetch_data(symbol):
    try:
        ohlcv = exchange.fetch_ohlcv(symbol, TIMEFRAME, limit=LIMIT)
        df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        return df
    except Exception as e:
        print(f"Failed to fetch data for {symbol}: {e}")
        return None

def analyze_data(df):
    df['SMA_short'] = SMAIndicator(df['close'], window=3).sma_indicator()
    df['SMA_long'] = SMAIndicator(df['close'], window=10).sma_indicator()
    df.loc[1:, 'signal'] = np.where(df['SMA_short'][1:] > df['SMA_long'][1:], 1, 0)
    df['position'] = df['signal'].diff()
    return df

def execute_trade(symbol, action, price):
    timestamp = pd.Timestamp.now()
    coin = symbol.split('/')[0]
    amount = TRADE_AMOUNTS[coin]
    if action == 'buy':
        trade_entry = f"Buy {amount} {coin} at {price} on {timestamp}"
        print(trade_entry)
    elif action == 'sell':
        trade_entry = f"Sell {amount} {coin} at {price} on {timestamp}"
        print(trade_entry)
    trade_history[symbol].append(trade_entry)
    if len(trade_history[symbol]) > MAX_TRADES:
        trade_history[symbol].pop(0)

def withdraw_to_wallet(crypto, amount, address):
    try:
        exchange.withdraw(crypto, amount, address, tag=None)
        print(f"Withdrew {amount} {crypto} to {address}")
    except Exception as e:
        print(f"Withdrawal failed: {e}")

def main():
    print("Starting Multi-Coin Crypto Trading Bot (50 Coins)...")
    cycle_count = 0
    while True:
        try:
            for symbol in SYMBOLS:
                print(f"\nProcessing {symbol}")
                df = fetch_data(symbol)
                if df is None or df.empty:
                    continue
                df = analyze_data(df)
                latest_position = df['position'].iloc[-1]
                latest_price = df['close'].iloc[-1]
                
                print(f"Latest Price: {latest_price}")
                print(f"SMA Short: {df['SMA_short'].iloc[-1]}, SMA Long: {df['SMA_long'].iloc[-1]}")
                print(f"Signal: {df['signal'].iloc[-1]}, Position: {latest_position}")
                print(f"Last Timestamp: {df['timestamp'].iloc[-1]}")

                if latest_position == 1:
                    execute_trade(symbol, 'buy', latest_price)
                elif latest_position == -1:
                    execute_trade(symbol, 'sell', latest_price)

                print(f"\nRecent Trades for {symbol} (Last 5):")
                for trade in trade_history[symbol][-5:]:
                    print(trade)

            # Wallet withdrawal prompt every 60 seconds
            cycle_count += 1
            if cycle_count % 60 == 0:
                try:
                    coin = input("\nEnter coin to withdraw (e.g., BTC, ETH, XRP) or 'skip': ").upper()
                    if coin == 'SKIP':
                        print("Skipping withdrawal...")
                    elif coin in [s.split('/')[0] for s in SYMBOLS]:
                        amount = float(input(f"Enter {coin} amount to withdraw: "))
                        address = input(f"Enter wallet address for {coin}: ")
                        withdraw_to_wallet(coin, amount, address)
                    else:
                        print("Invalid coin!")
                except ValueError:
                    print("Invalid amount entered!")

            print("\nWaiting for next cycle...")
            time.sleep(2)  # 2s sleep for 50 coins

        except Exception as e:
            print(f"Error: {e}")
            time.sleep(2)

if __name__ == "__main__":
    main()