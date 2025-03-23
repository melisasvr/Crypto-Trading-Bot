# Crypto Trading Bot

A Python-based trading bot that monitors and trades 50 cryptocurrency pairs on Binance’s testnet using a simple moving average (SMA) crossover strategy. It includes a wallet withdrawal feature and logs trades in the console.

## Features
- **50 Coins**: Trades 50 popular USDT pairs (e.g., BTC/USDT, ETH/USDT, XRP/USDT).
- **SMA Strategy**: Buys when the 3-period SMA crosses above the 10-period SMA; sells when it crosses below.
- **Wallet Withdrawals**: Prompts every 60 seconds to withdraw funds to an external wallet.
- **Console Output**: Displays price, SMAs, signals, and recent trades for each coin.

## Prerequisites
- Python 3.7+
- Binance testnet account (get API keys from [Binance Testnet](https://testnet.binance.vision/))
- Dependencies:
  - `ccxt`: For Binance API interaction
  - `pandas`: For data handling
  - `numpy`: For calculations
  - `ta`: For technical indicators
  - `python-dotenv`: For environment variables

## Installation
1. **Clone the Repository** (or save the script as `trading_bot.py`):
   ```bash
   git clone <repo-url>
   cd <repo-folder>

2. Install Dependencies
- pip install ccxt pandas numpy ta python-dotenv
  
3. Set Up Environment Variables
- Create a `.env` file in the project directory:
- API_KEY=your_binance_testnet_api_key
- API_SECRET=your_binance_testnet_api_secret
- Replace your_binance_testnet_api_key and your_binance_testnet_api_secret with your Binance testnet credentials.

## Usage
1. Run the Bot:
- python trading_bot.py
- The bot starts in Binance testnet mode and processes 50 coins every 2 seconds.
2. Monitor Output:
- Example output for NEAR/USDT
- Processing NEAR/USDT
- Latest Price: 2.752
- SMA Short: 2.752333333333333, SMA Long: 2.7541
- Signal: 0.0, Position: 0.0
- Last Timestamp: 2025-03-23 01:47:00
- Recent Trades for NEAR/USDT (Last 5):
- Sell 1.0 NEAR at 2.754 on 2025-03-22 18:46:19.695456
- Sell 1.0 NEAR at 2.754 on 2025-03-22 18:46:33.962376
- Sell 1.0 NEAR at 2.752 on 2025-03-22 18:46:47.686629
- Sell 1.0 NEAR at 2.752 on 2025-03-22 18:47:02.592059

3. Withdraw Funds:
- Every 60 seconds, you’ll see:
- Enter coin to withdraw (e.g., BTC, ETH, XRP) or 'skip':
- Enter a coin (e.g., `XRP`), amount (e.g., `1.0`), and testnet wallet address, or type `skip`.

4. Stop the Bot:
- Press `Ctrl+C` to exit.

## Configuration
- Coins: Edit the SYMBOLS list in trading_bot.py to change the 50 pairs.
- Trade Amounts: Adjust TRADE_AMOUNTS for custom quantities (e.g., 0.001 BTC, 0.1 SOL, 1.0 XRP).
- Timeframe: Change TIMEFRAME (default: 1m) to 5m, 15m, etc., if desired.
- SMA Periods: Modify window=3 and window=10 in analyze_data() for different SMA lengths.

## Notes
- Testnet Mode: Runs in sandbox mode. For live trading, remove exchange.set_sandbox_mode(True) and use real API keys (use caution!).
- Rate Limits: 2-second sleep avoids Binance API limits for 50 coins.
- Errors: If a coin fails (e.g., unavailable on testnet), it skips to the next one.

### Sample Output: 
- Starting Multi-Coin Crypto Trading Bot (50 Coins)...
-  Processing CHZ/USDT
-  Latest Price: 0.0456
-  SMA Short: 0.0456, SMA Long: 0.045599999999999995
- Signal: 1.0, Position: 1.0
- Last Timestamp: 2025-03-23 01:47:00
-  Buy 1.0 CHZ at 0.0456 on 2025-03-22 18:47:33.084424

- Recent Trades for CHZ/USDT (Last 5):
- Sell 1.0 CHZ at 0.0456 on 2025-03-22 18:45:37.390387
- Sell 1.0 CHZ at 0.0456 on 2025-03-22 18:45:51.138412
- Sell 1.0 CHZ at 0.0456 on 2025-03-22 18:46:06.500460
- Buy 1.0 CHZ at 0.0456 on 2025-03-22 18:47:18.266573
- Buy 1.0 CHZ at 0.0456 on 2025-03-22 18:47:33.084424

- Waiting for next cycle... 


## Troubleshooting
- API Errors: Check .env for correct keys and testnet connectivity.
- No Trades: Testnet data may be static, so try live mode or fewer coins.
- Performance: Increase time.sleep(2) if rate-limited.

## License
- MIT License—feel free to modify and share!






