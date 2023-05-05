from typing import List


class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def check(s,word):
            i = j =0
            while i<len(s) and j<len(word):
                if s[i] !=word[j]:
                    return False
                ch  = s[i]
                counti = 0
                while i <len(s) and s[i] ==ch:
                    counti+=1
                    i+=1
                countj = 0
                while j<len(word) and word[j] ==ch:
                    countj+=1
                    j+=1
                if counti<countj:
                    return False
                if countj !=counti and counti<3:
                    return False
            return i ==len(s) and j ==len(word)
        ans = 0
        for word in words:
            ans +=1 if check(s,word) else 0
        return ans

if __name__ == '__main__':
    S = "heeellooo"
    words = ["hello", "hi", "helo"]
    test = Solution()
    print(test.expressiveWords(S, words))
