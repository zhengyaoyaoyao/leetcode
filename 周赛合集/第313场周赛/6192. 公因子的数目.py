from math import gcd


class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        num = 0
        check = min(a, b)
        for i in range(1, check + 1):
            if a % i == 0 and b % i == 0:
                num += 1
        return num


class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        # 找到最大公因子，最大公因子的因子数就是两个数的因子数。
        g = gcd(a, b)
        ans = 0
        i = 1
        # 只要遍历到根号g即可
        while i * i <= g:
            if g % i == 0:
                ans += 1
                # g/i 也是一个因子
                # 但是当 i*i==g 的时候，i ==g/i 只能算是一个
                if i * i < g:
                    # 这个意思是如果i是因子，因为g是公因子，所以另一个肯定也是。这判断防止重复因子
                    ans += 1
            i+=1
        return ans