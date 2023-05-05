from typing import List


class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        cur=0
        maxValue = 0
        row = len(grid)
        col = len(grid[0])
        for i in range(0,row-2):
            for j in range(0,col-2):
                cur = sum(grid[i][j:j+3])+grid[i+1][j+1]+sum(grid[i+2][j:j+3])
                maxValue = max(maxValue,cur)
        return maxValue

if __name__ == '__main__':
    test = Solution()
    grid = [[6,2,1,3],[4,2,1,5],[9,2,8,7],[4,1,2,9]]
    print(test.maxSum(grid))
