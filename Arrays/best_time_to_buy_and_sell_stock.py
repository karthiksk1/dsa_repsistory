"""
Problem: Best Time to Buy and Sell Stock

Description:
Given daily stock prices, buy once and sell on a later day.
Return the maximum profit. Return 0 if no profit is possible.

Example:
Input:  [7, 1, 5, 3, 6, 4]
Output: 5  (buy at 1, sell at 6)
"""


def max_stock_profit(prices):
    if len(prices) < 2:
        return 0
    min_price = prices[0]
    max_profit = 0
    for price in prices[1:]:
        profit = price - min_price
        if profit > max_profit:
            max_profit = profit
        if price < min_price:
            min_price = price
    return max_profit


prices = [7, 1, 5, 3, 6, 4]
print(max_stock_profit(prices))
