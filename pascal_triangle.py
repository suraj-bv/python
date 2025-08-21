from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for row in range(numRows):
            new_row = [1] * (row + 1)
            for col in range(1, row):
                new_row[col] = triangle[row-1][col-1] + triangle[row-1][col]
            triangle.append(new_row)

        return triangle
    
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for i in range(rowIndex):
            row = [x + y for x, y in zip([0] + row, row + [0])]
        return row