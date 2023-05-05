from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        nums = [[0]*n for _ in range(n)]
        startx,starty =0,0
        loop,mid = n//2,n//2
        count=1
        for offset in range(1,loop+1):
            for i in range(starty,n-offset):
                nums[startx][i] = count
                count+=1
            for i in range(startx,n-offset):
                nums[i][n-offset]=count
                count+=1
            for i in range(n-offset,starty,-1):
                nums[n-offset][i]=count
                count+=1
            for i in range(n-offset,startx,-1):
                nums[i][starty]=count
                count+=1
            startx+=1
            starty+=1
        if n%2 !=0:
            nums[mid][mid]=count
        return nums


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        l,r,t,b = 0,n-1,0,n-1
        mat = [[0]*n for _ in range(n)]
        count,tar = 1,n*n
        while count<=tar:
            for i in range(l,r+1):
                mat[t][i]=count
                count+=1
            t+=1
            for i in range(t,b+1):
                mat[i][r]=count
                count+=1
            r-=1
            for i in range(r,l-1,-1):
                mat[b][i] = count
                count+=1
            b-=1
            for i in range(b,t-1,-1):
                mat[i][l]=count
                count+=1
            l+=1
        return mat