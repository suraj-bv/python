class Solution:
    def addDigits(self, num: int) -> int:
        def addedSum(num, prevSum):
            last = num % 10
            prevSum += last
            num = num // 10

            return num, prevSum

        while num >= 10:
            prevSum = 0
            while num > 0:
                num, prevSum = addedSum(num, prevSum)    
            num  = prevSum
    
        return num