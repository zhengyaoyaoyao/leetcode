from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return list()
        n = len(matrix)
        m = len(matrix[0])
        l,r,t,b = 0,m-1,0,n-1
        count = 1
        ans = []
        while count <=m*n:
            for i in range(l,r+1):
                if count<=m*n:
                    ans.append(matrix[t][i])
                    count+=1
            t+=1
            for i in range(t,b+1):
                if count<=m*n:
                    ans.append(matrix[i][r])
                    count+=1
            r-=1
            for i in range(r,l-1,-1):
                if count<=m*n:
                    ans.append(matrix[b][i])
                    count+=1
            b-=1
            for i in range(b,t-1,-1):
                if count<=m*n:
                    ans.append(matrix[i][l])
                    count+=1
            l+=1
        return ans