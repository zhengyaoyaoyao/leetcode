from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n=len(grid[0])
        ans = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                new_i=(i+int((j+k)/n))%m
                new_j=(j+k)%n
                ans[new_i][new_j]=grid[i][j]
        return ans

if __name__ == '__main__':
    test = Solution()
    grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]
    print(test.shiftGrid(grid,4))