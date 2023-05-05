from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        length = len(code)
        ans = [0]*length
        if k >0:
            for i in range(len(code)):
                if i+1+k>length:
                    ans[i] = sum(code[i+1:])+sum(code[:k-(length-i)+1])
                else:
                    ans[i] = sum(code[i+1:i+k+1])
        elif k<0:
            k = -1*k
            for i in range(len(code)):
                if i-k<0:
                    ans[i] = sum(code[:i])+sum(code[length-(k-i):])
                else:
                    ans[i] = sum(code[i-k:i])
        return ans


if __name__ == '__main__':
    code =  [1,2,3,4]
    k = 0
    test = Solution()
    test.decrypt(code,k)