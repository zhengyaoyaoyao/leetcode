"""
力扣最喜欢的位运算
1. 等价于：合理地分配这c2个1
2. 贪心
"""


class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        c2 = num2.bit_count()
        if c2 >= num1.bit_length():
            return (1 << c2) - 1
        c1 = num1.bit_count()
        # c2<c1,去掉1，等价于去掉num1最低的c1-c2个1.结果就是最小的值。
        # 一开始会疑惑为什么是去掉最低位而不是最高，因为你要找到消除的这个值，你必须至少有那么大。因为我们是直接在num1上改
        # x的lowbit
        # x&-x
        # x-=x&-x
        # x&=x-1
        while c2 < c1:
            num1 &= num1 - 1  # 去掉num1的最低的c1-c2个1
            c2 += 1
        # c2>c1 把最低的0变成1
        # y=~x
        # x|=y&-y
        # x| = x+1
        while c2 > c1:
            num1 |= num1 + 1
            c2 -= 1
        return num1


'''
下面是自己的版本，错误版本
'''


class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        if num2 == 0:
            return 0

        def check(num):
            a = list(str(format(num, 'b')))
            value = 0
            for i in range(len(a)):
                if a[i] == '1':
                    value += 1
            return value

        target = check(num2)
        checkValue = 2147483646
        houxuanAns = []
        for i in range(checkValue + 1):
            if target == check(i):
                houxuanAns.append(i)
        minValue = houxuanAns[0] ^ num1
        curMin = houxuanAns[0]
        for i in houxuanAns:
            cur = i ^ num1
            if cur < minValue:
                curMin = i
                minValue = cur
        return curMin


if __name__ == '__main__':
    test = Solution()
    num1, num2 = 65, 84
    print(test.minimizeXor(num1, num2))
