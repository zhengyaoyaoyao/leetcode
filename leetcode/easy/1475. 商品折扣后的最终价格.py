from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for slow in range(len(prices)):
            for quick in range(slow+1,len(prices)):
                if prices[quick]<=prices[slow]:
                    prices[slow]=prices[slow]-prices[quick]
                    break
        return prices

'''
使用单调栈+哈希表
'''
class Solution1:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res=[]
        stack=[]
        for num in reversed(prices):
            while stack and num<stack[-1]:
                stack.pop()
            res.append(num-stack[-1] if stack else num)
            stack.append(num)
        res.reverse()
        return res

if __name__ == '__main__':
    prices = [8, 4, 6, 2, 3]
    test = Solution1()
    print(test.finalPrices(prices))