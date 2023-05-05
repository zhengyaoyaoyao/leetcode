'''
方法一：
既然是找第几个最小值/第几个最大值：要想到最小堆/最大堆，
那就是想想这个堆应该是什么样的，我们能想到这些值是3x，5x，7x的集合。一次就是一个循环。然后不断的添加循环。
'''
import heapq


class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        factors = [3,5,7] # 用于因子计算
        seen  = {1} #
        heap = [1]
        for i in range(k-1):
            curr = heapq.heappop(heap)
            for factor in factors:
                nxt = curr*factor
                if nxt not in seen:
                    seen.add(nxt)
                    heapq.heappush(heap,nxt)
        return heapq.heappop(heap)

'''
动态规划
思想就是因为必须只有3，5，7这几个因子
所以从1开始乘，后面就是乘5等等。那么就可以维护一个队列
'''

class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        ans=[1]*(k+1)
        i3,i5,i7 = 1,1,1
        for idx  in range(2,k+1):
            a,b,c = ans[i3]*3,ans[i5]*5,ans[i7]*7
            cur = min(a,b,c)
            i3 = i3 +1 if cur ==a else i3
            i5 = i5 +1 if cur ==b else i5
            i7 = i7 +1 if cur ==c else i7
            ans[idx] = cur
        return ans[k]


if __name__ == '__main__':
    k=5
    text =Solution()
    print(text.getKthMagicNumber(k))
