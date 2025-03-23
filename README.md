# Crypto Trading Bot

A Python-based trading bot that monitors and trades 50 cryptocurrency pairs on Binance using a simple moving average (SMA) crossover strategy with real funds. It includes a wallet withdrawal feature and logs trades in the console.

## Features
- **50 Coins**: Trades 50 popular USDT pairs (e.g., BTC/USDT, ETH/USDT, XRP/USDT).
- **SMA Strategy**: Buys when the 3-period SMA crosses above the 10-period SMA; sells when it crosses below.
- **Wallet Withdrawals**: Prompts every 60 seconds to withdraw funds to an external wallet.
- **Console Output**: Displays price, SMAs, signals, and recent trades for each coin.

## Prerequisites
- Python 3.7+
- Binance account with API keys (create at [Binance API Management](https://www.binance.com/en/my/settings/api-management))
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
- API_KEY=your_binance_api_key
- API_SECRET=your_binance_api_se-
cret
- Replace your_binance_api_key and your _binance_api_secret with your live Binance API credentials.
- Ensure the API has trading and withdrawal permissions enabled.

## Usage
1. Modify the Code for Live Trading:
- Open trading_bot.py and remove or comment out this line:
- exchange.set_sandbox_mode (True)
- This ensures the bot uses the live Binance API instead of the testnet.
  
2. Run the Bot:
- python trading_bot.py
- The bot starts trading with real funds on Binance and processes 50 coins every 2 seconds.


3. Monitor Output:
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

4. Withdraw Funds:
- Every 60 seconds, you’ll see:
- Enter coin to withdraw (e.g., BTC, ETH, XRP) or 'skip':
- Enter a coin (e.g., `XRP`), amount (e.g., `1.0`), and testnet wallet address, or type `skip`.


5. Stop the Bot:
- Press `Ctrl+C` to exit.


## Configuration
- Coins: Edit the SYMBOLS list in trading_bot.py to change the 50 pairs.
- Trade Amounts: Adjust TRADE_AMOUNTS for custom quantities (e.g., 0.001 BTC, 0.1 SOL, 1.0 XRP).
- Timeframe: Change TIMEFRAME (default: 1m) to 5m, 15m, etc., if desired.
- SMA Periods: Modify window=3 and window=10 in analyze_data() for different SMA lengths.


## Notes
- Live Trading: This bot uses real funds via the Binance API.
- Double-check TRADE_AMOUNTS and test with small amounts first to avoid unintended losses.
- Rate Limits: 2-second sleep avoids
Binance API limits for 50 coins.
- Errors: If a coin fails (e.g., market unavailable), it skips to the next one.
- Security: Keep your .env file secure and never share your API keys.

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
- API Errors: Verify .env has correct keys and Binance API permissions (trading, withdrawals).
- No Trades: Ensure your account has funds and the market is active.
- Performance: Increase
time.sleep (2) if rate-limited by Binance.


## License
- MIT License feel free to modify and share!






