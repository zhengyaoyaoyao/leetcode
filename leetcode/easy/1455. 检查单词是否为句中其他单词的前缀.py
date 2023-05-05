class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words=sentence.split(" ")
        ans =-1
        for index in range(len(words)):
            if words[index].startswith(searchWord):
                ans = index+1
                break
        return ans