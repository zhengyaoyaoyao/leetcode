from typing import List

'''
用数组来记录信息
'''


class Solution1:
    def setZeroes1(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 先记录找到要修改的（i，j）元组，然后赋值
        m = len(matrix)
        n = len(matrix[0])
        row, col = [False] * m, [False] * n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = col[j] = True

        for i in range(m):
            for j in range(n):
                if row[i] or col[j]:
                    matrix[i][j] = 0


'''
用2个标签来记录
'''


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        # 查看第一列有没有0值
        flag_col0 = any(matrix[i][0] == 0 for i in range(m))
        # 查看第一行有没有0值
        flag_raw0 = any(matrix[0][j] == 0 for j in range(n))
        # 下面两个for 就解决了出1行和1列外其他元素的替换。
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # 现在处理第一行和第一列
        if flag_col0:
            for i in range(m):
                matrix[i][0] = 0
        if flag_raw0:
            for j in range(n):
                matrix[0][j] = 0

'''
再省略就是可以就用第一列作为存储，第一行如果有就直接先改。看做是有
'''


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        flag_col0 = False

        for i in range(m):
            if matrix[i][0] == 0:
                flag_col0 = True
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(m - 1, -1, -1):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if flag_col0:
                matrix[i][0] = 0


if __name__ == '__main__':
    test = Solution()
    matrix = [[1, 1, 0, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [0, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
    test.setZeroes(matrix)
