class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        bottles = numBottles
        empty = numBottles
        
        while empty >= numExchange:
            newBottles = empty // numExchange
            bottles += newBottles
            empty = newBottles + (empty % numExchange)
        
        return bottles