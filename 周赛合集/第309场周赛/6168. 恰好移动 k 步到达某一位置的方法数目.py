from math import comb


class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        """
        1. 关键词：方法数
        2. DP，这个可以从提示中找线索。DP就很看重这个状态描述，f[][]，那么这个状态存储是几维就要思考这个问题
            如果是一维的，存储了当前位置和目标位置的差距，那么步数就没有办法存储。所以需要二维信息去存，走到这里了，走了多少步。
        3.记忆化搜索
        """
        # 为了减少时间复杂度，那么就先判断如果本来就到不了，或者走到后是奇数都是不可能的，所以可以直接先剪枝
        d= abs(startPos-endPos)
        if d>k or d%2!=k%2:
            return 0
        MOD = 10**9 +7
        def f(x:int,left:int) ->int:
            #这种情况就是如果终点和起点的差值大于剩余步数了，那么就可以直接返回0了。
            if abs(x - endPos)>left:
                return 0
            #如果刚好剩余1步，那么就是返回1，有点类似走楼梯的意思
            if left ==0:
                return 1
            return (f(x-1,left-1)+f(x+1,left-1))%MOD
        return f(startPos,k)

'''
方法2：组合数学题，因为l表示向左走的步数，r表示向右走的步数。
r + l = k
r - l =start - end
所以r就能够算出来
r= (k+start -end)/2
那么就是在总共的步数k中选出r个向右走就行，那么答案就是C（r,k）
'''
class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        d= abs(startPos-endPos)
        if d>k or d%2 !=k%2:
            return 0
        MOD = 10**9 +7
        return comb(k,(d+k)//2) %MOD

