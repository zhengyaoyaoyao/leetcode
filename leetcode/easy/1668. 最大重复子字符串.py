class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        res = 0
        while(res*word) in sequence:
            res+=1
        res-=1
        return res


if __name__ == '__main__':
    sequence ="aaabaaaabaaabaaaabaaaabaaaabaaaaba"
    word = "aaaba"
    test = Solution()
    print(test.maxRepeating(sequence,word))