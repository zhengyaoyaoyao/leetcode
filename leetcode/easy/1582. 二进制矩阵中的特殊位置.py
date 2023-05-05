from typing import List

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows_sum = [sum(row) for row in mat]
        cols_sum = [sum(col) for col in zip(*mat)]
        res = 0
        for i, row in enumerate(mat):
            for j, x in enumerate(row):
                if x == 1 and rows_sum[i] == 1 and cols_sum[j] == 1:
                    res += 1
        return res

if __name__ == '__main__':
    mat = [[1, 0, 0],
           [0, 0, 1],
           [1, 0, 0]]
    test = Solution()
    print(test.numSpecial(mat))