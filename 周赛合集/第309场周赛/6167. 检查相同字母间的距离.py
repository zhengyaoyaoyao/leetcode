from collections import defaultdict
from typing import List


class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        visited = set()
        for i in range(len(s)):
            if s[i] in visited:
                continue
            visited.add(s[i])
            dit = ord(s[i])-97
            dit = distance[dit]
            if i+dit+1<len(s) and s[i+dit+1]==s[i]:
                continue
            else:
                return False
        return True
class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        #因为有26个字母。那就直接存就好了，如果在里面是0说明还没有遍历，那就把当前位置放进去，等再次遍历到了那就计算看下等不等
        visited = [0]*26
        for i ,c in enumerate(s):
            # 现在就是要存一下字母的相对位置
            c = ord(c)-ord('a')
            #如果这个字母已经存进去了。并且计算下当前和之前存的位置如果和distance不等，那就是有问题
            if visited[c] and i -visited[c] !=distance[c]:
                return False
            visited[c] = i+1
        return True


if __name__ == '__main__':
    s = "abaccb"
    distance = [1, 3, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    test = Solution()
    print(test.checkDistances(s,distance))