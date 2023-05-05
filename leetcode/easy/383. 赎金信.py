import collections


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # 最简单就是哈希
        if len(magazine)<len(ransomNote):
            return False
        check = collections.Counter(magazine)
        for i in range(len(ransomNote)):
            check[ransomNote[i]]-=1
            if check[ransomNote[i]]<0 or ransomNote[i] not in check:
                return False
        return True

if __name__ == '__main__':
    ransomNote = "aa"
    magazine = "aab"
    test = Solution()
    print(test.canConstruct(ransomNote,magazine))