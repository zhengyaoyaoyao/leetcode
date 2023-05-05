class Solution:
    def numTrees(self, n: int) -> int:
        G=[0]*(n+1)
        G[0]=1
        G[1]=1
        # i 表示的是有几个数作为不同值得最后总数。j表示每次加入新得值后1-i个节点都为根时的数。
        for i in range(2,n+1):
            #这里j为什么取值1-i+1，因为要以不同的节点作为根，
            for j in range(1,i+1):
                G[i]+=G[j-1]*G[i-j]
        return G[n]

'''
solution2:
'''
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        C = 1
        for i in range(0, n):
            C = C * 2*(2*i+1)/(i+2)
        return int(C)