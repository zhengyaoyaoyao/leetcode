import collections
from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = collections.deque()
        for i in logs:
            if i =="../" :
                if len(stack)>0:
                    stack.pop()
            elif i== "./":
                continue
            else:
                stack.append(i)
        return len(stack)

if __name__ == '__main__':
    test = ["./","../","./"]
    demo = Solution()
    print(demo.minOperations(test))
