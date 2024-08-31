def max_profit(prices):
    profit = 0
    
    # Iterate through the price list
    for i in range(1, len(prices)):
        # If the price today is greater than the price yesterday, buy yesterday and sell today
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    
    return profit

# Example usage:
prices = [7, 1, 5, 3, 6, 4]  # Example price list
print("Maximum profit:", max_profit(prices))
 
