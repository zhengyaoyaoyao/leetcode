from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        ans =[[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                ans[j][n-i-1]=matrix[i][j]
        matrix[:]=ans

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # 先水平翻转
        for i in range(n//2):
            for j in range(n):
                matrix[i][j],matrix[n-i-1][j] = matrix[n-i-1][j],matrix[i][j]
        # 再角对角线旋转
        for i in range(n):
            for j in range(i):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

