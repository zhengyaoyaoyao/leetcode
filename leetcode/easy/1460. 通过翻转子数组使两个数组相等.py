import collections
from typing import List


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        ans1= dict()
        ans2=dict()
        for i in arr:
            ans1[i]=0
        for i in target:
            ans2[i]=0
        for i in arr:
            if i in ans1:
                ans1[i]+=1
        for i in target:
            if i in ans2:
                ans2[i]+=1
        for key in ans1.keys():
            if key not in ans2 or ans1[key] !=ans2[key]:
                return False
        return True

#其实排个序就好了。然后一一对比。

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target.sort()
        arr.sort()
        return target==arr
#还有一个记录数组数量的函数counter（）

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return collections.Counter(target) ==collections.Counter(arr)