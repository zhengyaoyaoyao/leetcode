class Solution:
    def isHappy(self, n: int) -> bool:
        check  =set()
        while n not in check and n!=1:
            check.add(n)
            countSum = 0
            while n!=0:
                num = n%10
                n = n //10
                countSum = countSum+num**2
            n = countSum
        return n==1

'''
这其实是一个循环的概念，所以可以用快慢指针
'''
class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(number):
            total_sum = 0
            while number > 0:
                number, digit = divmod(number, 10)
                total_sum += digit ** 2
            return total_sum

        slow_runner = n
        fast_runner = get_next(n)
        while fast_runner != 1 and slow_runner != fast_runner:
            slow_runner = get_next(slow_runner)
            fast_runner = get_next(get_next(fast_runner))
        return fast_runner == 1


if __name__ == '__main__':
    n = 19
    test = Solution()
    print(test.isHappy(n))