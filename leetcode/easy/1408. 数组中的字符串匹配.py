from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans=[]
        for i in range(len(words)):
            for j in range(len(words)):
                if  i==j:
                    continue
                if words[j].count(words[i]):
                    ans.append(words[i])
                    #是字串就行，直接添加后就结束。
                    break
        return ans

class Solution1:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        for i, x in enumerate(words):
            for j, y in enumerate(words):
                if j != i and x in y:
                    ans.append(x)
                    break
        return ans
if __name__ == '__main__':
    words = ["a", "aa", "aaaa", "aaaaa"]
    text = Solution1()
    print(text.stringMatching(words))