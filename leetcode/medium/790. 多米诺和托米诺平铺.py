# 注意分析前一个阶段的四种情况，对后续情况的影响。

class Solution:
    def numTilings(self, n: int) -> int:
        f = [[0]*4 for _ in range(n+10)]
        f[1][0] = f[1][1] =1
        for i in range(2,n+1):
            f[i][0] = f[i-1][1]
            f[i][1] = sum([f[i-1][j] for j in range(4)])
            f[i][2] = f[i-1][0] +f[i-1][3]
            f[i][3] = f[i-1][0] +f [i-1][2]
        return f[n][1] %1000000007

