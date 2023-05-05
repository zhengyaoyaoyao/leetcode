from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        newHeights = [0]*len(heights)
        #复制一个数组，然后对新的排序
        for i in range(len(heights)):
            newHeights[i] = heights[i]
        newHeights.sort(reverse=True)
        res = []
        for i in range(len(newHeights)):
            for j in range(len(heights)):
                if newHeights[i] == heights[j]:
                    res.append(j)
                    break
        ans = []
        for i in range(len(res)):
            ans.append(names[res[i]])
        return ans

# 语法题 就是zip函数
'''
zip函数是返回一个列表的，这个列表里面是一个个的元组。所以是可以排序的。
'''
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [name for _,name in sorted(zip(heights,names),reverse=True)]


if __name__ == '__main__':
    names =["Mary","John","Emma"]
    heights=  [180,165,170]
    test= Solution()
    print(test.sortPeople(names,heights))



