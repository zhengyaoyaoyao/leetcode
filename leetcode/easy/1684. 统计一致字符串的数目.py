from typing import List

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res =0
        for word in words:
            for i in word:
                if i not in allowed:
                    break
            else:
                res+=1
        return res