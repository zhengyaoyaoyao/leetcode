class Solution:
    def smallestValue(self, n: int) -> int:
        # 直到这个数是个质数就行。
        pre = float("inf")
        while pre>n:
            # 计算这个质数的和
            sum = 0
            pre = n
            i = 2
            while i<=n:
                while n%i ==0:
                    sum+=i
                    n/=i
                i+=1
            n = sum
        return n
