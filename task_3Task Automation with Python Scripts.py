import yfinance as yf

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}  # Dictionary to store stock symbol and number of shares
    
    def add_stock(self, symbol, shares):
        """Add stock to the portfolio."""
        if symbol in self.portfolio:
            self.portfolio[symbol] += shares
        else:
            self.portfolio[symbol] = shares
        print(f"Added {shares} shares of {symbol} to the portfolio.")
    
    def remove_stock(self, symbol):
        """Remove stock from the portfolio."""
        if symbol in self.portfolio:
            del self.portfolio[symbol]
            print(f"Removed {symbol} from the portfolio.")
        else:
            print(f"Stock {symbol} not found in the portfolio.")
    
    def view_portfolio(self):
        """Display the current portfolio."""
        if not self.portfolio:
            print("Your portfolio is empty.")
            return
        
        print("\nCurrent Portfolio:")
        for symbol, shares in self.portfolio.items():
            print(f"{symbol}: {shares} shares")
    
    def get_portfolio_value(self):
        """Calculate the current value of the portfolio using real-time data."""
        total_value = 0
        if not self.portfolio:
            print("Your portfolio is empty.")
            return
        
        print("\nFetching real-time stock prices...")
        for symbol, shares in self.portfolio.items():
            stock = yf.Ticker(symbol)
            stock_info = stock.history(period="1d")  # Fetch the latest price
            latest_price = stock_info['Close'][0]
            stock_value = latest_price * shares
            total_value += stock_value
            print(f"{symbol}: {shares} shares @ ${latest_price:.2f} each = ${stock_value:.2f}")
        
        print(f"\nTotal Portfolio Value: ${total_value:.2f}")
        return total_value

# Example usage
portfolio = StockPortfolio()

portfolio.add_stock("AAPL", 10)
portfolio.add_stock("MSFT", 5)
portfolio.view_portfolio()
portfolio.get_portfolio_value()

portfolio.remove_stock("AAPL")
portfolio.view_portfolio()
portfolio.get_portfolio_value()
