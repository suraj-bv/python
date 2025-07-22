# this code is for calculating maximum profit from stock prices in multiple transactions
# this code calculates the sum of all the profits made by buying and selling stocks on different days

from typing import List


class Solution:
    def maximumProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        
        return profit






# this code is for calculating maximum profit from stock prices in one transaction
# one maximum profit can be made by buying at the lowest price and selling at the highest price after that
from typing import List
class Solution:
    def maximumProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = prices[0]
        
        for price in prices[1:]:
            current_profit = price - min_price
            
            if current_profit > profit:
                profit = current_profit
                
            if price < min_price:
                min_price = price
                
        return profit
        