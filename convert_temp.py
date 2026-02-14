class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        res = []
        kel = celsius + 273.15
        fa = celsius * 1.80 + 32
        res.append(kel)
        res.append(fa)
        return res