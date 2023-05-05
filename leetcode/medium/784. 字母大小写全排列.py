from collections import deque
from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []
        q = deque([''])
        while q:
            cur = q[0]
            pos  = len(cur)
            if pos ==len(s):
                ans.append(cur)
                q.popleft()
            else:
                if s[pos].isalpha():
                    q.append(cur+s[pos].swapcase())
                q[0]+=s[pos]
        return ans

if __name__ == '__main__':
    s = "a1b2"
    test = Solution()
    print(test.letterCasePermutation(s))