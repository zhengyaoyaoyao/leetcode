import collections
from typing import List

# 不能用加，加的话会出现前面加和等于后面的情况，必须计数或者排序。
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = [0]*len(strs)
        mp = collections.defaultdict(list)
        for index in range(len(strs)):
            for i in range(len(strs[index])):
                ans[index]=ans[index]+ord(strs[index][i])-ord('a')+1
            mp[ans[index]].append(strs[index])
        return list(mp.values())

class Solution1:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)
        for st in strs:
            counts=[0]*26
            for ch in st:
                counts[ord(ch)-ord("a")]+=1
            mp[tuple(counts)].append(st)
        return list(mp.values())

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp=  collections.defaultdict(list)
        for st in strs:
            key  = "".join(sorted(st))
            mp[key].append(st)
        return list(mp.values())

if __name__ == '__main__':
    strs = ["ac","c"]
    test =Solution()
    print(test.groupAnagrams(strs))