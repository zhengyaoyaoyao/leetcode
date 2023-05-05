from math import sqrt


class Solution:
    def factorial(self,n):
        '''阶乘'''
        res = 1
        for i in range(1, n + 1):
            res = res * i
            res %=(10**9+7)
        return res
    def isPrime(self,n: int):
        '''判断质数'''
        if n == 1:
            return 0
        for i in range(2,int(sqrt(n))+1):
            if n % i == 0:
                return 0
        return 1
    def numPrimeArrangements(self, n: int) -> int:
        numPirmes = sum(self.isPrime(i) for i in range(1,n+1))
        return (self.factorial(numPirmes) * self.factorial(n-numPirmes)) % (10**9+7)

if __name__ == '__main__':
    test = Solution()
    print(test.numPrimeArrangements(5))
    # print(6%(10**9)+7)
