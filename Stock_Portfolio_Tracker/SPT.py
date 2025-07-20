# Hardcoded stock prices dictionary
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 130,
    "MSFT": 300,
    "AMZN": 140
}

portfolio = {}
total_investment = 0

print("[]Welcome to Stock Portfolio Tracker")
print("Available Stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("Enter stock symbol (or type 'done' to finish): ").upper()
    
    if stock == "DONE":
        break
    
    if stock in stock_prices:
        try:
            quantity = int(input(f"Enter quantity for {stock}: "))
            portfolio[stock] = portfolio.get(stock, 0) + quantity
        except ValueError:
            print("Invalid input! Quantity must be an integer.")
    else:
        print("Stock not found in price list!")

# Calculate total investment
print("\n--- Portfolio Summary ---")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    investment = price * qty
    total_investment += investment
    print(f"{stock}: {qty} shares @ ${price} = ${investment}")

print(f"\nTotal Investment Value: ${total_investment}")

# Optional: Save to file
save_option = input("\nDo you want to save the result to a file? (yes/no): ").lower()
if save_option == "yes":
    with open("portfolio_summary.txt", "w") as file:
        file.write("--- Portfolio Summary ---\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            investment = price * qty
            file.write(f"{stock}: {qty} shares × ${price} = ${investment}\n")
        file.write(f"\nTotal Investment Value: ${total_investment}\n")
    print(" Portfolio saved to portfolio_summary.txt")
