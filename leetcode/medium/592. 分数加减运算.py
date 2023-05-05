from math import gcd


class Solution:
    def fractionAddition(self, expression: str) -> str:
        denominator, numerator = 0, 1  # 分子，分母
        i, n = 0, len(expression)
        while i < n:
            # 读取分子
            denominator1, sign = 0, 1
            if expression[i] == '-' or expression[i] == '+':
                if expression[i] == '-':
                    sign = -1
                i += 1
            while i < n and expression[i].isdigit():#判断其是不是数字
                denominator1 = denominator1 * 10 + int(expression[i])#读取第一个分子，*10是因为不一定一位数。
                i += 1
            denominator1 = sign * denominator1#加上符号构成第一个分子。
            i += 1

            # 读取分母
            numerator1 = 0
            while i < n and expression[i].isdigit():# 同理获取第一个分母。
                numerator1 = numerator1 * 10 + int(expression[i])
                i += 1

            denominator = denominator * numerator1 + denominator1 * numerator
            numerator *= numerator1
        if denominator == 0:
            return "0/1"
        g = gcd(abs(denominator), numerator)
        return f"{denominator // g}/{numerator // g}"

if __name__ == '__main__':
    test = Solution()
    print(test.fractionAddition('-1/2+1/2+1/3'))