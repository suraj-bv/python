class Solution:
    def arrangeCoins(self, n: int) -> int:
        coins = 0
        row = 0
        while n >= coins+1:
            coins += 1
            n -= coins
            row += 1

        return row