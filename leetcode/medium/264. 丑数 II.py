import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        factors= [2,3,5]
        seen = {1}
        h = [1]
        for i in range(n-1):
            cur = heapq.heappop(h)
            for factor in factors:
                nxt = factor*cur
                if nxt not in seen:
                    seen.add(nxt)
                    heapq.heappush(h,nxt)
        return heapq.heappop(h)

'''
动态规划
'''
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ans = [1]*(n+1)
        i2,i3,i5 =1,1,1
        for idx in range(2,n+1):
            a,b,c = ans[i2]*2,ans[i3]*3,ans[i5]*5
            cur = min(a,b,c)
            i2  = i2 +1 if cur ==a else i2
            i3  = i3 +1 if cur ==b else i3
            i5  = i5 +1 if cur ==c else i5
            ans[idx] = cur
        return ans[n]



if __name__ == '__main__':
    test = Solution()
    n =10
    print(test.nthUglyNumber(n))