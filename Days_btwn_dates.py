from datetime import datetime

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        fmt = "%Y-%m-%d"
        d1 = datetime.strptime(date1, fmt)
        d2 = datetime.strptime(date2, fmt)
        return abs((d1 - d2).days)